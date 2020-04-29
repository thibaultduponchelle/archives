#!/usr/bin/env perl

# Quick and dirty
# Use like this :
# cat aliens | ./gen.pl > README.md

my $yml = << "END";
on:
  push:
    branches:
      - '*'
    tags-ignore:
      - '*'
  pull_request:
  schedule:
    - cron: 0 0 * * *

jobs:
  perl:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout\@v2
      - name: perl -V
        run: perl -V
      - name: Install Dependencies
        run: curl -sL https://git.io/cpm | perl - install --show-build-log-on-failure 
END


my @badges = ();


while(<>) {
	my $full_alien = $_;
	chomp $full_alien;
	my ($trash, @all) = split("::", $full_alien);
	my $alien = join("-", @all);
	#print "Alien::$alien is $full_alien\n";
	
	chomp $alien;
	push @badges, $alien;
	#print $alien ."\n";
	#next;
	
	my $filename = ".github/workflows/$alien.yml";
	open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
	print $fh "name : $alien\n\n";
	chomp $yml;
	print $fh $yml;
	print $fh "$full_alien\n";
	close $fh;
}

print "| :alien: | :alien: | :alien: | :alien: | :alien: |\n";
print "|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |\n";

my $cells = 0;
foreach my $b (@badges) {
	$cells ++;
	print "| [![$b](https://github.com/thibaultduponchelle/aliens-ci/workflows/$b/badge.svg)](https://github.com/thibaultduponchelle/aliens-ci/actions?query=workflow%3A$b) ";
	if($cells > 5) { 
		$cells = 0;
		print "\n";
	}
}

print " |\n"
