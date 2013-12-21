#!/bin/bash

TOP=`pwd`

RIPPLE=$TOP/..
RELEASE=release

function release_tarball()
{
	local _date=`date +%Y%m%d`
	local _tarball=$RELEASE-$_date.tar.gz

	pushd $RIPPLE >/dev/null
	tar --exclude=.git -zcf $_tarball $RELEASE
	popd >/dev/null

	echo "Tarball: $RIPPLE/$_tarball"
}

function release_copy()
{
	local _list="getdata.py safe-start.sh websocket.py"

	mkdir -p $RIPPLE/$RELEASE
	for file in $_list; do
		cp -f $file $RIPPLE/$RELEASE
	done
}

function usage()
{
	echo "Usage:"
	echo "  `basename $0` [option]"
	echo "Option:"
	echo "  --copy     copy files to release directory"
	echo "  --tarball  create tarball for release directory"

	exit 0
}

if [ $# -ne 1 ]; then
	usage
fi

case $1 in
	--copy)
		release_copy
		;;
	--tarball)
		release_tarball
		;;
	*)
		usage
		;;
esac

