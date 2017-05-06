# kindle.py
import sys
import time

# --------------------------------------------------------
# Get the directory and filename as input parameters
# --------------------------------------------------------
inputASIN = sys.argv[1]
inputCitekey = sys.argv[2]

inputfiledir = 'kindle\\'
inputfilename = r''
inputfilename+=inputfiledir
inputfilename+=inputASIN
inputfilename+='.txt'

# --------------------------------------------------------
# Open the input file
# --------------------------------------------------------
fin = open(inputfilename, 'r')

# --------------------------------------------------------
# Initialise all the variables
# --------------------------------------------------------
vLocation = ''
vPageNum = 0

# Setup kindle link addresses
vKindleAmazon = 'https://kindle.amazon.com/your_highlights'
vKindleURL = 'kindle://book?action=open&asin='+inputASIN+'&'

# --------------------------------------------------------
# Print Heading
# --------------------------------------------------------
vDokuTemplate = '/* '+inputASIN+' */'
print (vDokuTemplate,)
vDokuTemplate = '===== Kindle highlights ====='
print (vDokuTemplate)

# --------------------------------------------------------
# Read through the file
# --------------------------------------------------------
while 1:
    line=fin.readline() # check for EOF
    if not line: break

    # TODO: Remove illegal characters (currently must be done manually
    s = line.strip()
    # Add a bullet point
    s = '  * '+s

    # Delete "Delete this highlight"
    x = s.find('* Delete this highlight')
    if x > 0:
        s = s[0:x].rstrip()
    # Ignore line "Add a note"
    if s[0:14] == '  * Add a note':
        s = ''
    # Indent lines that begin with "Note: "
    if s[0:10] == '  * Note: ':
        s = '  '+s
    # Remove "Edit" at end of line
    if s[len(s)-4:len(s)] == 'Edit':
        s = s[0:len(s)-4]
    # Turm "Read more at location" into a page link
    x = s.find('Read more at location')
    if x > 0:
        vPageNum = s[x+22:]
        vLocation = 'location='+vPageNum
        s = s[0:x]+' //([['+vKindleURL+vLocation+'|loc='+vPageNum+']])//'

    # Print out the line
    if len(s) > 0:
       vDokuTemplate = s
       print (vDokuTemplate)

# --------------------------------------------------------
# End of while
# --------------------------------------------------------
print ('')

# --------------------------------------------------------
# Print Footer
# --------------------------------------------------------
vDokuTemplate = "//"
vDokuTemplate+="[["+vKindleAmazon+'|Kindle highlights]]'
vDokuTemplate+=' automatically extracted on '
vDokuTemplate+=time.strftime("%d/%m/%Y")
vDokuTemplate+=' at '
vDokuTemplate+=time.strftime("%H:%M:%S")
vDokuTemplate+='//'
print (vDokuTemplate)
print ('\n\r', end=' ')

# --------------------------------------------------------
# Close the input file
# --------------------------------------------------------
fin.close()
