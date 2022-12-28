all: data/larry-wall.dat data/perl-folklore.dat data/perl-japhs.dat data/larry-wall-facts.dat

%.dat : %
	@strfile $< $@
