#!/bin/bash

CITEKEYS="$HOME/citekeys.txt"

# See if citekeys file exists
if [ ! -f $CITEKEYS ]; then
    echo "ERROR: Citekeys file not found ~ $CITEKEYS"
    exit 1
fi

# Process each citekey in the file
for filename in $(cat $CITEKEYS)
do
    ./bibtext.sh $filename
done

# FTP the audit trail
$HOME/dokuwiki/barbourians/beta.sh wiki audit_trail &> /tmp/audit_trail.out
# Get the number of bytes transferred
bytes=$(cat /tmp/audit_trail.out | grep "bytes sent" | wc -l)
if [ $bytes -eq 0 ]; then
    echo "Error: ftp failed for audit trail"
    exit 2
fi

# Clean up
rm /tmp/audit_trail.out

#EOF