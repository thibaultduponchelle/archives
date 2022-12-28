# Some JAPHs from [Luke Poskitt](https://github.com/ltp)

Taken from [ltp japh repo](https://github.com/ltp/japh)

## japh.pl
```
@a=(
	[a6X1s3,w3R2t5,l1J5t4,u1G1b4R1,y3r4t7],
	[v6A1i3,p2S1l2O1i4,u1D1i4C1a3,g1W1o4O15,g9s5d2,b6n6],
	[d6L1c3,k1N1v4O1y3,v1V1y4R1z3,q1D1h4F1f1,h6j6c6,a2s3q6],	
	[q6T1t3,q1X6p3,i1E5l4,n1M6n4o1o8,i1h2k1k1],
	[b1N1b4B1u3,o1O1o4O1o3,d1S1n4m1f3,u1J1s4T1p12,y0e0W0w1],
	[x2Z4v4,j1S1z4I1t3,p1O1f8,k1J1d4V1v8,j1h1k1]
);

for($i=0;$i<@a;$i++){
	$o.="\n";
	for($j=0;$j<=$#{$a[$i]};$j++){
		&w($a[$i][$j])}}
		$o.="\n";

		x($a[2][8]),				x($a[1][8]),		x($a[8][1]),			x($a[9][3]),
		x($a[7][3]),			x($a[2][9]),	x($a[8][3]),	x($a[0][0]),			x($a[1][3]),
		x($a[4][3]),			x($a[3][3]),	x($a[0][7]),	x($a[4][4]),			x($a[0][4]),
		x($a[5][3]),			x($a[3][3]),	x($a[2][3]),	x($a[3][4]),			x($a[2][4]),
		x($a[0][8]),x($a[1][4]),	x($a[3][4]),	x($a[2][4]),	x($a[1][5]),x($a[1][7]),
		x($a[2][3]),x($a[4][4]),		x($a[5][4]),		x($a[2][5]),x($a[3][4]),	x($a[2][4]);

sub w{$_=reverse $_[0];while(($w=chop)&&($x=chop)){$w=~y/a-z/ /||$w=~y/A-Z/#/;$o.="$w"x$x}}
sub x{@x=(" ",a..z);$o.=$x[(eval(join("+",(split/\D/,$_[0]))))]}print $o,"\n"
``` 
