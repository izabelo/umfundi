@ECHO off

REM Document type is passed as a parameter
SET "docType="
SET docType=%1

REM See if notes directory exists
SET notesDir=www\%docType%\notes
IF NOT EXIST %notesDir% (
    ECHO Error: Directory not found - %notesDir%
    ECHO   * %DATE% %TIME% Error: Directory not found - %notesDir% >> www\wiki\audit_trail.txt
    GOTO :END
)

ECHO Processing document type: %docType%

REM Get all the files in the notes directory
CALL ftp\barbourians-mget %docType% notes > \temp\footnotes.out

REM Count the number of files
DIR %notesDir%\*.txt | FIND /I "txt" /C >\temp\footnotes.out
SET /p tempv=<\temp\footnotes.out
ECHO %tempv% note pages found

REM Extract the comments
FINDSTR "((" %notesDir%\*.txt > www\category\%docType%.out

REM count the number of footnotes extracted
TYPE www\category\%docType%.out | FIND /i "www" /C >\temp\footnotes.out
SET /p tempv=<\temp\footnotes.out
ECHO %tempv% comments found

REM Add a line feed at the end of the file
ECHO. >> www\category\%docType%.out

REM Clean up
DEL \temp\footnotes.out

:END
ECHO -------------------------------------------------------------------------------
