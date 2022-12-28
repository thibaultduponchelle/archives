# :speech_balloon: perl-fortunes
A Perl collection of quotes to be used by crazy people as fortune database.

## :hammer: Setup
```
make
sudo cp data/* /usr/share/games/fortunes
```

... if your fortunes are located in `/usr/share/games/fortunes`, you can get this place from `fortune` like this : 
```
fortune -f 2>&1 | head -n 1 | cut -f2 -d" "
```

## :warning: Warning
Could contains Perl code :scream: and Larry Wall quotes :joy:

## :snowman: TODO

* Check if we can pick some new JAPHs from here : https://github.com/Perl/perl5/blob/blead/t/japh/abigail.t
* Poetry...

## :monkey: Conclusion
Happy Perl hacking ! :kissing_closed_eyes:
