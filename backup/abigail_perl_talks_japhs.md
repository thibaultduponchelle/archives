# JAPHs and other obscure signatures
Abigail

Philadelphia	27 March 2000

New York	18 April 2000

Pittsburg	22 June 2000

Amsterdam	6 February 2001

## History

* Originally, Japhs are "Usenet signatures", small programs that can be put under a Usenet posting, that will print the text Just another Perl Hacker.
* Made popular by Randal Schwartz in early 1990.
* Archive some of the old Japhs is at [https://www.cpan.org/misc/japh](https://www.cpan.org/misc/japh).
* `@a=split(/(\d)/,"4Hacker,2another3Perl1Just");shift(@a);%a=@a;print "@a{1..4}";`

## Rules

* There are no formal rules on what is a JAPH and what isn't.
* But we can derive some de facto rules.
* Short: preferably fit in 4 x 80 characters.
* Prints "Just another Perl Hacker".
* Obscure or surprising syntax. 

## Classification (?)

* Data Hiding.
* Surprising or obscure program flow.
* Looks funny.
* ....
* Non-Japhs. 


## Data Hiding 
```
perl5.004 -wMMath::BigInt -e'$^V=Math::BigInt->new(qq]$^F$^W783$[$%9889$^F47]
.qq]$|88768$^W596577669$%$^W5$^F3364$[$^W$^F$|838747$[8889739$%$|$^F673$%$^W]
.qq]98$^F76777$=56]);$^U=substr($]=>$|=>5)*(q.25..($^W=@^V))=>do{print+chr$^V  
%$^U;$^V/=$^U}while$^V!=$^W'
```

## Obscure flow
```
sub _'_{$_'_=~s/$a/$_/}map{$$_=$Z++}Y,a..z,A..X;*{($_::_=sprintf+q=%X==>"$A$Y".
"$b$r$T$u")=~s~0~O~g;map+_::_,U=>T=>L=>$Z;$_::_}=*_;sub _{print+/.*::(.*)/s}
*_'_=*{chr($b*$e)};*__=*{chr(1<<$e)};
_::_(r(e(k(c(a(H(__(l(r(e(P(__(r(e(h(t(o(n(a(__(t(us(J())))))))))))))))))))))))
```

## Funny 
```
perl -e '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
         / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
         % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %;
         BEGIN {% % = ($ _ = " " => print "Just Another Perl Hacker\n")}'
```

## Russ 
```
#!/usr/bin/perl -- Russ Allbery, Just Another Perl Hacker
$^=q;@!>~|{>krw>yn{u<$$<[~||<Juukn{=,<S~|}<Jwx}qn{<Yn{u<Qjltn{ > 0gFzD gD,
 00Fz, 0,,( 0hF 0g)F/=, 0> "L$/GEIFewe{,$/ 0C$~> "@=,m,|,(e 0.), 01,pnn,y{
rw} >;,$0=q,$,,($_=$^)=~y,$/ C-~><@=\n\r,-~$:-u/ #y,d,s,(\$.),$1,gee,print
```

## Counting lines
```
perl -wlpe '}{*_=*.}{' file
```

## Print numbers
```
perl -wle 'print "Prime" if (1 x shift) !~ /^1?$|^(11+?)\1+$/'
```

## Making a Japh

What you need is an idea (`&%%hole`)


* Start with a hash and a sub that prints "Just another Perl Hacker".
* Nothing obscure yet, except for the unusual name `%_` 

```
%_ = (Just => another => Perl => Hacker);
sub {foreach (sort keys %_) {print "$_ $_{$_} "}};
```

## Last
A Japh that uses...

* Computed `goto`. 
* `eval`.
* `POD`.
* A loop with only unconditional jumps....
* ... but it terminates anyway.
* Self modifying code.
* `strict`.
* `-w`.
* No more than one line.
* No more than 80 characters. 

... does it exist ?

```
perl -Mstrict -we '$_ = "goto F.print chop;\n=rekcaH lreP rehtona tsuJ";F1:eval'
```
