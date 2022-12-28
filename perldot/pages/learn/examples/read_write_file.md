---
layout: text
title: "Read/Write" 
permalink: /learn/example/read_write_file
---



## Writing to a file

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

## Appending to a file

```
# As above but use opena_utf8() instead of openw_utf8()
my $file_handle = $file->opena_utf8();
```

## Reading a file
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


