---
title: "Tisp v0.1 Release"
tags: tech programming languages projects
categories: tech
date: 2024-11-21
---

After over 7 years of off-and-on development (but mostly off),
I am finally releasing the first version of Tisp, the tiny lisp programming language.
Tisp is far from complete or being ready to use in the real world,
but I am now satisfied at the current state of features.

Before the idea of tisp ever formed, I worked on a shell interpreter called [s][].
It is a traditional shell which aimed to replace the complexity of bash.
When creating tisp, I brought this experience with me and wanted to make tisp a practical language
for everyday interactive use, shell scripting, and quick but powerful one-liners.

The desire to have a small, simple language, easy to embed or extend with external libraries,
originally inspired the creation Tisp.
Initially, Lua seemed to fit these requirements, 
but it lacks expressive power, which leads to verbose and repetitive code.
You cannot tailor Lua to the specific domain where you embed it.
Lua's imperative nature leads to programs which focus on the step by step operations to solve a problem, not the big picture.
This mandatory ceremony adds noise which clutters the core business logic at the heart of the problem solution.
Global by default encourages writing messy spaghetti code which manipulates global state, making programs impossible to reason about locally.
By more carefully selecting a higher level of abstraction, abandoning the imperative semantics of Lua can lead to an even simpler core language.

Together this eventually motivated the creation of a new language which combines the simplicity of Lua with the functional and expressive power of lisp and pragmatism of shell.

[s]: https://github.com/rain-1/s

# Current Features

- Interactive read-eval-print-loop (REPL) interface, with readline keybindings [^rlwrap].
- S-expression based homoiconic syntax.
  - Enables simple yet powerful macros to extend syntax by manipulating code like data.
  - Prefix syntax for `Func`, `quote`, `quasiqutote`, `unquote`, and `unquote-splice`.
- Runtime evaluation
  - Full language is always available: `read`, `parse`, `eval`, and `print` eevo code during runtime.
- Symmetric printing: values are printed in a format that can be read by the parser
  (with the exception of procedures).
- Basic error messages and debugging through backtrace `bt`.
- Strings and symbols are interned to reduce memory and enable fast comparisons.
- Sizeable core library written in tisp for control flow, lists, stacks, math, and IO.
- Builtin documentation for every procedure, accessed through `doc` function at runtime.

[^rlwrap]: Through the use of [rlwrap](https://github.com/hanslub42/rlwrap).

# Library

Tisp is designed as a library first, which can be easily included in any C project (or language with C bindings),
or inversely call any library with C bindings.
Tisp is essentially just a collection of functions which provide a high-level runtime for C.
The language's syntax is defined by the `parse` function, which transforms a string of tisp code into a tisp value.
The language's semantics are defined by the `eval` function, which transforms a value into its evaluated form (performing any side-effects along the way).
Then the language defines how to display the results with the `display` function.[^MVC]

[^MVC]: Web and game devs might see this as similar to the model-view-controller design pattern.

Currently the only application which uses tisp as a library is the default CLI interpreter.
Other possible applications include 
a notebook interface (like [juptyer][] notebook for python),
game platform (similar to [love2d][] or [pico-8][]),
a text editor (like lua for [neovim][], or elisp for [emacs][]),
or a spreadsheet (replacing visual basic).

[jupyter]: https://jupyter.org/
[love2d]: https://love2d.org/
[pico-8]: https://www.lexaloffle.com/pico-8.php
[neovim]: https://neovim.io/
[emacs]: https://www.gnu.org/software/emacs/

# Interpreter

While tisp is a library first, a default interpreter is provided as a standalone executable,
enabling execution of tisp programs from the command line.
It also serves as an example on how to use tisp as a library.

- `-r` launch REPL prompt (Default if no other options given).
- `-c` run command as tisp code.
- `-` read from standard input.
- if no hyphen prefix, run program in file.

# Types

- Integers, decimals, (with scientific notation for both) and rationals.
- Strings
  - Supporting backslash escape codes for newline, carriage return, tab, and double quote.
- Symbols
  - Variable identifiers as first class objects.
- Functions (and primitives from host language)
  - Including captured environment for closures.
- Macros (and special forms from host language)
  - Functions which operate on syntax, treating code as data.
- Pairs
  - Building block used to construct lists, trees, graphs, stacks, queues, etc.
- Nil
- Void
- Error

# Variables

- `True`
  - All values except `Nil` are truthy, use `True` as explicit true value.
- `False`
  - Equivalent to `Nil`
- `bt`
  - Backtrace of procedure call history which caused error
- `version`
  - String of current version: `"0.1"`

# Builtins

Procedures defined by the host runtime (currently only C).
Each procedure is either a primitive which behaves like a normal function,
or a special form which might not evaluate some of its arguments (eg `quote`, `cond`).
See the documentation of each primitive for more information.

- `car`, `cdr`
- `cons`
- `quote`
- `eval`
- `=`
- `cond`
- `typeof`
- `get`
- `Func`
- `Macro`
- `def`
- `undefine`
- `defined?`
- `load`
- `error`

## IO

- `read`
- `write`
- `parse`

## OS

- `cd!`
- `pwd`
- `now`
- `time`

## String

- `Sym`
- `Str`

## Math

- `+`, `-`, `*`, `/`, `mod`, `^`
- `<`, `>`, `<=`, `>=`
- `Int`, `Dec`
- `floor`, `ceil`, `round`
- `sin`, `cos`, `tan`
- `sinh`, `cosh`, `tanh`
- `arcsin`, `arccos`, `arctan`, `arcsinh`, `arccosh`, `arctanh`
- `exp`, `log`

# Core Library

Functions defined in eevo, included by default but not required.

- `list`, `list*`
- `if`, `when`, `unless`
- `not`, `and`, `or`, `nand`, `nor`
- `let`, `recur`, `switch`
- `apply`, `map`
- `do`, `do0`
- `compose`
- `caar`, `cadr`, `cdar`, `cddr`, etc.
- Type tests `nil?`, `int?`, `string?`, etc.
- `defmacro`
- `quasiqutote`

- `length`
- `last`, `nth`, `head`, `tail`
- `convert`, `filter`, `keep`, `remove`, `memp`, `member`
- `reverse`
- `count`, `every?`, `everyp?`
- `assoc`
- `append`, `zip`
- `push`, `pop`, `peek`, `swap`

- `doc`
- `repl`

### IO

- `print`, `display`, `println`, `displayln`, `newline`
- `run`

### Math

- `pi`, `tau`, `e`
- `/=`,
- `inc`, `dec`, `truncate`
- `sqr`, `cube`, `root`, `sqrt`, `cbrt`
- `logb`, `log10`
- `csc`, `sec`, `cot`, `arccsc`, `arcsec`, `arccot`
- `csch`, `sech`, `coth`, `arccsch`, `arcsech`, `arccoth`
- `abs`, `sgn`, `max`, `min`,
- `positive?`, `negative?`, `zero?`, `even?`, `odd?`,
- `dot`, `!`

# Next Steps

This is likely the first and last release of Tisp.
Tisp has always been a temporary name.
As the language moves away from the signature lisp style and starts taking more inspiration from
other languages, a rebrand is in order.
One of the primary motivators for this release is so I can fundamentally change much of core language, 
such as the syntax, data structures, and type system.

I have already started implementing a new syntax system built on top of s-expressions,
to remove top level parentheses and forced prefix notation.

While this is the far from the end of the language, a significant revamp is coming.
