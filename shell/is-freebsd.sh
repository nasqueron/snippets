#   -------------------------------------------------------------
#   Determine etc directory path
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

. /etc/os-release

if [ "$ID" = "freebsd" ]; then
    ETC=/usr/local/etc
else
    ETC=/etc
fi
