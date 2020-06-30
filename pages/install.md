---
layout: default
title: "Install"
permalink: /install
---

{% include header.html 
   title="Install" 
%}

{% include sectiontext.html
  color="white"
  title="How to install"
  content='Install modules with <pre><code>wget https://www.cpan.org/src/5.0/perl-5.32.0.tar.gz
tar -xzf perl-5.32.0.tar.gz
cd perl-5.32.0
./Configure -des -Dprefix=$HOME/localperl
make
make test
make install</code></pre>'
%}






