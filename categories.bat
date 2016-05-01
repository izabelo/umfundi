@ECHO off

REM Set category output directory and filename with all the entries
SET categoryDir=www\category
SET categoryFile=all.out
SET categorySort=all-sorted.out

REM Combine the comments from all doctypes into one file
ECHO Combining ...
TYPE %categoryDir%\article.out  > %categoryDir%\%categoryFile%
TYPE %categoryDir%\book.out    >> %categoryDir%\%categoryFile%
TYPE %categoryDir%\thesis.out  >> %categoryDir%\%categoryFile%

REM Extract the categories
ECHO Extracting ...
python categories-extract.py %categoryDir% %categoryFile% > \temp\categories.out

REM sort the file by category
ECHO Sorting ...
SORT \temp\categories.out > %categoryDir%\%categorySort%

REM Create the Dokuwiki category pages
ECHO Creating ...
python categories-create.py %categoryDir% %categorySort% >> www\wiki\audit_trail.txt 

REM Combine all the pages into one page fr the start page
DEL %categoryDir%\start.txt
ECHO ====== All Categories ====== > \temp\start.txt
TYPE %categoryDir%\*.txt >> \temp\start.txt
MOVE \temp\start.txt %categoryDir%\start.txt

REM FTP the category pages
ECHO Uploading pages ...
CALL ftp\barbourians-mput category > \temp\categories.out

REM ftp the audit trail to the wiki
ECHO Uploading audit trail ...
CALL ftp\barbourians wiki audit_trail.txt > \temp\categories.out
FINDSTR "ftp:" \temp\categories.out

REM Clean up
DEL \temp\categories.out

:END
ECHO -------------------------------------------------------------------------------
