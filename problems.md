# Aliens problems

## Can't locate Alien/Base/ModuleBuild.pm
- Alien::Sodium -> PR from plicease + waiting adoption from genio
- Alien::Lua
- Alien::SFML

### Alranel 
- Alien::qd -> PR from plicease already merged -> need only 0.02 release I guess
- Alien::GEOS  -> PR from plicease already merged -> need only 0.02 release I guess

### Getty
- Alien::mpg123 -> PR from me
- Alien::ffmpeg
- Alien::sismpctl
- Alien::gettext

### OLIVER
- Alien::SNMP::MAXTC
- Alien::SNMP

### GUGOD 
- Alien::CImg
- Alien::libsndfile


## Something else
- Alien::GSL -> Could not find any matching files at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild.pm line 442.
- Alien::Plotly::Orca prereq Fil::Copy::Recursive not reproducible locally
- Alien::Hush Failed to change directory to 'src/': No such file or directory at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild/Repository/Local.pm line 20.
- Alien::DBD::SQLite::BundledExtensions Can't locate File/ShareDir.pm in @INC not reproduced locally
- Alien::Gnuplot -> tarball content changed I guess
- Alien::raylib -> Makefile:1005: recipe for target '_alien/mm/build' failed
- Alien::HDF4 -> tarball content changed ? Cannot find hdf library, libdf.a.
- Alien::LibANN -> syntax error at inc/Devel/CheckLib.pm line 164, near "$mm_attr_key qw(LIBS INC)"
- Alien::AntTweakBar -> Can't link/include C library 'X11/cursorfont.h', 'GL/glx.h', 'GL/gl.h', aborting.
- Alien::LibBigWig -> fatal error: curl/curl.h: No such file or directory I do not reproduce locally
- Alien::LibJIT -> You need to make sure you have a recent 'libtool' installed and that it can be found in your PATH at inc/Module/Build/AlienLibJIT.pm line 40
- Alien::RRDtool -> configure: error: you need either glib with g_regex support or libpcre to compile rrdtool.
- Alien::Protobuf -> ??
- Alien::DDC-Concordance -> configure: error: could not find pcre_compile(): ensure that LDFLAGS, LIBS are set to link to libpcre
- Alien::OpenVcdiff -> compilation error src/vcdecoder_test.cc:33:3: error: narrowing conversion of ‘214’ from ‘int’ to ‘char’ inside { } [-Wnarrowing]
- Alien::Gimp -> only a probe ?
- Alien::ROOT -> configure: libX11 MUST be installed
- Alien::SDL -> -> !  Archive::Zip is not installed + FAIL Timed out (> 60s).
- Alien::MeCab -> Detected circular dependencies Alien-MeCab-0.97005 -> Alien-MeCab-0.97005

### PLU 
- Alien::Gearman -> depends on Alien::Libevent that fails
- Alien::Libevent -> syntax error

### ATHREEF
- Alien::HIDAPI -> depends on LibUSB that failed
- Alien::LibUSB -> Can't locate Alien/libudev.pm in @INC (you may need to install the Alien::libudev module) prereq missing

### CBUREL 
- Alien::QtSmoke -> Fetch problem Fetch failed! HTTP response: 500 Internal Server Error [500 Can't connect to ftp.gtlib.cc.gatech.edu:80 (Name or service not known)] at Makefile.PL line 43.
- Alien::SmokeQt -> Found unsuitable Qt version "" from NOTFOUND, this code requires Qt 4.x

### ZMUGHAL
- Alien::pdf2htmlEX -> depends on Alien::FontForge Alien::Poppler
- Alien::Poppler -> Could NOT find Freetype (missing: FREETYPE_LIBRARY FREETYPE_INCLUDE_DIRS)
- Alien::FontForge -> tarball content changed ? -> sh: 0: Can't open ./bootstrap
- Alien::LibMagic -> Could not find any matching files at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild.pm line 442.
- Alien::UDUNITS2 -> Could not find any matching files at /usr/local/share/perl/5.26.1/Alien/Base/ModuleBuild.pm line 442.

### KMX
- Alien::IUP ###FATAL### No supported GUI subsystem (GTK3, GTK2, X11/Motif) detected! (gonna exit)
- Alien::FreeImage ->  error: call of overloaded ‘powf64(int, int)’ is ambiguous

### KIWIROY
- ALien::MUSCLE ExtUtils::CBuilder version 0.280226 required--this is only version 0.280225 at /home/tduponchelle/.cpanm/work/1588163506.974/Alien-MUSCLE-0.01/alienfile line 8.
- Alien::KentSrc pngwrite.c:7:10: fatal error: png.h: No such file or directory

### PEVANS
- Alien::libtickit looking for pkg-config termkey... OS unsupported - unable to find GNU libtool
- Alien::libtermkey depends on Alien::unibilium + OS unsupported - unable to find GNU libtool
- Alien::unibilium requires:    !  ExtUtils::PkgConfig is not installed + OS unsupported - unable to find GNU libtool

