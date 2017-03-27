import urllib.request
infile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
ifh=infile.read().decode()

words = ifh.split()

print("Number of words in the url: is",len(words))