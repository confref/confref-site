#!/bin/sh
# Build the site and copy it to www.confref.org (bart, decision 0015 of confref-data). Deployment is by hand:
# a commit does not change the live site.
set -eu
cd "$(dirname "$0")/.."
out="$HOME/lokal/confref/work/site-public"
rm -rf "$out"
hugo --gc --minify -d "$out"
rsync -rtp --delete --exclude='.*' "$out/" bart:/home/eckert/www.confref.org/
