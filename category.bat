@ECHO off
CLS

REM Download and extract the footnotes for the notes pages
CALL footnotes article
CALL footnotes book
CALL footnotes thesis

REM Create and upload the category pages
CALL categories

ECHO ===============================================================================
