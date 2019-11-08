all: data/larry-wall.dat data/perl-folklore.dat data/perl-japhs.dat data/perl-poetry.dat

%.dat : %
	@strfile $< $@
