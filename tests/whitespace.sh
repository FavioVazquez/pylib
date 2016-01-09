#!/usr/bin/env bash
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2016-01-09 18:50:56 +0000 (Sat, 09 Jan 2016)
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

cd "$srcdir/.."

. "tests/utils.sh"

found=0
for filename in $(find "${1:-.}" -maxdepth 2 -type f -iname '*.py' -o -iname '*.jy'); do
    isExcluded "$filename" && continue
    grep -Hn '^[[:space:]]\+$' "$filename" && found=1 || :
done
if [ $found == 1 ]; then
    echo "Whitespace only lines detected!"
    exit 1
fi
