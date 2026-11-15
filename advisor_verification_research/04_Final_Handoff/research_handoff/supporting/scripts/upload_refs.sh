#!/usr/bin/env bash
# Print Drive file-reference strings (sha256:<hex>:<abs path>) for the given files.
for f in "$@"; do
  p=$(readlink -f "$f"); h=$(sha256sum "$p" | cut -d' ' -f1); s=$(wc -c < "$p")
  echo "$s  sha256:$h:$p"
done
