# categories-create.py
import sys
import time

vDelimiter = '#'

# --------------------------------------------------------
# Get the directory and filename as input parameters
# --------------------------------------------------------
vInputFileDir = sys.argv[1]
vInputFileDir+='\\'
inputfilename = r''
inputfilename+=vInputFileDir
inputfilename+=sys.argv[2]

# --------------------------------------------------------
# Initialise all the variables
# --------------------------------------------------------
vCategory = ''
vCategoryName = ''
vCategoryPrev = ''
vCiteKey = ''
vDocType = ''
vDokuTemplate = ''
vOutputFileName = ''
vOutputFileOpen = False
vPageNum = ''
vText = ''

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
    
    # Get the category as the first field
    vCategoryName = line[0:line.find(vDelimiter)].strip()
    if vCategoryName:
        # change to lowercase and replace spaces and dashes with underscores
        s = vCategoryName.lower()
        s = s.replace("?","")
        s = s.replace(" ","_")
        s = s.replace("-","_")
        s = s.replace(".","_")
        s = s.replace("__","_")
        vCategory = s

        # If a new category then open a new file
        if vCategory != vCategoryPrev:

            # Close the existing output file if open
            if vOutputFileOpen:
                vDokuTemplate ='\n'
                vDokuTemplate+='/* Page automatically generated on '
                vDokuTemplate+=time.strftime("%d/%m/%Y")
                vDokuTemplate+=' at '
                vDokuTemplate+=time.strftime("%H:%M:%S")
                vDokuTemplate+=' */ \n'
                fout.write(vDokuTemplate);
                fout.close()                     
                vOutputFileOpen = False
            
            # Create a new Dokuwiki page file
            vOutputFileName = vInputFileDir+'\\'+vCategory+'.txt'
            fout = open(vOutputFileName, 'w')
            vOutputFileOpen = True

            # Print output that can be added to the audit trail page
            vDokuTemplate ='  * '
            vDokuTemplate+=time.strftime("%d-%m-%Y")
            vDokuTemplate+=' '
            vDokuTemplate+=time.strftime("%H:%M:%S")
            vDokuTemplate+=' Category Page: '
            vDokuTemplate+='[[category:'+vCategory+']]'
            print (vDokuTemplate)

            # Create the heading for the page
            vDokuTemplate ='====== '+vCategoryName+' ======'
            vDokuTemplate+='\n\n'
            fout.write(vDokuTemplate);

        # File is now open so get the data
        s = line
        # Document type
        s = s[s.find(vDelimiter)+1:]
        vDocType = s[0:s.find(vDelimiter)]
        # Cite key
        s = s[s.find(vDelimiter)+1:]
        vCiteKey = s[0:s.find(vDelimiter)]
        # Page number
        s = s[s.find(vDelimiter)+1:]
        vPageNum = s[0:s.find(vDelimiter)]
        vPageNum = vPageNum[vPageNum.find('(')+1:vPageNum.find(')')]
        # Extract text
        s = s[s.find(vDelimiter)+1:]
        vText = s[0:s.find(vDelimiter)]
        
        # Write the data to the output file
        vDokuTemplate = vText
        vDokuTemplate+=' ([['+vDocType+':'+vCiteKey+'|'+vCiteKey+', '+vPageNum+']])'
        vDokuTemplate+='\n\n'
        fout.write(vDokuTemplate);

        # Store current category
        vCategoryPrev = vCategory
        
#    else:
#        print (line)

# --------------------------------------------------------
# End of while
# --------------------------------------------------------

# --------------------------------------------------------
# Close the input and output files
# --------------------------------------------------------
fin.close()
if vOutputFileOpen:
    vDokuTemplate ='\n'
    vDokuTemplate+='/* Page automatically generated on '
    vDokuTemplate+=time.strftime("%d/%m/%Y")
    vDokuTemplate+=' at '
    vDokuTemplate+=time.strftime("%H:%M:%S")
    vDokuTemplate+=' */ \n'
    fout.write(vDokuTemplate);
    fout.close()                     

# End of file
