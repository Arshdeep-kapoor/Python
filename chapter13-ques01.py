import os

filename = input("Enter a filename: ").strip()
if os.path.isfile(filename):
    infile = open(filename,"r")
    new_lines=[]
    remove = input("Enter string to be removed: ")
    for line in infile:
        line=line.replace(remove,"")
        new_lines.append(line)
    infile.close()
    outfile = open(filename,"w")
    for line in new_lines:
        outfile.write(line)
    outfile.close()
    print("Done.")
else:
    print("No such file exists in the path you specified")