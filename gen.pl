#!/usr/bin/env perl

# Quick and dirty
# Use like this :
# cat aliens | ./gen.pl > README.md

my $startyml = << "END";
on:
  schedule:
    - cron: 0 12 * * *

jobs:
  perl:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout\@v2
      - name: perl -V
        run: perl -V
END

my $endyml = << "END";
      - name: Install alien
END


my @badges = ();

print "| :alien: | :alien: | :alien: | :alien: | :alien: |\n";
print "|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |\n";
my $cells = 0;

while(<>) {
	my $line = $_;
	chomp $line;
	my ($full_alien, @debs) = split(" ", $line);
	my ($trash, @all) = split("::", $full_alien);
	for my $mode ("cpanm", "cpm") {
		my $alien = join("-", @all);
		#print "Alien::$alien is $full_alien\n";
		my $alienm = "$alien-$mode";
	
		chomp $alien;
		
	
		my $filename = ".github/workflows/$alienm.yml";
		open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
		print $fh "name : $alienm\n\n";
		print $fh $startyml;

		if(@debs) {
			print $fh "      - name: apt-get update\n";
			print $fh "        run: sudo apt-get update\n";
			print $fh "      - name: Install non alienazed dependencies\n";
			print $fh "        run: sudo apt-get install @debs\n";
		}
		print $fh $endyml;
		if($mode eq "cpanm") {
			print $fh "        run: curl -L https://cpanmin.us | perl - --configure-timeout=1920 ";
			print "| [![$alienm](https://github.com/thibaultduponchelle/aliens-ci/workflows/$alienm/badge.svg)](https://github.com/thibaultduponchelle/aliens-ci/actions?query=workflow%3A$alienm) ";
		} elsif($mode eq "cpm") {
			print $fh "        run: curl -sL https://git.io/cpm | perl - install --show-build-log-on-failure --test --configure-timeout=1920 ";
			print "[![$alienm](https://github.com/thibaultduponchelle/aliens-ci/workflows/$alienm/badge.svg)](https://github.com/thibaultduponchelle/aliens-ci/actions?query=workflow%3A$alienm) ";
			$cells ++;
		}

		if($cells >= 5) { 
			$cells = 0;
			print "|\n";
		}
		print $fh "$full_alien\n";
		close $fh;
	}
}

print "|" if($cells);
print "\n\n";
print "You can find details about failing modules on the [problems page](https://github.com/thibaultduponchelle/aliens-ci/blob/master/problems.md)\n";
