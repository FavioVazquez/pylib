#!/usr/bin/env bash
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2015-05-25 01:38:24 +0100 (Mon, 25 May 2015)
#
#  https://github.com/harisekhon/pylib
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback to help improve or steer this or other code I publish
#
#  http://www.linkedin.com/in/harisekhon
#

set -eu

hr(){
    echo "===================="
}

if [ -n "${TRAVIS:-}" ]; then
    sudo=sudo
else
    sudo=""
fi

#export SPARK_HOME="$(ls -d tests/spark-*-bin-hadoop* | head -n 1)"

. "$srcdir/excluded.sh"