# Aliens problems

## Can't locate Alien/Base/ModuleBuild.pm
- :construction: Alien::Sodium -> [PR](https://github.com/ajgb/alien-sodium/pull/4) from plicease 2016 + waiting adoption from genio
- :construction: Alien::SFML -> [PR](https://github.com/jakeanq/perl-alien-sfml/pull/2) MERGED from plicease 2016 -> need cpan release ([issue](https://github.com/jakeanq/perl-alien-sfml/issues) from me 30 april 2020)
- :construction: Alien::NSS -> Fixed by plicease [PR](https://github.com/0xxon/alien-nss/pull/4) in 2016 -> need cpan release
- :construction: Alien::LibUSBx -> [PR](https://github.com/henrikbrixandersen/Alien-LibUSBx/pull/1) from plicease not merged 2016 -> [PR](https://github.com/henrikbrixandersen/Alien-LibUSBx/pull/3) from me 8 may 2020
- :construction: Alien::libgpg_error -> [PR](https://github.com/salva/p5-Alien-Libgpg_error/pull/1) MERGED from plicease 2016 -> need a CPAN release

### SMUELLER
- :construction: Alien::Lua -> [PR](https://github.com/tsee/p5-Alien-Lua/pull/1) from plicease 2016 -> [commented](https://github.com/tsee/p5-Alien-Lua/pull/1#issuecomment-623946352) 5 may 2020
- :construction: Alien::LuaJIT -> [PR](https://github.com/tsee/p5-Alien-LuaJIT/pull/1) MERGED from plicease 2016 -> need a CPAN release -> New [issue](https://github.com/tsee/p5-Alien-LuaJIT/issues/2) from me 9 may 2020

### Alranel AAR
- :construction: Alien::qd -> [PR](https://github.com/alranel/Alien-qd/pull/2) from plicease MERGED 17 april 2016 -> need only 0.02 release I guess -> commented 30 april 2020 
- :construction: Alien::GEOS  -> [PR](https://github.com/alranel/Alien-GEOS/pull/1) from plicease MERGED 1 march 2016 -> need only 0.02 release I guess -> commented 5 may 2020

### GETTY
- :construction: Alien::mpg123 -> [PR](https://github.com/Getty/p5-alien-mpg123/pull/2) from me 30 april 2020
- :construction: Alien::ffmpeg -> [PR](https://github.com/Getty/p5-alien-ffmpeg/pull/5) from me 30 april 2020
- :construction: Alien::sispmctl -> [PR](https://github.com/Getty/p5-alien-sispmctl/pull/2) from me 30 april 2020
- :construction: Alien::gettext -> [PR](https://github.com/Getty/p5-alien-gettext/pull/2) from me 30 april 2020 and also 
```
perl -e 'use Alien::gettext; print Alien::gettext->libs()'
Could not resolve -lgettextlib-0 at -e line 1.
Could not resolve -lgettextsrc-0 at -e line 1.
Could not resolve -lpreloadable_libintl at -e line 1.
-L/usr/local/share/perl/5.26.1/auto/share/dist/Alien-gettext/lib -lasprintf -lgettextlib -lgettextlib-0 -lgettextpo -lgettextsrc -lgettextsrc-0 -lpreloadable_libintl -ltextstyle
```

### GUGOD 
- :construction: Alien::CImg -> [PR](https://github.com/gugod/Alien-CImg/pull/1) from me 30 april 2020
- :construction: Alien::libsndfile -> [PR](https://github.com/gugod/Alien-libsndfile/pull/1) from me 30 april 2020


## Something else
- :construction: Alien::Plotly::Orca prereq Fil::Copy::Recursive not reproducible locally -> [PR](https://github.com/stphnlyd/perl5-Alien-Plotly-Orca/pull/4) from me
- :construction: Alien::DBD::SQLite::BundledExtensions Can't locate File/ShareDir.pm in @INC not reproduced locally -> Alien/Base/PkgConfig not in @INC -> fix on my [REPO](https://github.com/thibaultduponchelle/Alien-DBD-SQLite-BundledExtensions/commit/e4736bba119ab2ab1653a83670412c11b2515be2)
- :construction: Alien::LibANN -> syntax error at inc/Devel/CheckLib.pm line 164, near "$mm_attr_key qw(LIBS INC)" -> [PR](https://github.com/rogersprint/Alien-LibANN/pull/1) from me
- :construction: Alien::LibBigWig -> fatal error: curl/curl.h: No such file or directory I do not reproduce locally -> [PR](https://github.com/Ensembl/Alien-LibBigWig/pull/3) from me
- :construction: Alien::Protobuf -> Only a system install in upstream -> share is on kiwiroy branch, system seems broken here
- :construction: Alien::SNMP::MAXTC -> compilation error [PR](https://github.com/ollyg/Alien-SNMP-MAXTC/pull/3) from me to upgrade tarball
- :construction: Alien::NSS -> 404 -> [PR](https://github.com/0xxon/alien-nss/pull/6) by me
- :construction: Alien::LibUSBx -> download link issue Could not connect to 'aarnet.dl.sourceforge.net:80': Name or service not known -> [PR](https://github.com/henrikbrixandersen/Alien-LibUSBx/pull/3) from me 8 may 2020
- Alien::XInputSimulator
- Alien::Judy
- :construction: Alien-ActiveMQ -> Can't locate Test/Exception.pm in @INC
- ~Alien::SVN -> need libaprutil1-dev and libsqlite3-dev ?~ 

### PLU 
- :construction: Alien::Gearman -> depends on Alien::Libevent that fails -> removed inc/Devel/ChecLib and use cpan version, no github (removed) -> Need ALien::libuuid -> fixed on my [REPO](https://github.com/thibaultduponchelle/Alien-Gearman)  -> [RT ticket](https://rt.cpan.org/Ticket/Display.html?id=132505) 5 may 2020 -> Johannes Plunien confirmed -> TO ADOPT -> I asked to adopt it
- :construction: Alien::Libevent -> syntax error -> removed inc/Devel/ChecLib and use cpan version, no github (removed) -> Fixed on my [REPO](https://github.com/thibaultduponchelle/Alien-Libevent) -> [RT ticket](https://rt.cpan.org/Ticket/Display.html?id=98058#txn-1896610) 5 may 2020 -> Johannes Plunien confirmed -> TO ADOPT -> I asked to adopt it

### ATHREEF
- :construction: Alien::HIDAPI -> depends on LibUSB that failed
- :construction: Alien::LibUSB -> Can't locate Alien/libudev.pm in @INC (you may need to install the Alien::libudev module) prereq missing -> Alien::libudev is not a prereq because not available on all platforms, I need to investigate. Conditional use, very tricky -> Fixed with [PR](https://github.com/athreef/Alien-LibUSB/pull/3) MERGED from plicease -> need cpan release

### ZMUGHAL
- :construction: Alien::pdf2htmlEX -> depends on Alien::FontForge -> Will be reworked soon by ZMUGHAL
- :construction: Alien::FontForge -> tarball content changed ? -> sh: 0: Can't open ./bootstrap -> Will be reworked soon by ZMUGHAL
- :construction: Alien::WFDB -> [PR](https://github.com/EntropyOrg/p5-Alien-WFDB/pull/8) from me

### KMX
- :construction: Alien::FreeImage ->  error: call of overloaded ‘powf64(int, int)’ is ambiguous -> [PR](https://github.com/kmx/alien-freeimage/pull/1) or [PR](https://github.com/kmx/alien-freeimage/pull/2)

### KIWIROY
- :construction: ALien::MUSCLE ExtUtils::CBuilder version 0.280226 required--this is only version 0.280225 at /home/tduponchelle/.cpanm/work/1588163506.974/Alien-MUSCLE-0.01/alienfile line 8. -> Fixed with [PR](https://github.com/kiwiroy/p5-alien-muscle/pull/2) -> need cpan release
- :construction: Alien::KentSrc pngwrite.c:7:10: fatal error: png.h: No such file or directory -> Alien::PNG not installed but if libpng is installed, Alien::PNG does not install devel ? -> Needs prereq Alien::libuuid ? -> Fixed on lib-deps branch of [kiwiroy repo](https://github.com/kiwiroy/alien-kentsrc/tree/lib-deps)


## Broken 
- Alien::MeCab -> Detected circular dependencies Alien-MeCab-0.97005 -> Alien-MeCab-0.97005
- Alien::DDC::Concordance -> configure: error: could not find pcre_compile(): ensure that LDFLAGS, LIBS are set to link to libpcre -> compilation error with Curl.cpp (??)
- Alien::OpenVcdiff -> compilation error src/vcdecoder_test.cc:33:3: error: narrowing conversion of ‘214’ from ‘int’ to ‘char’ inside { } [-Wnarrowing] 
- Alien::RRDtool -> configure: error: you need either glib with g_regex support or libpcre to compile rrdtool. -> need libxml2-dev (or Alien::libxml2) then relocation issue + multiple RT issues)
- Alien::Gnuplot -> only root install
- Alien::ROOT -> configure: libX11 MUST be installed ([repo](https://github.com/tsee/SOOT/tree/master/Alien-ROOT)) + can not include iostream.h (bundled with sources) -> tested with more recent root lib same error -> then compilation error
- Alien::QtSmoke -> Fetch problem Fetch failed! HTTP response: 500 Internal Server Error [500 Can't connect to ftp.gtlib.cc.gatech.edu:80 (Name or service not known)] at Makefile.PL line 43. -> mirrors are dead
- Alien::SmokeQt -> Found unsuitable Qt version "" from NOTFOUND, this code requires Qt 4.x -> install libqt4-dev -> compilation error
- Alien::Hush Failed to change directory to 'src/': No such file or directory at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild/Repository/Local.pm line 20.

## OK :+1: 
- :heavy_check_mark: ~Alien::GSL -> Could not find any matching files at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild.pm line 442. -> [PR](https://github.com/Perl5-Alien/Alien-GSL/pull/6) and [PR](https://github.com/Perl5-Alien/Alien-GSL/pull/7)~
- :heavy_check_mark: ~Alien::LibJIT -> You need to make sure you have a recent 'libtool' installed and that it can be found in your PATH at inc/Module/Build/AlienLibJIT.pm line 40 -> add libtool-bin flex, bison, texinfo -> Alien::libtool and Alien::bison and Alien::flex and Alien::texinfo are available...~
- :see_no_evil: ~Alien::IUP ###FATAL### No supported GUI subsystem (GTK3, GTK2, X11/Motif) detected! (gonna exit) -> Not KO, just need to install gtk2, gtk3 or x11~
- :heavy_check_mark: ~Alien::LibMagic -> Could not find any matching files at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild.pm line 442. -> [PR](https://github.com/zmughal/p5-Alien-LibMagic/pull/6) or [PR](https://github.com/zmughal-p5CPAN/p5-Alien-LibMagic/pull/8)~
- :heavy_check_mark: ~Alien::UDUNITS2 -> Could not find any matching files at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild.pm line 442. -> [PR](https://github.com/EntropyOrg/p5-Alien-UDUNITS2/pull/10) from me or [PR](https://github.com/EntropyOrg/p5-Alien-UDUNITS2/pull/11)~
- :heavy_check_mark: ~Alien::SDL -> !  Archive::Zip is not installed + FAIL Timed out (> 60s).~
- :heavy_check_mark: ~Alien::SDL2 -> unstable timeout~
- :heavy_check_mark: ~Alien::SNMP::MAXTC -> [PR](https://github.com/ollyg/Alien-SNMP-MAXTC/pull/2) from me~
- :heavy_check_mark: ~Alien::SNMP -> [PR](https://github.com/ollyg/Alien-SNMP/pull/3) from me - ABMB was added but not in the correct phase~
- :heavy_check_mark: ~Alien::libtickit looking for pkg-config termkey... OS unsupported - unable to find GNU libtool -> require libtool~ Alien::libtool exists
- :heavy_check_mark: ~Alien::libtermkey depends on Alien::unibilium + OS unsupported - unable to find GNU libtool -> require libtool~ Alien::libtool exists
- :heavy_check_mark: ~Alien::unibilium requires:    !  ExtUtils::PkgConfig is not installed + OS unsupported - unable to find GNU libtool -> require libtool~ Alien::libtool exists
- :heavy_check_mark: ~Alien::HDF4 -> tarball content changed ? Cannot find hdf library, libdf.a.~
- :heavy_check_mark: ~Alien::raylib -> Makefile:1005: recipe for target '_alien/mm/build' failed -> no problem locally -> need debs~
- :heavy_check_mark: ~Alien::Gimp -> only a probe ? -> need libgimp dev~
- :heavy_check_mark: ~Alien::gputils -> flex -> we should use Alien::flex~ 
- :heavy_check_mark: ~Alien::AntTweakBar -> Can't link/include C library 'X11/cursorfont.h', 'GL/glx.h', 'GL/gl.h', aborting. -> insall non alienazed big deps~
- :heavy_check_mark: ~Alien::TALib -> compilation/build problem -> tiemout~
