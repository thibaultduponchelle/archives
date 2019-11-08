all: data/larry-wall.dat data/perl-folklore data/perl-japhs data/perl-poetry

%.dat : %
	@strfile $< $@
