#!/usr/bin/env perl

# Quick and dirty
# Use like this :
# cat aliens | ./gen.pl > README.md

my $startyml = << "END";
on:
  schedule:
    - cron: 0 0 * * *

jobs:
  perl:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout\@v2
      - name: perl -V
        run: perl -V
END

my $endyml = << "END";
      - name: Install Dependencies
        run: curl -sL https://git.io/cpm | perl - install --show-build-log-on-failure 
END


my @badges = ();


while(<>) {
	my $line = $_;
	chomp $line;
	my ($full_alien, @debs) = split(" ", $line);
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
	print $fh $startyml;
	if(@debs) {
		print $fh "      - name: Install non alienazed dependencies\n";
		print $fh "        run: sudo apt-get install @debs\n";
	}
	chomp $endyml;
	print $fh $endyml;
	print $fh "$full_alien\n";
	close $fh;
}

print "| :alien: | :alien: | :alien: | :alien: | :alien: |\n";
print "|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |\n";

my $cells = 0;
foreach my $b (@badges) {
	$cells ++;
	print "| [![$b](https://github.com/thibaultduponchelle/aliens-ci/workflows/$b/badge.svg)](https://github.com/thibaultduponchelle/aliens-ci/actions?query=workflow%3A$b) ";
	if($cells >= 5) { 
		$cells = 0;
		print "\n";
	}
}

print " |\n\n";
print "You can find details about failing modules on the [problems page](https://github.com/thibaultduponchelle/aliens-ci/blob/master/problems.md)\n";
