#!/usr/bin/python
# Daniel Hnyk (c) 2014, All rights reserved

# This script should export notes taken by Desktop Mendeley version 1.11
# to txt or csv format

# To run this script you need to have pandas library. It can be
# installed by pip with last version of Python by 'pip install pandas'

# This script comes with no warranty and was create only for my personal
# use, hence lacks any of noticeable futures - still better than nothing
# Feel free to contact me

# You need to adjust (at least) TWO variables in this script:
## user_mail: this mail is the one you use to sign into Mendeley. It can
###              be found on their webpage or in app - File -> Sign ...
## path: this is a path where Mendeley stores it's files and most 
##          importantly - the database with everything
##          this path is OS-dependent and also on your installation
##          the one provided under is the Linux variant

import sqlite3 as lite
user_mail = "barbourians@gmail.com"
path = "sqlite\\{0}@www.mendeley.com.sqlite".format(user_mail)

con = lite.connect(path)
cur = con.cursor()

cur.execute("SELECT id, title FROM Documents")
documents = cur.fetchall()

cur.execute("SELECT id, documentId, page, note, createdTime, modifiedTime FROM FileNotes")
notes = cur.fetchall()

import pandas as pd
df = pd.DataFrame(data=notes, columns=["id", "documentId", "page", "note", "createdTime", "modifiedTime"])

documents = dict(documents)
df.documentId = df.documentId.map(documents)

def to_string(df, *filename):
    """
    Returns notes in nice formated string
        
    If filename is given, it saves string to this file
    """
    
    vyslstr = ""
    for name, note in df.iterrows():
        type(note)
        vyslstr += """
ID: {0}|File: {1}|Page: {2}
{3}
        """.format(note.id, note.documentId, note.page, note.note)
    
    if filename:
        with open(filename[0], mode="w", encoding="utf-8") as fout:
            fout.write(vyslstr)
    return(vyslstr)

def to_csv(df):
    "Detailed output to csv file"

    df.to_csv("notes_mendeley.csv")

to_csv(df)
to_string(df, "notes_mendeley.txt")