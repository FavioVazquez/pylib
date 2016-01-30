#!/usr/bin/env bash
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2015-11-05 23:29:15 +0000 (Thu, 05 Nov 2015)
#
#  https://github.com/harisekhon/pylib
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback to help improve or steer this or other code I publish
#
#  http://www.linkedin.com/in/harisekhon
#

set -euo pipefail
srcdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "
# ================== #
# Running PyLib ALL
# ================== #
"

cd "$srcdir";

./whitespace.sh

#./syntax.sh
./pylint.sh

#./python3.sh

../bash-tools/python_compile.sh

../bash-tools/run_scripts.sh

#./help.sh

cd "$srcdir/.."
bash-tools/all.sh
