#! /bin/sh
#
# Written by configsmoke.pl v0.091
# Wed Jul  7 17:43:03 2021
# NOTE: Changes made in this file will be *lost*
#       after rerunning configsmoke.pl
#
# 
# Uncomment this to be as nice as possible. (Jarkko)
# (renice -n 20 $$ >/dev/null 2>&1) || (renice 20 $$ >/dev/null 2>&1)

cd /home/Test-Smoke/bin
CFGNAME=${CFGNAME:-smokecurrent_config}
LOCKFILE=${LOCKFILE:-smokecurrent.lck}
continue=''
if test -f "$LOCKFILE" && test -s "$LOCKFILE" ; then
    echo "We seem to be running (or remove $LOCKFILE)" >& 2
    exit 200

fi
echo "$CFGNAME" > "$LOCKFILE"


PATH=/home/Test-Smoke/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

export PATH
umask 0
/usr/bin/perl /home/Test-Smoke/bin/tssmokeperl.pl -c "$CFGNAME" $continue $*

rm "$LOCKFILE"
