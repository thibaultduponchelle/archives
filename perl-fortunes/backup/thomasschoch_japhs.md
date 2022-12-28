# "Just another Perl Hacker"

Taken from [Thomas Schoch website](http://retas.de/thomas/computer/programs/useless/index.html)

A "JAPH" is a small Perl program that prints
"Just another Perl Hacker".

The code should be somehow or other obscure,
illegible, obfuscated or formatted funnily.

My favourite web resources on JAPHs are:

*  Abigail's brilliant "slides" on JAPHs and
   other weird stuff. (Abigail is IMO one of
   the greatest masters of JAPH.)

*  An Obfuscated Perl Contest Entry by Mark
   Jason Dominus with detailed explanation.

*  A CPAN archive of 224 JAPHs.

My 5 JAPHs are just experiments. Needless to
say, they do not approach the quality of the
JAPHs from the sources above.

## JAPH 1
```
$_=q^#ba':;Dy{rw}<+2~|}+?

+<jwx}@n{<Yn{u<Qjltn{ew+'

;%+.+i0r3>rd]#&<-9+ge^,y;

#ba@]!0>mk%32iv[f^*!7z?<;

$_=q(Thomas Schoch 2005);

;;;;;;; eval,eval ;;;;;;;
```
This Perl program prints
"Just another Perl Hacker".

## JAPH 2
```
/[+-]/&&eval"\$/$_$_"||/\x2e/&&print chr$/for qw!
=================================================
+ + + + + + + + + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + + + + + + + .
+ + + + + + + + + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + . - - . + . -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - . + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + + + + + + + .
+ + + + + + + + + + + + + . + . + + + + + . - - -
- - - - - - - - - . - - - . + + + + + + + + + + +
+ + . - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - . + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + + + + + + + +
+ + + + + + + + + . + + + + + + + + + + + + + + +
+ + + + + + . + + + + + + + + + + + + + . - - - -
- - . - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - . + + + + + + + + + + + + + + + + + + + +
+ + + + + + + + + + + + + + + + + + + + . + + + +
+ + + + + + + + + + + + + + + + + + + + + . + + .
+ + + + + + + + . - - - - - - . + + + + + + + + +
+ + + + . - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - + + + + + + + + - - - - - - - -
=================================================
A bilingual JAPH. Valid code in Perl & brainf***!
```
 This program prints
"Just another Perl Hacker".
(More about JAPHs.)

It is bilingual and can be
executed with Perl or Brainf***.
([More](http://www.iwriteiam.nl/Ha_BF.html) about Brainf***)

## JAPH 3
```
        [60],$_
        =do{ $_
        =q{}.$_
        [40].$_
        { a}.$_
        {w }.$_
        [38].$_
        { t}.$_
        {r }.$_
        [18].$_
        { e}.$_
        [14].$_
        {i }.$_
        [ 9].$_
        [22].$_
        [14].$_
        {i }.$_
        { d}.$_
        [9 ].$_
        { e}.$_
        [38].$_
        {k }.$_
        [36].$_
        [14].$_
        { i},s
  ^H^h^^y^p^P^d^print
    "\x4au$_\n"}if%
      _=@_=split//
       =>reverse
        q>stack
          >.q
           ;

print "Hello, world!\n";
```
This Perl program prints
"Just another Perl Hacker".

## JAPH 4
```
eval 's=Shell'; eval "echo 'Just another $s Hacker\
'; exit" && 1 for $s = Perl; sub echo { print @_ };
```

This is a bilingual JAPH.

It can be executed with Perl (it then
prints "Just another Perl Hacker") or
with Unix shells like sh, bash or ksh
(printing "Just another Shell Hacker").

 A pure Kornshell version is here:

```
eval '_=Kornshell'; eval "print 'Just another $_ Hacker\
'; exit" &&1 for qw{ "use Perl or Kornshell or die" }[1]
```

## JAPH 5
```
%==(q<=>=>q=+==>q->-=>q=-=)=>$ _=
q-=4a=2b>2=1>54=41=d=1=5>c>3=d>52
=30=15=d>6>4c=28=19=2=8>6=d>68-=>
$^=q=print(chr($-==>=>s<(.)(\w+)>
[$^$={$1}=hex(qq=$2=)))=>]g=>eval

This Perl program prints
"Just another Perl Hacker".
```
