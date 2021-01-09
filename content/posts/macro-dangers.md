---
title: "The Dangers of C Macros"
date: 2018-09-11
tags: tech code c
categories: tech
---

C macros, while being extremely powerful when used correctly, can also be the
cause for a lot of unnecessary headaches if you are not aware of their
limitations. It is easy to view macros as just a fast shorthand for making
simple functions, but there are very important differences which need to be
addressed.

This post outlines some real life examples of macros I have come across or
attempted to use, some are very beneficial, improving life for everyone,
others are terrible and impossible to debug, and then some just are plain
stupid.

## intro

In C, macros are delegated to the preprocessor, a program run before the
compiler which changes the source C files so they are ready to be compiled.
This includes basic things such as removing comments or adding the contents of
others files with `#include`. The preprocessor also handles a crude, yet
powerful, form of constant variable creation with `#define`. For example, the
following makes the C preprocessor replaces every occurrence of `PI` with the
number `3.14159`.

```c
#define PI 3.14159
```

This is also extended to accept arguments, allowing for macros which act as
basic functions.

```c
#define RADTODEG(X) ((X) * 57.29578)
```

The preceding macro replaces every `RADTODEG(PI/2)`, with `((3.14159/2) *
57.29578)`, converting *π/2* radians to about 90 degrees.

## the good

```c
#define MAX(A, B)         ((A) > (B) ? (A) : (B))
#define MIN(A, B)         ((A) < (B) ? (A) : (B))
#define BETWEEN(X, A, B)  ((A) <= (X) && (X) <= (B))
#define LEN(X)            (sizeof(X) / sizeof((X)[0]))
```

Above is a list of four macros which I have in pretty much every project I am
working on, just because they are so useful. The first one, `MAX` returns the
larger of the two given numbers. This is a nice shorthand, making the code much
easier to read by hiding the ternary operator away. In companion with it is of
course `MIN`, which does exactly what you think it does.

Next, I often find my self needing `BETWEEN`, which returns whether or not the
given character `X` is inside `A` and `B`. One example of this is to figure out
if a given character is a lower case letter: `BETWEEN(c, 'a', 'z')`.  Finally,
`LEN` returns the length of an array, fairly basic and well needed.

## the bad

Here is a seemly innocent macro I wrote to check if a character is valid for a
specific application:

```c
#define ISVALID(C) (BETWEEN(C, 'a', 'z') || strchr("_-", C))
```

The macro should return 1 if the passed character, `C`, is a lowercase letter,
an underscore, or a hyphen. At first, it might seem like this macro works
perfectly fine, and it does for the most part; however, in certain cases, there
are undesirable side effects which are hard to figure out. For example, I
wanted to use this macro, which had been working well so far, to strip the
characters at the end of a string that are not valid. Simple enough, right?

```c
for (char *s = str; *s && ISVALID(*s++); len++)
	/* do nothing in here */ ;
str[len] = '\0';
```

This should move the terminating null character to where the last valid
character of the string is, but in this current usage, it doesn't seem to
work correctly. If you use the example string `"test-string! removed"`
you would expect `"test-string"`, instead you get `"te"`, which is much
shorter than it ought to be.

In order to know why this happens you have to understand what the C
preprocessor is doing under the hood. For every instance of `ISVALID`, C
replaces it with the defined expression, in this case `(BETWEEN(C, 'a', 'z') ||
strchr("_-", C))`.  If you specified arguments, which is the case for macros,
the variable is then replaced with every occurrence within the given
expression, so the for loop gets replaced with:

```c
for (char *s = str; *s && (('a' <= *s++ && *s++ <= 'z') || strchr("_-", *s++)); len++) ;
```

It should be clear now why this is producing weird results, the increment is
duplicated three times. When a function is run, each argument is evaluated
before being supplied to the body, but for macros, the preprocessor doesn't
understand the expression, it just blindly copies and pastes it to every
occurrence, causing the character to be incremented more times than wanted.

This subtle, but critical, distinction between macros and functions can cause
these hard to find bugs when you refuse to acknowledge their differences.

To solve this error I ended up just replacing this short macro with a function,
which in this case demonstrates some of the limitations of macros. Sometimes it
is just easier to use a function.

Another example I have come across is a macro used in a codebase to report and
keep count of any errors encountered. The initial version of this macro is
shown.

```c
#define report(M, ...)                                                        \
	fprintf(stderr, "%s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__); \
	errors++;
```

This works fine for many causes, but problems arise when you start to use it
more often in different situations. One of these use cases which no longer
works as intended is when you try to call it in an `if` statement.

```c
if (val != A_NUM)
	report("error: variable 'val' is [%d] not A_NUM", val);
```

In C the curly braces around a conditional statement can be omitted if the
statement only contains a single line. Most of the time this works fine and
makes the code look cleaner, but this example complicates things. While the
macro may look like a single line, when the preprocessor modifies it is now two
separate lines, the `fprintf` function and the `errors++` statement. The `if`
statement only encompasses the `fprintf`, so the program always increments
`errors` by one, even if `val` is the desired value and there is no issue.

At first, this seems easy enough to fix, once you realize that you are calling
a multi-lined macro, not a function, you just add some curly braces to your
macro.

```c
#define report(M, ...) {                                                      \
	fprintf(stderr, "%s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__); \
	errors++;                                                             \
}
```

This does indeed solve this particular problem, but it also introduces some
others.  Later on, I wanted to add an `else` to the `if` statement, but the
compiler spat out a syntax error complaining that the there is no `if` for the
`else`.  After much examination, I realized that the semicolon after the macro
is actually not needed and is getting in the way of the `else`. When expanded
this code:

```c
if (str == NULL)
	report("error: variable str is NULL");
else
	do_something(str);
```

Becomes:

```c
if (str == NULL) {
	fprintf(stderr, "%s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__);
	errors++;
};
else
	do_something(str);
```

Now it is clear that this semicolon is separating the `if` and `else`
statements. You could just remove this semicolon since it's not actually
needed, but now it looks like your code is missing a semicolon, and every time
you use this macro you have to remember that you can't use a semicolon. This is
less than ideal, so instead, you can extend these curly braces to become a
do-while loop.

```c
#define report(M, ...) do {                                                   \
	fprintf(stderr, "%s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__); \
	errors++;                                                             \
} while(0)
```

Since it is a do-while loop it is always evaluated at least once, but because
the condition is `0`, it never repeats. A while loop also needs a semicolon at
the end, this allows us to include one after the macro, giving the programmer
the expected results. The do-while loop also only counts as one line, so the
shorten `if` statement notation can be used.

In this example, macros are still a very viable option, once you are aware of
their limitations.

## the ugly

The next portion is for serious macro abuses, one such example I found
stumbling through `tcsh`'s source code.

```c
#define DO_STRBUF(STRBUF, CHAR, STRLEN)				\
								\
struct STRBUF *							\
STRBUF##_alloc(void)						\
{								\
    return xcalloc(1, sizeof(struct STRBUF));			\
}								\
								\
void								\
STRBUF##_free(void *xbuf)					\
{								\
    STRBUF##_cleanup(xbuf);					\
    xfree(xbuf);						\
}								\
								\
const struct STRBUF STRBUF##_init /* = STRBUF##_INIT; */

DO_STRBUF(strbuf, char, strlen);
DO_STRBUF(Strbuf, Char, Strlen);
```

`tcsh`'s `tc.str.c` defines an 80 line long macro (small portion displayed
above, the whole mess is [here][1]) in order to duplicate a family of functions
to work with their `Char` variable type as well as normal `char`. The macro is
defined as `DO_STRBUF` which takes 3 arguments, a struct `STRBUF`, a type
`CHAR`, and a function `STRLEN`. `tcsh`'s old code base is designed to work on
many legacy and outdated systems, so it needs to support the various types of
`char`, such as `wchar_t`, `wint_t`, `short`, etc. The overly complex
assignment of `Char` can be seen [here][2]. For some reason, the authors
thought it best to include two types of these boilerplate functions, instead of
unifying them as one set, which would greatly improve the entire code base's
simplicity and readability.

## conclusion

If you are aware of macros' limitations then they can become a powerful
tool to quickly write clean and effective code. You always have to be careful
though when utilizing them, use your judgement to determine when their
advantages over normal functions become problems and headaches instead of fast
time savers.

[1]: https://github.com/tcsh-org/tcsh/blob/master/tc.str.c#L628-L710
[2]: https://github.com/tcsh-org/tcsh/blob/master/sh.h#L94-L124
