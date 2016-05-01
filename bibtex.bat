@ECHO off
SET bibFileDir=c:\mendeley\bibtex

SET "citeKey="
SET citeKey=%1

REM Display CiteKey
ECHO CiteKey=%citeKey%

REM See if Mendeley BibTex file exists
SET bibtexFile=%bibFileDir%\%citeKey%.bib
IF NOT EXIST %bibtexFile% (
    ECHO Error: File not found - %bibtexFile%
    ECHO   * %DATE% %TIME% Error: File not found - %bibtexFile% >> www\wiki\audit_trail.txt
    GOTO :END
)

REM Extract the bibtex data
python bibtex.py %bibFileDir% %citeKey% > www\%citeKey%.txt

REM Get BibTex Doc Type to set Bibtex Category
SET "bibtexDocType="
SET /p bibtexDocType=< www\%citeKey%.txt
REM Display DocType
ECHO DocType=%bibtexDocType%

REM Set Category using the DocType
SET "bibtexCategory="
IF "%bibtexDocType%"=="/* article */" (
    SET bibtexCategory=article
) ELSE IF "%bibtexDocType%"=="/* book */" (
    SET bibtexCategory=book
) ELSE IF "%bibtexDocType%"=="/* thesis */" (
    SET bibtexCategory=thesis
) ELSE IF "%bibtexDocType%"=="/* conference */" (
    ECHO Warning: Not processed - %bibtexDocType% ~ %citeKey%
    ECHO   * %DATE% %TIME% Warning: Not processed - %bibtexDocType% ~ %citeKey% >> www\wiki\audit_trail.txt
    GOTO :END
) ELSE IF "%bibtexDocType%"=="/* unpublished */" (
    ECHO Warning: Not processed - %bibtexDocType% ~ %citeKey%
    ECHO   * %DATE% %TIME% Warning: Not processed - %bibtexDocType% ~ %citeKey% >> www\wiki\audit_trail.txt
    GOTO :END
) ELSE (
    ECHO Error: DocType not found - %bibtexDocType% ~ %citeKey%
    ECHO   * %DATE% %TIME% Error: DocType not found - %bibtexDocType% ~ %citeKey% >> www\wiki\audit_trail.txt
    GOTO :END
)

REM Move the file to correct directory
SET citekeyFile=www\%bibtexCategory%\%citeKey%.txt
MOVE www\%citeKey%.txt %citekeyFile% > \temp\bibtex.out

REM See if DokuWiki txt file exists (ie copy file has worked)
IF NOT EXIST %citekeyFile% (
    ECHO Error: File not found - %citekeyFile%
    ECHO   * %DATE% %TIME% Error: File not found - %citekeyFile% >> www\wiki\audit_trail.txt
    GOTO :END
)

REM FTP the file
CALL ftp\barbourians %bibtexCategory% %citeKey%.txt > \temp\bibtex.out
REM Display the number of bytes transferred
FINDSTR "ftp:" \temp\bibtex.out

REM Write to audit file
ECHO   * %DATE% %TIME% Success: [[%bibtexCategory%:%citeKey%]]>> www\wiki\audit_trail.txt 

REM Clean up
DEL \temp\bibtex.out

:END
ECHO -------------------------------------------------------------------------------
