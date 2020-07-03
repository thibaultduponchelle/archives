---
layout: text
title: "Modules" 
color: "lblue"
permalink: /learn/modules
---


## What is a Perl module?

Perl [modules](https://perldoc.pl/perlmod.html) are a set of related functions packaged into a library file. 

They are specifically designed to be reusable by other modules or programs (then "YOU" :smiley:). 

There are a lot of modules (around 200 000 currently) and for basically everything. They are ready for you to use on the [Comprehensive Perl Archive Network](https://www.cpan.org/). Perl have smart installers ([cpan](https://metacpan.org/pod/distribution/CPAN/scripts/cpan), [cpanm](https://metacpan.org/pod/App::cpanminus), [cpm](https://metacpan.org/pod/App::cpm)) to make the retrieval and installation easy.

<a class="button button-secondary" href="https://cpan.org/">CPAN portal</a>

Most modules are written in Perl (they are "pure-perl"). Some use [XS](https://perldoc.pl/perlxs.html) or [FFI](https://metacpan.org/pod/FFI) to interface to another programming language (often [C](https://en.wikipedia.org/wiki/C_(programming_language))) and can require some tooling to build like a [C compiler](https://en.wikipedia.org/wiki/Compiler).

If you followed the [installing](/learn/installing) instructions you already have one. 

Modules may have dependencies on other modules (almost always on [CPAN](http://www.cpan.org/)) and cannot be installed without them (or without a specific version of them). Many modules on CPAN now require a recent version of Perl.

   
## Where can I find modules?

[MetaCPAN](https://metacpan.org) is the best friend of every Perl programmer. [MetaCPAN](https://metacpan.org) lets you search through more than 194,000 modules on CPAN. :+1:

<a class="button button-secondary" href="https://metacpan.org/">MetaCPAN</a>

   
## Which modules should I use?

[MetaCPAN](https://metacpan.org) has user ratings, also have a look at [Task::Kensho](https://metacpan.org/release/Task-Kensho/). 

The [examples](/learn/examples) section and [FAQ](/learn/faq) also have some recommendations, but you could also ask the Perl community.

   
## How do I install a module?

If you haven't already installed **cpanm**, do that first:

```
cpan App::cpanminus
```

Or if you're one a GNU/Linux machine :

```
curl -L https://cpanmin.us | perl - --sudo App::cpanminus
```

Then to install any module from CPAN

```
cpanm Module::Name
```


