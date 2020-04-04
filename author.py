# author.py
import sys
import time
 
# --------------------------------------------------------
# Get the directory and filename as input parameters
# --------------------------------------------------------
inputfiledir = sys.argv[1]
inputfiledir+='/'
inputfilename = r''
inputfilename+=inputfiledir
inputfilename+=sys.argv[2]
inputfilename+='.bib'

# --------------------------------------------------------
# Open the input file
# --------------------------------------------------------
fin = open(inputfilename, 'r')

# --------------------------------------------------------
# Initialise all the variables
# --------------------------------------------------------
vAuthor = 'No Author'

# --------------------------------------------------------
# Read through the file
# --------------------------------------------------------
while 1:
    line=fin.readline() # check for EOF
    if not line: break

    if line[0:6] == 'author':
        s = line[6+4:line.find('}')]
        if s.count(' and ') > 0:
            s = s[0:s.find(' and ')]
        vAuthor = s

# --------------------------------------------------------
# Turn author name into a DokoWiki link
# --------------------------------------------------------
vAuthorLink = vAuthor
vAuthorLink = vAuthorLink.strip()
vAuthorLink = vAuthorLink.lower()
vAuthorLink = vAuthorLink.replace(".","")
vAuthorLink = vAuthorLink.replace(",","")
vAuthorLink = vAuthorLink.replace("'","_")
vAuthorLink = vAuthorLink.replace(" ","_")

# --------------------------------------------------------
# Display: Full author name as h1 heading
# --------------------------------------------------------
vDokuTemplate = '====== '+vAuthor+' ======'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Display: Link to author bio
# --------------------------------------------------------
vDokuTemplate = '{{page>author:bio:'+vAuthorLink+'}}'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Display: Backlinks
# --------------------------------------------------------
vDokuTemplate = '===== Links here ====='
print (vDokuTemplate)
vDokuTemplate = '{{backlinks>.}}'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# End of file message
# --------------------------------------------------------
vDokuTemplate = '/* Page automatically generated on '
vDokuTemplate+=time.strftime("%d/%m/%Y")
vDokuTemplate+=' at '
vDokuTemplate+=time.strftime("%H:%M:%S")
vDokuTemplate+=' */'
print (vDokuTemplate)
print ('\n\r')

# --------------------------------------------------------
# Close the input file
# --------------------------------------------------------
fin.close()
