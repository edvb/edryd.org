---
title: "Understanding Vim's Indenting System"
date: 2017-04-30
tags: tech vim tutorial
categories: tech
---

![Vim](/img/posts/vim-indenting/vim.jpg)

Like most things in Vim, the indenting (tabs) system is complex making it
extremely flexible so that it can fit any programming language or use case.
However, the commands and terminology can be confusing for beginners, this
post is designed to explain all the different commands and options needed to
fully control and customize tab's size, type, and look for any purpose.

To start of you should know that Vim has two different types of tabs, hard tabs
and soft tabs. Hard tabs are a single `<TAB>` character per indent level, while
soft tabs are multiple spaces per level. Hard tabs, while being only one
character, can be displayed by a text editor or viewer as any size, normally 8.
Different languages have different recommendations for the type and length of
tab to use, so learning how to control them can sometimes be necessary to
format your code properly.

## creating indents

To insert a tab in Vim you can do it much like any other editor by pressing
`<TAB>` at the start of a line while in insert mode. In insert mode you can
also press `<C-t>` anywhere in the line to increase the lines indentation
and `<C-b>` to decrease.

In normal mode you can also use `>` and `<` followed by a motion to increase
and decrease the lines tabs as well. For example, `>>` will increase the tabs
on the current line, `>ap` will increase the indentation level of the entire
paragraph, `<j` will decrease two lines. The `>` and `<` commands also work
with a selected region in visual mode, but after every indent you have to
select the area again if you want to add another indent. To solve this I use
the following mapping in my `.vimrc` to automatically reopen the visual
selection for multiple levels of indents.

	vnoremap > >gv
	vnoremap < <gv

## stylizing indents

By default vim displays hard tabs as clear white space, however you can change
this with the `listchars` option. `listchars` has multiple different possible
options such as `eol`, `space`, `trail`, etc. The option we care about for
indents is `tab`, which takes two single character arguments: the first one
being the character shown at the start of a hard tab and the second one being
the character that is repeated for the rest of the tab space. See `:h
listchars` for more.

### examples

The following command sets the first character to a vertical bar `|` and the
rest of the tab to spaces. Remember to put the space at the end after the
second `\ `.

	:set listchars=tab:\|\

![tabs-1](/assets/img/posts/vim-indenting/tabs-1.png)

To have hard tabs look like dots you can use this:

	:set listchars=tab:··

![tabs-2](/assets/img/posts/vim-indenting/tabs-2.png)

Another example:

	:set listchars=tab:»-

![tabs-3](/assets/img/posts/vim-indenting/tabs-3.png)

### indent-guides plugin

This customization can be extending beyond what Vim offers by default with a
plugin such as [vim-indent-guides][1]. indent-guides lets you color and
stylize not only hard tabs, but soft ones, as well as many other features.

![indentation-guides](/assets/img/posts/vim-indenting/indent-guides.png)

## configuring indents

Now if you need to learn to manually change tabs settings, here is an outline
of the options:

 * `shiftwidth` sets the length that vim indents by (default 8)
 * `expandtab` makes Vim insert soft tabs instead of hard tabs (default off)
 * `noexpandtab` makes Vim hard tabs instead of soft ones (default: on)
 * `tabstop` changes displayed length of hard tabs in Vim only, should almost
    always be equal to `shiftwidth` (default 8)
 * `softtabstop` like `tabstop` but only for soft tabs (default 0)
 * `autoindent` automatically indent newline to the level of the last one
   (default off)
 * `smartindent` enables auto indenting based on context (eg after `{`)
   (default off)
 * `smarttab` when on Vim inserts tabs according to `shiftwidth` at the
   beginning of the line, whereas `tabstop` and `softtabstop` are used
   elsewhere.

For more info run `:help 'OPTION'` in Vim, where `OPTION` is any option from
above.

### examples

Small hard tabs (html):

	:set noexpandtab
	:set shiftwidth=2
	:set softtabstop=2

Soft tabs (python):

	:set expandtab
	:set shiftwidth=4
	:set softtabstop=4

Normal hard tabs (C):

	:set noexpandtab
	:set shiftwidth=8
	:set tabstop=8

To automatically change the options for indents per file type you could put
lines such as these in your `.vimrc` file:

	autocmd FileType html setlocal shiftwidth=2 tabstop=2
	autocmd FileType python setlocal expandtab shiftwidth=4 softtabstop=4
	autocmd FileType c setlocal noexpandtab shiftwidth=8 softtabstop=8

### polyglot plugin

![languages](/assets/img/posts/vim-indenting/prog-languages.png)

Unless you want to add a new line to your `.vimrc` every time you want to edit
a new type of file, I would recommend installing the Vim plugin
[vim-polyglot][2]. Not only does this plugin provide syntax highlighting for
hundreds of languages but it also provides default indentation settings for
each as well. While these defaults are useful, it can also be necessary to
manually control each setting. For example if you want to change the defaults
to your own preference or if a file is already formatted a specific way
polyglot will not change it, so you will have to.

[1]: https://github.com/nathanaelkane/vim-indent-guides
[2]: https://github.com/sheerun/vim-polyglot
