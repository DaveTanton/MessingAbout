import urllib.request, urllib.parse, urllib.error

sitename=input("enter your URL here: ")
    #EX link. data.pr4e.org/romeo.txt
filehandler=urllib.request.urlopen("http://"+sitename)
for line in filehandler:
    print(line.decode().strip())
    
#this is an exercise from coursera "Using Python to Access Web Data"
# modified to allow user to type in the data

#suing a real website will return the html of the website

counts = dict()
for line in filehandler:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)
