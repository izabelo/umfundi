import sys
import time

vDelimiter = '#'

# --------------------------------------------------------
# Get the directory and filename as input parameters
# --------------------------------------------------------
inputfiledir = sys.argv[1]
inputfiledir+='\\'
inputfilename = r''
inputfilename+=inputfiledir
inputfilename+=sys.argv[2]

# --------------------------------------------------------
# Initialise all the variables
# --------------------------------------------------------

# --------------------------------------------------------
# Open the input file
# --------------------------------------------------------
fin = open(inputfilename, 'r')

# --------------------------------------------------------
# Read through the file
# --------------------------------------------------------
while 1:
    line=fin.readline() # check for EOF
    if not line: break

    # Initialise all the variables
    vCategory = ''
    vCiteKey = ''
    vDocType = ''
    vFileOutput = ''
    vPageNum = ''
    vText = ''
    vValid = False
    
    if line[4:8] == 'book':
        vValid = True
        vDocType = 'book'
        vCiteKey = line[15:line.find('.')]
        vCategory = line[line.find('[')+11:line.find(']')]
        vText = line[line.find(']')+5:line.find('<cite>')]
        vPageNum = line[line.find('<cite>')+6:line.find('</cite>')]

    elif line[4:10] == 'thesis':
        vValid = True
        vDocType = 'thesis'
        vCiteKey = line[17:line.find('.')]
        vCategory = line[line.find('[')+11:line.find(']')]
        vText = line[line.find(']')+5:line.find('<cite>')]
        vPageNum = line[line.find('<cite>')+6:line.find('</cite>')]

    elif line[4:11] == 'article':
        vValid = True
        vDocType = 'article'
        vCiteKey = line[18:line.find('.')]
        vCategory = line[line.find('[')+11:line.find(']')]
        vText = line[line.find(']')+5:line.find('<cite>')]
        vPageNum = line[line.find('<cite>')+6:line.find('</cite>')]

    if vValid:
        vFileOutput = vCategory+vDelimiter
        vFileOutput+= vDocType+vDelimiter
        vFileOutput+= vCiteKey+vDelimiter
        vFileOutput+= vPageNum+vDelimiter
        vFileOutput+= vText
        print (vFileOutput)
#    else:
#        print (line)

# --------------------------------------------------------
# End of while
# --------------------------------------------------------

# --------------------------------------------------------
# Close the input file
# --------------------------------------------------------
fin.close()
