tmpfile=$(mktemp /tmp/tmp.XXXXXX)

exec 3>"$tmpfile"
exec 4<"$tmpfile"

rm "$tmpfile"

echo test >&3

head -n 1 <&4

exec 3>-