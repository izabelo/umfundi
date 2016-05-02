import sys
import time

# --------------------------------------------------------
# Get the directory and filename as input parameters
# --------------------------------------------------------
inputfiledir = sys.argv[1]
inputfiledir+='\\'
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
vAbstract = ''
vAddress = ''
vAnnote = ''
vArchivePrefix = ''
vArxivId = ''
vAsin = ''
vAuthor = ''
vBibTex = ''
vBooktitle = ''
vChapter = ''
vCiteKey = ''
vDocType = ''
vDoi = ''
vEdition = ''
vEditor = ''
vEprint = ''
vFile = ''
vInstitution = ''
vIsbn = ''
vIssn = ''
vIssue = ''
vJournal = ''
vKeywords = ''
vMendeleyTags = ''
vOrganization = ''
vPages = ''
vPmid = ''
vPublisher = ''
vSchool = ''
vTitle = ''
vTitleHeading = ''
vType = ''
vUrl = ''
vVolume = ''
vYear = 'n.d.'

# --------------------------------------------------------
# Read through the file
# --------------------------------------------------------
while 1:
    line=fin.readline() # check for EOF
    if not line: break

    if line[0:5] == '@book':
        vDocType = 'book'
        vBibTex+=line
        vCiteKey = line[6:line.find(',')]
    elif line[0:8] == '@article':
        vDocType = 'article'
        vBibTex+=line
        vCiteKey = line[9:line.find(',')]
    elif line[0:10] == '@phdthesis':
        vDocType = 'thesis'
        vBibTex+=line
        vCiteKey = line[11:line.find(',')]
    elif line[0:11] == '@techreport':
        vDocType = 'report'
        vBibTex+=line
        vCiteKey = line[12:line.find(',')]
    elif line[0:12] == '@unpublished':
        vDocType = 'unpublished'
        vBibTex+=line
        vCiteKey = line[13:line.find(',')]
    elif line[0:13] == '@incollection':
        vDocType = 'book'
        vBibTex+=line
        vCiteKey = line[14:line.find(',')]
    elif line[0:14] == '@inproceedings':
        vDocType = 'conference'
        vBibTex+=line
        vCiteKey = line[15:line.find(',')]
    elif line[0:3] == 'doi':
        vBibTex+=line
        vDoi = line[3+4:line.find('}')]
    elif line[0:3] == 'url':
        vBibTex+=line
        vUrl = line[3+4:line.find('}')]
    elif line[0:4] == 'file':
        vFile = line[4+4:line.find('}')]
    elif line[0:4] == 'isbn':
        vBibTex+=line
        vIsbn = line[4+4:line.find('}')]
    elif line[0:4] == 'issn':
        vBibTex+=line
        vIssn = line[4+4:line.find('}')]
    elif line[0:4] == 'pmid':
        vBibTex+=line
        vIssn = line[4+4:line.find('}')]
    elif line[0:4] == 'type':
        vBibTex+=line
        vType = line[4+4:line.find('}')]
    elif line[0:4] == 'year':
        vBibTex+=line
        vYear = line[4+4:line.find('}')]
    elif line[0:5] == 'pages':
        vBibTex+=line
        vPages = line[5+4:line.find('}')]
    elif line[0:5] == 'title':
        vBibTex+=line
        vTitle = line[5+5:line.find('}')]
    elif line[0:6] == 'eprint':
        vBibTex+=line
        vEprint = line[6+4:line.find('}')]
    elif line[0:6] == 'author':
        vBibTex+=line
        vAuthor = line[6+4:line.find('}')]
    elif line[0:6] == 'volume':
        vBibTex+=line
        vVolume = line[6+4:line.find('}')]
    elif line[0:6] == 'editor':
        vBibTex+=line
        vEditor = line[6+4:line.find('}')]
    elif line[0:6] == 'school':
        vBibTex+=line
        vSchool = line[6+4:line.find('}')]
    elif line[0:6] == 'number':
        vBibTex+=line
        vIssue = line[6+4:line.find('}')]
    elif line[0:6] == 'annote':
        vAnnote = line[6+4:line.find('}')]
        # Amazon Kindle ASIN is in notes field
        if line[0:15] == 'annote = {ASIN:':
            vAsin = line[15:25]
    elif line[0:7] == 'chapter':
        vChapter = line[7+4:line.find('}')]
    elif line[0:7] == 'arxivId':
        vBibTex+=line
        vArxivId = line[7+4:line.find('}')]
    elif line[0:7] == 'journal':
        vBibTex+=line
        vJournal = line[7+4:line.find('}')]
    elif line[0:7] == 'address':
        vBibTex+=line
        vAddress = line[7+4:line.find('}')]
    elif line[0:7] == 'edition':
        vBibTex+=line
        vEdition = line[7+4:line.find('}')]
    elif line[0:8] == 'abstract':
        vAbstract = line[8+4:line.find('}')]
    elif line[0:8] == 'keywords':
        vKeywords = line[8+4:line.find('}')]
    elif line[0:9] == 'booktitle':
        vBooktitle = line[9+4:line.find('}')]
    elif line[0:9] == 'publisher':
        vBibTex+=line
        vPublisher = line[9+4:line.find('}')]
    elif line[0:11] == 'institution':
        vInstitution = line[11+4:line.find('}')]
    elif line[0:12] == 'organization':
        vOrganization = line[12+4:line.find('}')]
    elif line[0:13] == 'mendeley-tags':
        vMendeleyTags = line[13+4:line.find('}')]
    elif line[0:13] == 'archivePrefix':
        vBibTex+=line
        vArchivePrefix = line[13+4:line.find('}')]
#    else:
#        print ('###',line)

# Closing bracket for BibTex items
vBibTex+='}'
# --------------------------------------------------------
# End of while
# --------------------------------------------------------

# ========================================================
# Use extracted fields to produce page elements
# --------------------------------------------------------
# Put Authors into a list (array). If not Authors use editors
# --------------------------------------------------------
vAuthorList = []
s = vAuthor
if s == '':
    s = vEditor

if not s == '':
    while not s.count(' and ') == 0:
        vAuthorDisplay = s[0:s.find(' and ')]
        vAuthorList.append(vAuthorDisplay)
        s = s[s.find(' and ')+5:]

    vAuthorDisplay = s
    vAuthorList.append(vAuthorDisplay)

# --------------------------------------------------------
# Format authors as per APA style guidelines
# --------------------------------------------------------
vAuthorAPA = []
for x in range(0, len(vAuthorList)):
    s = vAuthorList[x]
    if (s.find(',')) < 1:
        # Only Surname was present
        vAuthorDisplay = s
    else:
        vAuthorDisplay = s[0:s.find(',')+1]
        s = s[s.find(','):]
        while not s.find(' ') < 1:
            vAuthorDisplay+=' '+s[s.find(' ')+1:s.find(' ')+2]+'.'
            s = s[s.find(' ')+1:]

    vAuthorAPA.append(vAuthorDisplay)

# --------------------------------------------------------
# Format authors as per Chicago style guidelines
# --------------------------------------------------------
vAuthorChicago = []
for x in range(0, len(vAuthorList)):
    s = vAuthorList[x]
    if (s.find(',')) < 1:
        # Only Surname was present
        vAuthorDisplay = s
    else:
        vAuthorDisplay = s[s.find(',')+1:]+' '
        vAuthorDisplay+= s[0:s.find(',')]

    vAuthorChicago.append(vAuthorDisplay)
    
# --------------------------------------------------------
# For each author create a link to their DokuWiki page
# --------------------------------------------------------
vAuthorLink = []
for x in range(0, len(vAuthorList)):
    s = vAuthorList[x].lower()
    s = s.replace(",","")
    s = s.replace(" ","_")
    vAuthorLink.append(s)

# --------------------------------------------------------
# Heading: Document Type (This is here to move .txt to correct directory)
# --------------------------------------------------------
print ('/*',vDocType,'*/')
print ('~~NOTOC~~','\n')

# --------------------------------------------------------
# Prepare h1 heading
# --------------------------------------------------------
# Find the first author surname
vAuthorDisplay = ''
if len(vAuthorList) > 0:
    s = vAuthorList[0]
    if (s.find(',')) < 1:
        vAuthorDisplay = s
    else:
        vAuthorDisplay = s[0:s.find(',')]

# Add other authors        
if len(vAuthorList) == 2:
    s = vAuthorList[1]
    if (s.find(',')) < 1:
        vAuthorDisplay+=' & '+s
    else:
        vAuthorDisplay+=' & '+s[0:s.find(',')]
elif len(vAuthorList) > 2:
    vAuthorDisplay+=' et al.'

# For books: Show Author Firstname & Lastname
if vDocType == 'book':
    s = ''
    if len(vAuthorList) > 0:
        s = vAuthorList[0]
        if (s.find(',')) > 1:
            s = s[s.find(',')+2:]+' '+s[0:s.find(',')]
        
        s = ' by '+s
        if vAuthor == '':
            s = ' Edited'+s

    vAuthorDisplay = s
    # If more than one author add et al.
    if len(vAuthorList) > 1:
        vAuthorDisplay+=' et al.'

# If title is more than 80 characters then shorten
s = vTitle
if len(s) > 80:
    if (s.find(' - ')) > 0:
        s = s[0:s.find(' - ')+1]
if len(s) > 80:
    if (s.find(': ')) > 0:
        s = s[0:s.find(': ')]
if len(s) > 80:
    if (s.find('" ')) > 0:
        s = s[0:s.find('" ')+1]
if len(s) > 80:
    if (s.find('? ')) > 0:
        s = s[0:s.find('? ')+1]
if len(s) > 80:
    if (s.find(' (')) > 0:
        s = s[0:s.find(' (')+1]
if len(s) > 80:
        s = s[0:80]+"..."
vTitleHeading = s
     
# Show surname and title in page heading
if vDocType == 'book':
    vDokuTemplate = '====== '+vTitleHeading+' ('+vYear+')'+vAuthorDisplay+' ======'
elif vDocType == 'thesis':
    vDokuTemplate = '====== '+vAuthorAPA[0]+' ('+vYear+') '+vTitleHeading+' ======'
else:
    vDokuTemplate = '====== '+vAuthorDisplay+' ('+vYear+') '+vTitleHeading+' ======'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Use Author name to create display for citation & links
# --------------------------------------------------------
if len(vAuthorChicago) == 0:
    vAuthorDisplay = ''
elif len(vAuthorChicago) == 1:
    vAuthorDisplay = '[[author:'+vAuthorLink[0]+'|'+vAuthorChicago[0]+']]'
elif len(vAuthorChicago) > 5:
    vAuthorDisplay = '[[author:'+vAuthorLink[0]+'|'+vAuthorChicago[0]+']] et al.'
else:
    vAuthorDisplay = '[[author:'+vAuthorLink[0]+'|'+vAuthorChicago[0]+']]'
    for x in range(1, len(vAuthorChicago)):
        vAuthorDisplay+=', [[author:'+vAuthorLink[x]+'|'+vAuthorChicago[x]+']]'

# --------------------------------------------------------
# Show heading for abstract (if there is an abstract)
# --------------------------------------------------------
if len(vAbstract) > 0:
    vDokuTemplate = '===== Abstract ====='
    print (vDokuTemplate)

# --------------------------------------------------------
# Show full title if it was shortened in the heading
# --------------------------------------------------------
if len(vTitle) > 80:
    vDokuTemplate = '== '+vTitle+' =='
    print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Show abstract (if there is one)
# --------------------------------------------------------
if len(vAbstract) > 0:
    vDokuTemplate = '//'+vAbstract+'//'
    print (vDokuTemplate,'\n')
   
# --------------------------------------------------------
# Citation
# --------------------------------------------------------
vDokuTemplate = '^ Citation | '

# Citation: Book
if vDocType == 'book':
    # If no author show editors
    if vAuthor == '':
        vAuthorDisplay+=' (Eds.).'
    vDokuTemplate+=vAuthorDisplay+' ('+vYear+'). //'+vTitle+'//'
    if not vEdition == '':
        vDokuTemplate+=' ('+vEdition+')'
    if not vAddress == '':
        vDokuTemplate+='. '+vAddress
    if not vPublisher == '':
        vDokuTemplate+='. '+vPublisher
    vDokuTemplate+='.'
    if not vDoi == '':
        vDokuTemplate+=' doi:'+vDoi
# Citation: Article
elif vDocType == 'article':
    vDokuTemplate+=vAuthorDisplay+' ('+vYear+'). '+vTitle+'. '+vJournal
    if not vVolume == '':
        vDokuTemplate+=', vol. '+vVolume
    if not vIssue == '':
        vDokuTemplate+=' no. '+vIssue
    if not vPages == '':
        vDokuTemplate+=', pp. '+vPages
    vDokuTemplate+='.'
# Citation: Thesis
elif vDocType == 'thesis':
    vDokuTemplate+=vAuthorDisplay+' ('+vYear+'). //'+vTitle+'//'
    vDokuTemplate+=' ('
    if not vType == '':
        vDokuTemplate+=vType+' thesis, '
    if not vSchool == '':
        vDokuTemplate+=vSchool+', '
    if not vAddress == '':
        vDokuTemplate+=vAddress
    vDokuTemplate+=').'
# Citation: All other types
else:
    vDokuTemplate+=vAuthorDisplay+' ('+vYear+'). '+vTitle+'.'
    
# Citation: Show the URL or ASIN (for Kindle books) or DOI
vDokuTemplate+=' ^ '
if len(vAsin) > 0:
    vDokuTemplate+='[['
    vDokuTemplate+='http://www.amazon.com/dp/'+vAsin
    vDokuTemplate+='|ASIN]]'
elif len(vUrl) > 0:
    vDokuTemplate+='[['
    vDokuTemplate+=vUrl
    vDokuTemplate+='|URL]]'
elif len(vDoi) > 0:
    vDokuTemplate+='[['
    vDokuTemplate+='http://dx.doi.org/'+vDoi
    vDokuTemplate+='|DOI]]'
else:
    # Citation: PDF File name (TODO: Create as a link to the PDF file)
    #vDokuTemplate+=vFile
    vDokuTemplate+=vDocType

vDokuTemplate+=' ^'
print (vDokuTemplate)

# --------------------------------------------------------
# Display BibText as hidden
# --------------------------------------------------------
vDokuTemplate = '<hidden BibTex entry for this '+vDocType+': >'
print (vDokuTemplate)
vDokuTemplate = '<code>'
print (vDokuTemplate)
vDokuTemplate = vBibTex
print (vDokuTemplate)
vDokuTemplate = '</code>'
print (vDokuTemplate)
vDokuTemplate = '</hidden>'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Show Tags (if they are present)
# --------------------------------------------------------
if len(vMendeleyTags) > 0:
    s = vMendeleyTags
    # Replace double space with space
    s = s.replace("  "," ")
    # Replace space with -
    s = s.replace(" ","-")
    # Replace comma with space
    s = s.replace(","," ")
    # Make lower case
    s = s.lower()
    vDokuTemplate = '{{tag>'+s+'}}'
    print (vDokuTemplate,'\n')

# --------------------------------------------------------
# For books and theses: Add an overview section for Table of Contents etc.
# --------------------------------------------------------
if vDocType == 'book' or vDocType == 'thesis':
    vDokuTemplate = '{{page>'+vDocType+':overview:'+vCiteKey+'}}'
    print (vDokuTemplate,'\n')
    
# --------------------------------------------------------
# Key ideas
# --------------------------------------------------------
vDokuTemplate = '===== Key ideas ====='
print (vDokuTemplate)
vDokuTemplate = '{{page>'+vDocType+':keyideas:'+vCiteKey+'}}'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Notes
# --------------------------------------------------------
vDokuTemplate = '{{page>'+vDocType+':notes:'+vCiteKey+'}}'
print (vDokuTemplate,'\n')
    
# --------------------------------------------------------
# Images
# --------------------------------------------------------
vDokuTemplate = '{{page>'+vDocType+':images:'+vCiteKey+'}}'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Kindle notes (if they exist and only for books)
# --------------------------------------------------------
if len(vAsin) > 0:
    vDokuTemplate = '{{page>'+vDocType+':kindle:'+vCiteKey+'}}'
    print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Links here
# --------------------------------------------------------
vDokuTemplate = '===== Links here ====='
print (vDokuTemplate)
vDokuTemplate = '{{backlinks>.}}'
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# Keywords
# --------------------------------------------------------
vDokuTemplate = '== Keywords: =='
print (vDokuTemplate,'\n')
# Replace comma with comma space
s = vKeywords
s = s.replace(",",", ")
vDokuTemplate = s
print (vDokuTemplate,'\n')

# --------------------------------------------------------
# References
# --------------------------------------------------------
vDokuTemplate = '{{page>'+vDocType+':references:'+vCiteKey+'}}'
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

# Print No cache for debugging
#print ('~~NOCACHE~~\n\r', end=' ')

# --------------------------------------------------------
# Close the input file
# --------------------------------------------------------
fin.close()
