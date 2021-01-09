---
title: "Overview of libsl"
date: 2017-06-04
tags: tech c library suckless
categories: tech
---

![suckless](/img/posts/sl-header.png)

[libsl][8] is an extremely small library used to write better and clearer C
programs. The code was created by the [suckless][9] community, a small group of
C hackers and developers creating powerful yet simple programs for Linux
designed to be lightweight, configurable, and easier to maintain then the many
other unnecessarily bloated [alternatives][10]. You can read more about their
[philosophy][11] on their website. Some of their most notable projects include
[dwm][12], [dmenu][13], [st][14], and [surf][15].

libsl is composed of tiny C99 source and headers files designed to be simply
copied into a project's source tree. This allows the library to be easily used
and easily modified to fit every project's need.

All of libsl is protected under the MIT license, allowing you to use it in your
own projects with little strings attached. See [LICENSE][6] in the source tree
for more.

## arg.h

One of the most utilized and most important files in libsl is [arg.h][1], a
C header designed to easily interpret short options from the command line.
This removes the necessity to copy complex boiler plate or clunky libraries to
simply see if an option has been supplied by the user.  While `arg.h` does not
support long options (`--option` vs `-o`), if your project's CLI is relatively
straight forward it is a great, simple, and lightweight method to quickly parse
short options in your C code.

To start reading short options simply use the macro `ARGBEGIN` followed by a
`{` in your C program's `main` function, don't forget to `#include "arg.h"` at
the top of the file. This macro loops through all the command line arguments
and finds the short option (beginning with a single `-`) and allows you to
select one in a switch statement by using `case 'a':`, where `a` can be any
character for the desired option.

`arg.h` also defines other macros to read data in the `ARGBEGIN` block. One
example is `ARGC()` which is defined to `ARGBEGIN`'s internal variable `argc_`,
the character for the short option currently being interpreted.

`ARGF()` is another useful macro to get an argument after an option. For
example if a program `prog` is run as `prog -s string` then `ARGF()` in the `s`
case will return `string` as a C string. This can also be converted to a number
through a function such as `atoi`.  A similar macro `EARGF(x)` can also run the
supplied function upon an error. It is common to define a `usage()` function
in suckless projects such as the one below.

```c
void
usage(void)
{
	die("usage: %s [-ab] [-c STR] [-d STR] [-n NUM | -NUM]", argv0);
}
```

`die()` is a function in libsl defined in `util.c`, see the [section](#utilc)
below for more.

`arg.h` also defines a string, `argv0`, which is set to the program's name,
equivalent to `argv[0]`, but global allowing it to be used throughout your
code, like in the usage message above.

In this example `EARGF(usage())` would display usage info on an error reading
the next string.

While `ARGF()` with `atoi()` can be used to get a number from given arguments,
it is often faster to use the `-NUM` format (eg `prog -4` to get the number `4`
instead of `prog -n 4`). In order to achieve this I have added my own macros
to `arg.h` that can be used.

```c
/* handles -NUM syntax */
#define ARGNUM case '0':\
               case '1':\
               case '2':\
               case '3':\
               case '4':\
               case '5':\
               case '6':\
               case '7':\
               case '8':\
               case '9'

/* get option number */
#define ARGNUMF()	(brk_ = 1, atoi(argv[0]))
```

The first is `ARGNUM` which is used in replace of a case statement in the
`ARG` block (eg `case 'n':` becomes `ARGNUM:`). Inside of this case
replacement `ARGNUMF()` is used to get the number given by the argument
supplied by the user. These macros, while only needing to be defined for 1-9,
work on any number over 10 as well.

After running through all the options you want---remembering to use `break`
after each one, possibly including a `default` in case an argument given is not
supported---`ARGBEGIN` and the curly bracket we opened need to be
closed via `} ARGEND`.  `ARGEND` is essentially just closing all the brackets
`ARGBEGIN` opened, not counting the one we placed.

A complete `ARG` block example is shown below, don't forget that it needs to be
placed in inside the `int main(int argc, char *argv[])` function.

```c
ARGBEGIN {
case 'a':
	printf("option a selected\n");
case 'b':
	printf("option b also runs if your not careful\n");
	break;
case 'c':
	printf("options can also have arguments: %s\n", ARGF());
	break;
case 'd':
	printf("support for error messages: %s\n", EARGF(usage()));
	break;
case 'n':
	printf("they can also be numbers: %d\n", atoi(EARGF(usage())));
	break;
ARGNUM:
	printf("or in this format: %d\n", ARGNUMF());
	break;
case 'v':
	verbose++; /* define before ARGBEGIN block */
	printf("options can also be repeated: %d\n", verbose);
	break;
default:
	usage();
} ARGEND;
```

Note that `arg.h` modifies `argv` and `argc`. If, for example, after parsing
the arguments you now want to read any strings after, such as file names,
`argv[0]` is the first argument after the valid options. So if `prog -s option
filename anotherfile` is used, the `s` case in `ARGBEGIN` is run with the
argument `option`, then `argv[0]` will be equal to `filename`, `argv[1]` to
`anotherfile`, etc.

## util.c

The next file in libsl is [util.c][2]. This file defines many general purpose C
functions used throughout different projects.

One function found here which is common in many C projects, including
[Linux][7], is `die()`. This utility takes a formatted string, adds a newline
at the end, and prints it to `stderr` before `exit()`ing with a return value of
`1`. This is useful for writing simple and clean error messages which need to
quit the program. `die()` is used above in the `usage()` example as well as the
quick examples below.

```c
struct MyData data;
data->str = init_str();
if (!data->str || !strcmp(data->str, ""))
	die("%s: error: could not init data->str", argv0);
```

```c
int strlen = 20;
char *str;
if (!(str = calloc(strlen, sizeof(char))))
	die("fatal: could not calloc() %u bytes", strlen * sizeof(char));
```

As well as formatting the output similar to `printf()`, libsl's `die()` also
supports automatic error messages for functions which set the C global `errno`.
If the string given ends in a colon (`:`), `die()` will append a space and the
error message thrown by a called function with `errno` support. Thus the above
`calloc` example can be replaced with the more adaptive:

```c
int strlen = 20;
char *str;
if (!(str = calloc(strlen, sizeof(char))))
	die("calloc:"); /* example error: "calloc: out of memory" */
```

The above example is the bases for another useful function `util` defines,
`ecalloc()`. This new function makes sure the pointer allocated by `calloc` is
not `NULL`, which indicates an error occurred. Using this new wrapper we can
replace the example above with the following.

```c
int strlen = 20;
char *str = ecalloc(strlen, sizeof(char));
```

This function can also be duplicated for other similar functions such as
`realloc()`, `malloc()`, `strdup()`, etc. A new example `erealloc()` function
is displayed below.

```c
void *
erealloc(void *p, size_t size)
{
	if (!(p = realloc(p, size)))
		die("realloc:");

	return p;
}
```

### util.h

The [header][3], as well as defining the previous functions, creates some
useful macros.

Two macros which are often copy and pasted between projects and files is
`MAX()` and `MIN()`. They are fairly simple, two integers are given as
arguments and the biggest or smallest one is returned respectively.

```c
#define MAX(A, B)   ((A) > (B) ? (A) : (B))
#define MIN(A, B)   ((A) < (B) ? (A) : (B))
```

```c
MAX(4, 8);     /* => 8   */
MIN(-38, -18); /* => -38 */
MAX(10, -47);  /* => 10  */
```

In a similar vain `BETWEEN()` returns whether the first integer supplied is
between the next two given integers.

```c
#define BETWEEN(X, A, B)   ((A) <= (X) && (X) <= (B))
```

```c
BETWEEN(4, -8, 12); /* => 1 (true)  */
BETWEEN(9, 20, 67); /* => 0 (flase) */
```

`LEN()` is also often defined here, it is used to return the size of an array.

```c
#define LEN(X)            (sizeof(X) / sizeof((X)[0]))
```

## drw.c

[drw.c][4] and its header [drw.h][5] are used as an X interfaced for making
basic graphical programs, for example [dmenu](http://tools.suckless.org/dmenu).
An in depth overview of the many functions and `typedef`s offered in this file
is coming soon as its own post.

## conclusion

I hope this post has be beneficial and will help you create more elegant and
cleaner code in C. For other projects putting this philosophy into practice
checkout some of my [projects](/projects), the [suckless git
repo](http://git.suckless.org), and their other [recommended
projects](http://suckless.org/rocks) page.

[1]:  http://git.suckless.org/libsl/tree/arg.h
[2]:  http://git.suckless.org/libsl/tree/util.c
[3]:  http://git.suckless.org/libsl/tree/util.h
[4]:  http://git.suckless.org/libsl/tree/drw.c
[5]:  http://git.suckless.org/libsl/tree/drw.h
[6]:  http://git.suckless.org/libsl/tree/LICENSE
[7]:  https://github.com/torvalds/linux/blob/16f73eb02d7e1765ccab3d2018e0bd98eb93d973/arch/mn10300/boot/tools/build.c#L47
[8]:  http://git.suckless.org/libsl
[9]:  http://suckless.org
[10]: http://suckless.org/sucks
[11]: http://suckless.org/philosophy
[12]: http://dwm.suckless.org/
[13]: http://tools.suckless.org/dmenu
[14]: http://st.suckless.org/
[15]: http://surf.suckless.org/

