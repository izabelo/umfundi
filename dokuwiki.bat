@ECHO off
CLS

REM Process the citekey found in each line of dokuwiki.txt
FOR /F %%A IN (dokuwiki.txt) DO CALL bibtex %%A

REM ftp the audit trail to the wiki
CALL ftp\barbourians wiki audit_trail.txt > \temp\dokuwiki.out
FINDSTR "ftp:" \temp\dokuwiki.out

REM Clean up
DEL \temp\dokuwiki.out

ECHO ===============================================================================
