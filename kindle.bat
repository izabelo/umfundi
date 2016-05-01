@ECHO off

SET "ASIN="
SET "citeKey="
SET ASIN=%1
SET citeKey=%2

REM Display CiteKey
ECHO Processing %ASIN% for %citeKey%

REM See if ASIN file exists
SET "ASINFile="
SET ASINFile=kindle\%ASIN%.txt
IF NOT EXIST %ASINFile% (
    ECHO Error: Kindle Highlights File not found - %ASINFile%
    GOTO :END
)

REM Define name of citekey file to store the Kindle highlights
SET citekeyFile=www\book\kindle\%citeKey%.txt

REM Extract the bibtex data
IF NOT EXIST kindle.py (
    ECHO Fatal Error: Python file not found - kindle.py
    GOTO :END
)
python kindle.py %ASIN% %citeKey% > %citekeyFile%

REM See if kindle citekey file exists
IF NOT EXIST %citekeyFile% (
    ECHO Error: Citekey File not found - %citekeyFile%
    GOTO :END
)

REM FTP the file
CALL ftp\barbourians book/kindle %citeKey%.txt

REM Write to audit file
ECHO   * %DATE% %TIME% Success: [[book:kindle:%citeKey%]]>> www\wiki\audit_trail.txt 

:END
ECHO -------------------------------------------------------------------------------
