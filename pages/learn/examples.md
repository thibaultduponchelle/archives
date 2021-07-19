---
layout: text
title: "Examples"
permalink: /learn/examples
---

## Mails
* [Sending an email](/perldot/learn/examples#email)
* [Validate an email](/perldot/learn/examples#validate-email)

## Files
* [List content of a directory](/perldot/learn/examples#directory-list)
* [Read/Write to file](/perldot/learn/examples#read-and-write-file)
* [Read a spreadsheet](/perldot/learn/examples#spreadsheet)
* [Processing configuration files](/perldot/learn/examples#configuration-files)

## Various
* [Setting up a local static web server](/perldot/learn/examples#static-webserver)
* [Resolving DNS](/perldot/learn/examples#dns)

--------

# Examples

## Email

Perl is the perfect tool for dealing with emails. 

Here is a example code to send an email:
```
#!/usr/bin/perl
use strict;
use warnings;

# first, create your message
use Email::MIME;
my $message = Email::MIME->create(
  header_str => [
    From    => 'you@example.com',
    To      => 'friend@example.com',
    Subject => 'Happy birthday!',
  ],
  attributes => {
    encoding => 'quoted-printable',
    charset  => 'ISO-8859-1',
  },
  body_str => "Happy birthday to you!\n",
);

# send the message
use Email::Sender::Simple qw(sendmail);
sendmail($message);
```

## Validate email 

Email validation is [not a trivial task](https://emailregex.com/), use a module like the following example: 
```
#!/usr/bin/perl
use strict;
use warnings;

use Email::Valid;

my $email_address = 'a.n@example.com';

unless( Email::Valid->address($email_address) ) {
    print "Sorry, that email address is not valid!";
}
```

## Directory list

List the content of a directory:
```
#!/usr/bin/perl
use strict;
use warnings;

use Path::Tiny;

my $dir = path('foo','bar'); # foo/bar

# Iterate over the content of foo/bar
my $iter = $dir->iterator;
while (my $file = $iter->()) {
    
    # See if it is a directory and skip
    next if $file->is_dir();
    
    # Print out the file name and path
    print "$file\n";
}
```

## Read and write file

### Writing to a file

Write to a file `/tmp/file.txt`:
```
#!/usr/bin/perl
use strict;
use warnings;

use Path::Tiny;
use autodie; # die if problem reading or writing a file

my $dir = path("/tmp"); # /tmp

my $file = $dir->child("file.txt"); # /tmp/file.txt

# Get a file_handle (IO::File object) you can write to
# with a UTF-8 encoding layer
my $file_handle = $file->openw_utf8();

my @list = ('a', 'list', 'of', 'lines');

foreach my $line ( @list ) {
    # Add the line to the file
    $file_handle->print($line . "\n");
}
```

### Appending to a file

```
# As above but use opena_utf8() instead of openw_utf8()
my $file_handle = $file->opena_utf8();
```

### Reading a file

Read file `/tmp/file.txt`:
```
#!/usr/bin/perl
use strict;
use warnings;

use Path::Tiny;
use autodie; # die if problem reading or writing a file

my $dir = path("/tmp"); # /tmp

my $file = $dir->child("file.txt");

# Read in the entire contents of a file
my $content = $file->slurp_utf8();

# openr_utf8() returns an IO::File object to read from
# with a UTF-8 decoding layer
my $file_handle = $file->openr_utf8();

# Read in line at a time
while( my $line = $file_handle->getline() ) {
        print $line;
}
```

**Path::Tiny** makes working with directories and files clean and easy to do. 

Use **path()** to create a **Path::Tiny** object for any file path you want to operate on, but remember if you are calling other Perl modules you may need to convert the object to a string using 'stringify':
```
$file->stringify();
$dir->stringify();
```

**autodie** forces many functions to die with a useful error message (instead of returning undef) if they fail. This makes for cleaner code. 

To check for and catch errors use **Try::Tiny**.

## Spreadsheet

Use **Spreadsheet::Read** to read a spreadsheet:
```
#!/usr/bin/perl
use strict;
use warnings;

use Spreadsheet::Read;

my $workbook = ReadData ("test.xls");
print $workbook->[1]{A3} . "\n";
```

## Configuration files

Load a configuration, whatever the format!
```
#!/usr/bin/perl
use strict;
use warnings;

use Config::Any;

my @files = (
        'path/to/config_file.json',
        'path/to/config.pl',
        'path/to/config.xml'
);

my $config = Config::Any->load_files( { files => \@files } );
```

## Static Webserver

Quick (and dirty) werbservers! :grin:

These code examples should not be used for production webservers!

### Plackup 

Install Plackup with :

```
cpanm Plack
```

#### Long version

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

#### Short version 

Magic oneliner: 

```
plackup -MPlack::App::Directory -e 'Plack::App::Directory->new(root=>".");' -p 8000
```

### HTTP::Server::Brick

Install **HTTP::Server::Brick** with:

```
cpanm HTTP::Server::Brick
```

Then start webserver with:
```
$ perl -MHTTP::Server::Brick -e '$s=HTTP::Server::Brick->new(port=>8000); $s->mount("/"=>{path=>"."}); $s->start'
```

### Mojolicious

Install **Mojolicious::Lite** with:

```
cpanm Mojolicious::Lite
```

Then you can start a webserver with:
```
$ perl -MMojolicious::Lite -MCwd -e 'app->static->paths->[0]=getcwd; app->start' daemon -l http://*:8000
```

## DNS

**"DNS"** stands for [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System), it is an important piece that makes the web what we know today. 

You can have more details/examples about Perl and DNS in the book [Perl for System Administration](https://www.oreilly.com/library/view/perl-for-system/1565926099/).

```
#!/usr/bin/perl
use strict;
use warnings;

use Net::DNS::Resolver;

my $hostname = 'perl.org';
my $res = Net::DNS::Resolver->new(
  nameservers => [qw(10.5.0.1)],
);

my $query = $res->search($hostname);

if ($query) {
  foreach my $rr ($query->answer) {
    next unless $rr->type eq "A";
    say "Found an A record: ".$rr->address;
  }
}
```
