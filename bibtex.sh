#!/bin/bash

WWW="$HOME/www"
WWWDIR="$WWW/beta/umfundi"
BIBFILEDIR="$HOME/Documents/BibTex"
AUDITFILE="$WWWDIR/wiki/audit_trail.txt"

# Get the current date time
DATETIME=$(date +%c)

# See if a citekey was passed
CITEKEY=$1
if [ $# -ne 1 ]; then
    echo "Error: Not Citekey for $0"
    exit 1
fi

# See if the citekey file exists
filename="$BIBFILEDIR/$CITEKEY.bib"
if [ ! -f $filename ]; then
    echo "Error: File not found - $filename"
    echo "  * $DATETIME Error: File not found - $CITEKEY" >> $AUDITFILE
    exit 2
fi

# See if .bib file contains }}
warning1=''
count=$(cat $filename | grep -v ^title | fgrep "}}" | wc -l)
if [ $count -gt 0 ]; then
    warning1="contains }}..."
fi

# See if .bib file contains {\%}
warning2=''
count=$(cat $filename | grep -v ^title | fgrep "{\%}" | wc -l)
if [ $count -gt 0 ]; then
    warning2="contains {\%}..."
fi

# Display message
echo ${CITEKEY}...${warning1}${warning2}

# Extract the bibtex data
python bibtex.py $BIBFILEDIR $CITEKEY > $WWW/$CITEKEY.txt

# Get BibTex Doc Type to set Bibtex Category
doctype=$(head -1 $WWW/$CITEKEY.txt)

# Set category using the doctype
if [ "$doctype" == "/* article */" ]; then
    category="article"
elif [ "$doctype" == "/* book */" ]; then
    category="book"
elif [ "$doctype" == "/* thesis */" ]; then
    category="thesis"
elif [ "$doctype" == "/* conference */" ]; then
    echo "Warning: Not processed - $doctype ~ $CITEKEY"
    echo "  * $DATETIME Warning: Not processed - $doctype ~ $CITEKEY" >> $AUDITFILE
    exit 3
elif [ "$doctype" == "/* unpublished */" ]; then
    echo "Warning: Not processed - $doctype ~ $CITEKEY"
    echo "  * $DATETIME Warning: Not processed - $doctype ~ $CITEKEY" >> $AUDITFILE
    exit 4
else
    echo "Error: DocType not found - $doctype ~ $CITEKEY"
    echo "  * $DATETIME Error: Doctype not found - $doctype ~ $CITEKEY" >> $AUDITFILE
    exit 5
fi

# Move the file to correct directory
citekeyfile="$WWWDIR/$category/${CITEKEY}.txt"
mv $WWW/$CITEKEY.txt $citekeyfile 

# See if DokuWiki txt file exists (ie copy file has worked)
if [ ! -f $citekeyfile ]; then
    echo "Error: Move failed - $citekeyfile"
    echo "  * $DATETIME Error: Move failed - $CITEKEY" >> $AUDITFILE
    exit 6
fi

# See if ftp must happen (helps for testing)
if [ -f NOFTP ]; then
    exit 99
fi

# FTP the file
$HOME/dokuwiki/barbourians/beta.sh $category ${CITEKEY} &> /tmp/${CITEKEY}.out
# Get the number of bytes transferred
bytes=$(cat /tmp/${CITEKEY}.out | grep "bytes sent" | wc -l)
if [ $bytes -eq 0 ]; then
    echo "Error: ftp failed for $category $CITEKEY"
    echo "  * $DATETIME Error: ftp failed for $CITEKEY" >> $AUDITFILE
    exit 7
fi

# Write to audit file
echo "Success: $category $CITEKEY"
echo "  * $DATETIME Success: [[umfundi:$category:$CITEKEY]]" >> $AUDITFILE

# Clean up
rm /tmp/${CITEKEY}.out

#EOF