# JAPH - Just Another Perl Hacker

From [rochester.pm.org](https://web.archive.org/web/20130516074850/http://rochester.pm.org/talks/japh_discussion.txt) 

## What is a JAPH?
A JAPH is a little Perl script that prints out the phrase "Just another perl hacker".  

Yes, it's pretty useless, but the goal is to figure out the most obfuscated and clever way to do this, and
fit it all into about 4 lines (or less) of code.

Many Perl gurus use their JAPH as part of their .signature file.  

Because of this, the creation of a JAPH is almost like a rite of passage.

## Criteria
Unlike most other programs, the goal of a JAPH is to be clever,
hard to figure out, and as round about as possible in reaching
the goal.  

The more time it takes to figure out what it's doing,the cooler it is.

## My Goals
My goals in designing my JAPH were:
- It had to look nice, being delimited with a line on top and a line on the bottom
- It would not be more than 4 lines, as I wanted to use it as my signature, and a .sig over 4 lines is considered rude.
- It of course had to print out "Just another Perl hacker"

That's really it.  

As I tackled these goals, I realized that I
could make the top and bottom lines part of my data, so I wouldn't
have to squeeze it all in to 2 lines.  

This worked out very nicely, and wound up producing what I think is an interesting piece of code.

## Concept
The concept behind the program is this:  The string "Just another
Perl hacker" contains characters that have corresponding ordinal
values.  

By then creating a string of each ordinal value, and
substituting a special character for each of those values, you can
construct a "pretty" line of characters that, when decoded, will
contain the message that will be printed.

-------------------------------------

## My JAPH:
```
$_=",.,,,.,,.,,.,,,,..,,,,,,,,.,,,,,,,,,,,,,.,,,,,,,,,.,,,,,,,..,..,,.,,,,,
   ,,,,";s/\s//gs;tr/,./05/;@a=split(//);$_=<DATA>;tr/~`'"^/0-4/;map{$o
   .=$a[$i]+$_;$i++}split(//);@a=$o=~m!...!g;map{print chr}@a; __DATA__
~'^``'``~```~"'~^'``~```````~^`~```^~"'~"~`~```^`~"~"'`~^~^'~^^`~'`~```^~`~
```

-------------------------------------

## JAPH Encoder:
```
#!/usr/local/bin/perl

# encode the string so that the decoder program will be able to read it.
#    There's probably lots of better ways to do this, but it's quick
#    and dirty

	# Set the string we want to encode
$plainstr = "Just another Perl hacker\n";
	
	# This is also an experiment in using the map() function
	# This is basically a for() loop that looks like this:
	#    foreach $_ ( split(//, $plainstr) ) {
	#        if( ord($_) < 100 ) {
	#	     $n .= 0 . ord($_);
	#	 } else {
	#	     $n .= ord($_);
	#	 }
	# 
	# Here we create a string containing the ordinal values of
	# each character in the string.
	# We need to ensure that every character always has 3 digits
	# associated with it, because we will not be using any
	# deliminers in the data.  Basically a fixed length field
map {$n .= (ord($_) < 100 ) ? '0'. ord($_) : ord($_);} split(//, $plainstr);


	# now that we have a string of numbers, we can start
	# associating them with characters
@a =  split(//, $n);

	# for each number in the string we just made, convert it to a
	# nicer looking character.  In order to get a nicer looking
	# string of characters when we're done, we need to split things
	# up into 2 groups.  One group of numbers that have the value of
	# 5 or above, and one group for below 5.
	#
	# here we construct 2 strings, one that keeps track of which
	# group each number is in.  I have chosen to use comma and dot
	# for this purpose.  
	# The second string is a modification of the one we created
	# above (in $n), except now there are no numbers in it with
	# values greater than 4.  We leave this string in $m.
for $e ( @a ) {
    if( $e < 5 ) {
	$red .= ',';
	$m .= $e;
    } else {
	$red .= '.';
	$m .= $e - 5;
    }
}

	# now we have 1 string, just have to create the other.  This
	# is now simple by using the tr/// operator.
$m =~ tr/0-4/~`'"^/;


	# print the whole japh out, with the data and code all put
	# together.
print '$_="';
print $red, '";', "\n";
print<<'EOC';
s/\s//gs;tr/,./05/;@a=split(//);$_=<DATA>;tr/~`'"^/0-4/;map{$o
.=$a[$i]+$_;$i++}split(//);@a=$o=~m!...!g;map{print chr}@a; __DATA__
EOC
print $m, "\n";
```

-------------------------------------

## My JAPH, with comments:

```
# japh_details.txt

	# this is top half of the data.  This string tracks which of
	# the corresponding elements below are valued 5 or higher
	# It is assigned to $_ to reduce the code size and make things
	# easier below.
$_=",.,,,.,,.,,.,,,,..,,,,,,,,.,,,,,,,,,,,,,.,,,,,,,,,.,,,,,,,..,..,,.,,,,,,,,,";

	# We need to remove any whitespace in the upper string.  This
	# allows me to put \n's in the data to make it wrap correctly
   s/\s//gs;
	
	# now, use tr/// to convert each character in the upper string
	# to it's numeric value, 0 or 5.
   tr/,./05/;

	# split the upper string into individual numbers so we can use
	# each value by itself.
   @a=split(//);

	# we are done processing the upper string, now get the lower
	# one, using Perl's built in <DATA> file handle
   $_=<DATA>;

	# convert the lower string into it's corresponding numeric
	# values
   tr/~`'"^/0-4/;
 
	# foreach $_ ( split(//) ) {
	#    $o .= $a[$i]+$_;
	#    $i++;
	# }
	#
	# Do most of the work here.  Take each numerical value in $_
	# (now containing the lower string), and add it to its
	# corresponding value in the array @a, created above.  Append
	# this final value to the string $o.
   map{$o.=$a[$i]+$_;$i++}split(//);

	# We now have all the data put back together, now to convert
	# it into letters.

	# First, grab each group of 3 numbers and store them in their
	# own array value
   @a=$o=~m!...!g;

	# foreach $_ ( @a ) {
	#    print chr($_);
	# }
	# Now, print out each element of @a, first converting it back
	# to a character value
   map{print chr}@a;

	# this just puts data into the <DATA> file handle mentioned
	# above
   __DATA__
~'^``'``~```~"'~^'``~```````~^`~```^~"'~"~`~```^`~"~"'`~^~^'~^^`~'`~```^~`~
```
