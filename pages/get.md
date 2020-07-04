---
layout: default
title: "Install"
permalink: /get
---

{% include header.html 
   title="Install" 
%}

{% include sectiontext.html 
   title="Perl runs on over 100 platforms!"
   color="blue"
   content='This is true, Perl is **UBIQUITOUS!**

There are good likehood that Perl is already installed on your system, and therefore you\'re not concerned by what is written on this page.

This page is for you if :
* You need to install a different version than what is already installed on your OS
* You need to install Perl on a OS that does not have it by default (e.g. Windows...)

We recommend that you always run the latest stable version. If you\'re running a version older than 5.8.3, you may find that the latest version of CPAN modules will not work.'
%}

{% include section2.html
   title="Unix"
   color="blue"
   description="Running Linux, Solaris, AIX, HPUX, or any other UNIX-like system?"
   left-title="Binaries"
   left-content=':heavy_check_mark: Already Installed

You probably already have perl installed. Type `perl -v` on a command line to find out which version.

ActiveState Perl has binary distributions of Perl for GNU/Linux.

See [ActivePerl](https://www.activestate.com/products/perl/downloads/)'


   right-title="Sources"
   right-content='Look at *"perl installers"* to help compile and manage Perl:
* [Perlbrew](https://perlbrew.pl/) - Installer written in perl
* [plenv](https://github.com/tokuhirom/plenv) - Another installer written in Perl
* [perl-install](https://github.com/skaji/perl-install) - Installer that does not require Perl

Or download the Perl source code.'

   right-button-text="Download latest development source code"
   right-button-link="https://www.cpan.org/src/"
%}

{% include section2.html
   title="Mac OS X"
   color="white"
   description="Mac OS X enthusiast ?"
   left-title="Binaries"
   left-content=':heavy_check_mark: Already Installed

You probably already have perl installed. Type `perl -v` on a command line to find out which version.

ActiveState Perl has binary distributions of Perl for Mac OS X.

See [ActivePerl](https://www.activestate.com/products/perl/downloads/)'


   right-title="Sources"
   right-content='Look at *"perl installers"* to help compile and manage Perl:
* [perl-install](https://github.com/skaji/perl-install) - Installer that does not require Perl
* [Perlbrew](https://perlbrew.pl/) - Installer written in perl
* [plenv](https://github.com/tokuhirom/plenv) - Another installer written in Perl

Or download the Perl source code.'

   right-button-text="Download latest development source code"
   right-button-link="https://www.cpan.org/src/"
%}

{% include section2.html
   title="Windows"
   color="blue"
   description="Windows does not have Perl installed by default."
   left-title="ActivePerl"
   left-content='**ActivePerl** - [ActiveState](https://www.activestate.com/) offers both a free community version and a commercially supported binary distribution of Perl for Win32 and Perl for Win64.'
   left-button-text='Donwload ActivePerl'
   left-button-link='https://www.activestate.com/products/perl/downloads/'

   right-title="StrawberryPerl"
   right-content='**StrawberryPerl** - A 100% Open Source Perl for Windows that is exactly the same as Perl everywhere else; this includes using modules from CPAN, without the need for binary packages.'
   right-button-text='Download StrawberryPerl'
   right-button-link='http://strawberryperl.com/'

%}
