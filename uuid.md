# uuid

## uuid.pc

### debian

```
prefix=/usr
exec_prefix=/usr
libdir=/usr/lib/x86_64-linux-gnu
includedir=/usr/include

Name: uuid
Description: Universally unique id library
Version: 2.31.1
Requires:
Cflags: -I${includedir}/uuid
Libs: -L${libdir} -luuid
```

### alien

```
prefix=/usr/local/lib/x86_64-linux-gnu/perl/5.26.1/auto/share/dist/Alien-libuuid
exec_prefix=${prefix}
libdir=${prefix}/lib
includedir=${prefix}/include

Name: uuid
Description: Universally unique id library
Version: 1.0.3
Requires:
Cflags: -I${includedir}/uuid
Libs: -L${libdir} -luuid
```
