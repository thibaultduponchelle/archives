---
layout: text
title: "Webserver" 
permalink: /learn/example/static_server
---


These code examples should not be used for production webservers!

## Plackup 

Install Plackup with :

```
cpanm Plack
```

## Long version

Save the following into a file called app.psgi

```
#!/usr/bin/perl
use strict;
use warnings;

# Serve static files from document root with a directory index
# app.psgi
use Plack::App::Directory;
my $app = Plack::App::Directory->new({ 
                root => "/path/to/htdocs" 
            })->to_app;

```

Then run :
```
$ plackup
Accepting connections at http://0:5000/
```

## Short version 

Magic oneliner: 

```
plackup -MPlack::App::Directory -e 'Plack::App::Directory->new(root=>".");' -p 8000
```

## HTTP::Server::Brick

Install **HTTP::Server::Brick** with:

```
cpanm HTTP::Server::Brick
```

Then start webserver with:
```
$ perl -MHTTP::Server::Brick -e '$s=HTTP::Server::Brick->new(port=>8000); $s->mount("/"=>{path=>"."}); $s->start'
```

## Mojolicious

Install **Mojolicious::Lite** with:

```
cpanm Mojolicious::Lite
```

Then you can start a webserver with:
```
$ perl -MMojolicious::Lite -MCwd -e 'app->static->paths->[0]=getcwd; app->start' daemon -l http://*:8000
```
