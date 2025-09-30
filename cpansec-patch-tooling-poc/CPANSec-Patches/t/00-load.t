#!perl
use 5.006;
use strict;
use warnings;
use Test::More;

plan tests => 1;

BEGIN {
    use_ok( 'CPANSec::Patches' ) || print "Bail out!\n";
}

diag( "Testing CPANSec::Patches $CPANSec::Patches::VERSION, Perl $], $^X" );
