@ECHO off

SET workingDir="sqlite\"
SET mendeleyDir="C:\Users\Ian\AppData\Local\Mendeley Ltd\Mendeley Desktop"
SET mendeleyDB="barbourians@gmail.com@www.mendeley.com.sqlite"

REM Move current working database to backup
MOVE %workingDir%"\"%mendeleyDB%

REM Copy current database to working directory
COPY %mendeleyDir%"\"%mendeleyDB% %workingDir%

python mendeley_notes.py
