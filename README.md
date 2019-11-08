# :cookie: perl-fortunes
A Perl collection of quotes to be used by crazy people as a fortune database 

## :hammer: Setup
```
make
sudo cp data/* /usr/share/games/fortunes
```

...if your fortunes are located in `/usr/share/games/fortunes`, you can get this place from `fortune` like this : 
```
fortune -f 2>&1 | head -n 1 | cut -f2 -d" "
```

## :warning: Warning :warning: 
Could contains Perl code and Larry Wall quotes ! :joy:

## :zzz: Conclusion
Happy Perl hacking ! :kissing_closed_eyes:
