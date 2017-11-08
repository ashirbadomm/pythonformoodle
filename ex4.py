inputFileName= input("Enter input file name that is full of comments? ")
outputFileName= input("Enter the file name to output too? ")
try:
    inFile= open(inputFileName,'r+')
    inlines = inFile.readlines()
    inFile.close()
    outFile= open(outputFileName,'w+')
except (OSError, IOError,NameError) as e:
    print (e)
for line in inlines:
    if(line[0:1]=='#'): continue
    else: outFile.write(line)
outFile.close()
