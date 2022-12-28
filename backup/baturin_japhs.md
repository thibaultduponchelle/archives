# JAPHs and other fun with obfuscation

        Christmas tree 2.0
        Fermat numbers
        Email is the key
        Three primes
        Seven points of Python
        Perl is in my heart (or vice versa)
        Glider
        Christmas tree

I like recreational obfuscation. Not that I'm really good at it, but here are some examples of what I wrote during inspiration attacks.

## Christmas tree 2.0
```
#!/usr/bin/env python3
# Happy winter holidays!
m = ['\0', '\0', '\\', '/', '|', '\n', '*', ' ']
n=1427204133903092885193970416731911941327299733
Y =  lambda f : lambda x, y : f( Y( f ) ) (x, y)
s = Y( lambda f : lambda  x, y : y if not x else
f(x >> 3, y + m[x & 7]))(n, "") ; print(s[::-1])
```
Should print an ASCII christmas tree:

```
    *    
   /|\   
  //|\\  
 ///|\\\ 
////|\\\\
```
...eight years later. Another take on the custom ASCII art encoding theme, this time every character is encoded by three bits. Since we only need six characters, while three bits can encode 23=8 distinct values, two unused values are mapped to the null character. A loop would be too obvious, so I used recursion with accumulator, implemented using the Y combinator instead of a direct recursive definition.

Date: December 2018

## Fermat numbers
```
#!/usr/bin/env perl
s3:n(q{Just });s5:n("another ");s17:n(q{Perl });s257:n("hacker");
s65537:n("\n");$p=1;sub n{$p++; $w=2**(2**$p)+1;print@_;goto"s$w"
unless grep/^1$/,map{1 if $w%$_==0}(2..int(sqrt($w)));exit;};n;1;
```

Should print “Just another Perl hacker”. Labels contain Fermat numbers, the n() subroutine generates a Fermat number and jumps to its label as long as the next number after it is prime. Since only the first five are prime, it terminates as expected.

The primality test is awfully inefficient but for very small numbers it doesn't matter.

Date: some 2013 I guess.
## Email is the key
```
#!/usr/bin/env perl
@a=split(//, "daniil @ baturin  . org" ); # Daniil Baturin
@b=split(//,q/Px%!+o0Q6lh*7dp$.@8#t!nr/);while($i<24){$_.=
chr((ord(@b[$i])-ord(@a[$i])+62)%94+32);$i++};print"$_\n"#
```
Should print traditional “Just another Perl hacker”.

The idea was to make the email address an essential part of the program that cannot be modified without understanding.

So the email address was used as a key for the running key variant (that is, where the key length is equal to the plaintext length) of the Vigenere cipher that uses the entire printable ASCII range as its alphabet.

Date: late 2012.
## Three primes
```
#!/usr/bin/env perl
use bigint;$i=
8311 * 11506699 * 5456897772732206286791603681159406921396401
;while($i){$_.=chr($i&0x7f);$i>>=7;}print
```
Should print traditional “Just another Perl hacker”.

Simply obtains character codes from the string converted to number and then factorized.

Date: September 2012

## Seven points of Python
```
#!/usr/bin/env python3
from math import log, exp
print ("".join(map(lambda
x:chr((int((round((29*exp
((log(x)*6))/720-(283*exp
(log(x)*5))/240+(1657*exp
(log(x)*4))/144-(2209*exp
(log(x)*3))/48+(21403*exp
(log(x)*2))/360+(231*x)/5
+10.4)))))),range(1,7))))
```

Should print “Python”. Last I checked, it works with either Python 2.7 or Python 3.

The function that produces the ASCII codes of the “Python\n” string was constructed with Lagrange polynomial interpolation.

Date: October 2012

## Perl is in my heart (or vice versa)
```
#!/usr/bin/env perl
use bigint;$h=0x3eff8fe0f0047c5fd;
while($h){$_.=$h&1?' ':'*';$h/=2};
$_=join("\n",$_=~/.{11}/g);print;1
```
Should print an ASCII heart:
```
 *       * 
***     ***
 ********* 
   *****   
    ***    
     *     
```

Obviously, written for the Valentine's day. Specifically, for a Valentine's day contest my ISP once held where users submitted their postcards, videos, and the like. To their credit, they ran it in some test VM and posted a screenshot of the terminal.

Spaces are encoded with zeroes and stars with 1's, packed into a single hexadecimal number.

Date: February 2012 perhaps?

## Glider
```
#!/usr/bin/env python
glider = [[  0, 1, 0  ],
          [  0, 0, 1  ],
          [  1, 1, 1  ]]

hacker = [[ 300, 300, 175 ],
          [ 390, 270, 255 ],
          [ 400, 265, 260 ],
          [ 365, 325, 260 ],
          [ 350, 345, 225 ],
          [ 400, 320, 265 ]]

from functools import reduce; nsqr = lambda x: sp(x, x)
sp=lambda u,v: reduce(lambda x,y:x+y,list(map(lambda z:z[0]*z[1],zip(u,v))),0)
transform = lambda m,v:list(map(lambda mr: sp(mr,v),m))
print("".join(map(chr,map(lambda x:nsqr(transform(glider,x))//10**4,hacker))))
```

Should print the word “Hacker”.

I generally support Eric Raymond's idea to use the glider as a technology neutral hacker subculture emblem (even if I don't agree with a lot of his opinions).

Here the glider is used as a linear transformation matrix that is applied to a bunch of vectors constructed so that the squares of their euclidian norms are equal to the ASCII character codes of the word “Hacker” (rather, their first two or three decimal digits are). The original version used floating point numbers, but I multiplied everything by 100 to avoid it and use only precise and portable integer arithmetics. Works in both Python 3 and Python 2.7.

This is an updated version that uses Python and integer arithmetics.

Date: November 2012, Python rewrite in December 2018

## Christmas tree

```
#!/usr/bin/perl
$_=16;$j=1;$r.=chr($_*2)x($_+1)."*"."\n";for
($i=$_;$i>$_>>1;$i--){;$r.=chr(2*$_)x$i.chr(
$_*3-1)x$j.chr($_*($_>>1)-sqrt($_)).chr($_*6
-sqrt($_))x$j.chr($_-6);$j++}$l=@a;print($r)
```
Early attempt, written in the late 2010 for the winter holidays. 
