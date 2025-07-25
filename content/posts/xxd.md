---
title: "Read Files at Compile Time in C"
date: 2021-01-30
tags: tech c make
categories: tech
---

Any [beginners C tutorial][1] will teach the basics of the C standard library's
file reading functions (eg `fopen`). The limitations of these interfaces is that they are designed
for run time reading, meaning that the file will be opened and read when the program is executed.
For most cases this is exactly what is wanted, often the file is only given at
run time by the user. However, there might be situations where instead it needs to read files
at compile time, similar to having a statically linked library. For example, I use this in my
[hobby programming language][2] to include the language's standard library written in the language
itself. This is done at compile time so it is statically bundled with the binary and requires no
external text file dependencies.

[1]: https://www.tutorialspoint.com/cprogramming/c_file_io.htm
[2]: https://eevo.pub

To achieve this a command line tool called xxd can be used. xxd is tool to create hex dumps of any
file given to it, and might already be on your Linux distro as it is included with
[vim][3].

[3]: https://www.vim.org

Hex files are hexadecimal (base 16) representations of each byte of a file. Instead of printing
each letter as the character it represents, it displays the binary encoding as a base 16 number.
This allows reading of special and invisible characters such as newlines, tabs, and
spaces. The hex file encoding can also be easily imported into a C program with xxd.

To create hex files with xxd, simply give it the file name and it will print a hex dump to stdout.

`file.txt`:
```
Tomorrow, and tomorrow, and tomorrow,
Creeps in this petty pace from day to day,
To the last syllable of recorded time
```

`xxd file.txt` output:
```
$ xxd file.txt
00000000: 546f 6d6f 7272 6f77 2c20 616e 6420 746f  Tomorrow, and to
00000010: 6d6f 7272 6f77 2c20 616e 6420 746f 6d6f  morrow, and tomo
00000020: 7272 6f77 2c0a 4372 6565 7073 2069 6e20  rrow,.Creeps in
00000030: 7468 6973 2070 6574 7479 2070 6163 6520  this petty pace
00000040: 6672 6f6d 2064 6179 2074 6f20 6461 792c  from day to day,
00000050: 0a54 6f20 7468 6520 6c61 7374 2073 796c  .To the last syl
00000060: 6c61 626c 6520 6f66 2072 6563 6f72 6465  lable of recorde
00000070: 6420 7469 6d65 0a                        d time.
```

This default output is useful for humans to read, but not easy to get into a C program. Luckily
xxd includes an option to format the hex dump in a syntax C can parse. If supplied the flag `-i`
xxd outputs the hex bytes formatted as an array declaration in C syntax, where each element is
a byte of the file in hexadecimal.

```c
$ xxd -i file.txt
unsigned char file_txt[] = {
  0x54, 0x6f, 0x6d, 0x6f, 0x72, 0x72, 0x6f, 0x77, 0x2c, 0x20, 0x61, 0x6e,
  0x64, 0x20, 0x74, 0x6f, 0x6d, 0x6f, 0x72, 0x72, 0x6f, 0x77, 0x2c, 0x20,
  0x61, 0x6e, 0x64, 0x20, 0x74, 0x6f, 0x6d, 0x6f, 0x72, 0x72, 0x6f, 0x77,
  0x2c, 0x0a, 0x43, 0x72, 0x65, 0x65, 0x70, 0x73, 0x20, 0x69, 0x6e, 0x20,
  0x74, 0x68, 0x69, 0x73, 0x20, 0x70, 0x65, 0x74, 0x74, 0x79, 0x20, 0x70,
  0x61, 0x63, 0x65, 0x20, 0x66, 0x72, 0x6f, 0x6d, 0x20, 0x64, 0x61, 0x79,
  0x20, 0x74, 0x6f, 0x20, 0x64, 0x61, 0x79, 0x2c, 0x0a, 0x54, 0x6f, 0x20,
  0x74, 0x68, 0x65, 0x20, 0x6c, 0x61, 0x73, 0x74, 0x20, 0x73, 0x79, 0x6c,
  0x6c, 0x61, 0x62, 0x6c, 0x65, 0x20, 0x6f, 0x66, 0x20, 0x72, 0x65, 0x63,
  0x6f, 0x72, 0x64, 0x65, 0x64, 0x20, 0x74, 0x69, 0x6d, 0x65, 0x0a
};
unsigned int file_txt_len = 119;
```

This creates an array containing the contents of the file.  It also defines another variable as
the number of characters in the file, which is the length of the array.

Since xxd takes care of all the formatting, to import it in C simply save it
to a file `xxd -i file.txt > file.h` and include it `#include "file.h"` in the necessary C file.
You now have access to both variables, and therefore the contents of the file, without the need
for `fopen`. Because the generated header file is now being read instead of the file directly the
compiled binary does not need the original file to exist.

If all that is needed is to loop over each character, simply iterate over the array until the
length is reached.  However, in C character arrays can also be treated as strings (since strings
are just pointers, and arrays are specially allocated pointers). The only thing that is missing is
the null terminator required for standard strings. To insert this zero byte use the following to
append null to the end of the array:

```
xxd -i file.txt | tac | sed "3s/$/, 0x00/" | tac > file.h
```

Now the variable `file_txt` can be used as a regular string in the C code, reading the contents
of the file.

If multiple files need to be read, they can be included all at once as a single file by being
concatenated `cat file1.txt file2.txt | xxd -i -`. However, this will not produce the correct
output. When xxd reads from stdin it does not know the file name so does not know what to call the
variables. Instead it only outputs the formatted contents of the array, letting you set the
variables' names yourself.

This can be done by a simple make recipe which can be added to a project's `Makefile`:

```make
file.h: file1.txt file2.txt
	@echo xxd $@
	@echo "unsigned char fileh[] = { " > $@
	@cat $^ | xxd -i - >> $@
	@echo ", 0x00};" >> $@
	@echo "unsigned int fileh_len = `wc -c $^ | awk 'END{print $$1}'`;" >> $@
```

Here `file.h` is the produced header, and `file1.txt`, `file2.txt` are the files to be read.
Simply add `file.h` as a dependency to the C file which includes it to have the recipe run when
needed. For a real world use of this method see [my programming language][4].

[4]: https://github.com/eevolang/eevo/blob/7c45f869f460d12e3cb091c6a918dd66adb3cb80/Makefile#L28

Using xxd is a simple but effective way to convert any file to a C header, allowing it to be
included when compiled and removing the need for the file path to exist at run
time. While only basic ASCII text file examples were covered, this method also works for any
file (eg unicode text, images, PDFs, etc) since they all store data as a binary file which can be
converted to hexadecimal.  However, extra steps would need to be taken when reading these files,
for example in unicode each letter is not necessary a single byte or single element of the array.
