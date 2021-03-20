""
#assignment 2.3
hrs = input("Enter Hours:")
hrs=int(hrs)
rate=2.75
pay=hrs*rate
print("Pay:",pay)
#assignment 3.1
hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate")
r = float(rate)
if h <= 40.0:
   print(h*r)
else:
  nh=h-40
  nr=r*1.5
  print((nh*nr)+(40*r))


#assignment 3.3
score = input("Enter Score: ")
score = float(score)

if score >= 1.1:
  print("value out of range(too high)")
elif score >= 0.9:
  print("A")
elif score >=0.8:
  print("B")
elif score >=0.7:
  print("C")
elif score >=0.6:
  print("D")
elif score < 0.6:
  print("F")
else: 
  print("value out of range(too low)")


#Assignment 4.6
def computepay(h,r):
  if h <= 40.0:
   return(h*r)
  else:
    nh=h-40
    nr=r*1.5
    return((nh*nr)+(40*r))


hrs = input("Enter Hours: ")
hrs=int(hrs)
rate = input ("Enter Rate: ")
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)


#Assignment 5.2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
      break
    try:
      num=int(num)
    except:
      print("Invalid input")
      continue
    if largest is None:
      largest = num
      smallest = num
    elif num > largest:
      largest = num
    elif num < smallest:
      smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)


#assignment 6.5
text = "X-DSPAM-Confidence:  0.8475"
num = text.find("0")
textslice = text[num:]
textslice = float(textslice)
print(textslice)


#assignment7.1
fname = input("Enter file name: ")
fhandle = open(fname)
for line in fhandle:
  line = line.rstrip()
  line = line.upper()
  print(line)


#assignment7.2
fname = input("Enter file name: ")
fhandle = open(fname)

count=0
total=0

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") :       continue
    count = count+1
    ipos = line.find(":")
    value = line[ipos+2:]#starts 2indexs beyond the ipos
    value = value.rstrip()#strips the white space and\n
    value = float(value)  
    total = total+value
average=total/count 
 
print("Average spam confidence:",average)

#personal 1
uInput = input("type in the file name: ")
uSearch = input("search for starting with: ")
fhandle = open(uInput)
msg = "card number: "
count=0
for line in fhandle:
  if not line.startswith(uSearch):
    continue # be wary of this indent here
  ipos = line.find("IRD")
  IRDnum = line[ipos:ipos+7]
  print(msg,IRDnum)
  count = count+1
print("line count",count)

#personal 2
myVar ="UNIVERSITY OF MICHIGAN"
print(myVar[::2])#slice from start to end every 2 places
print(myVar.count("I"))#finds and counts the number of times the value is in a string


#Assignment 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  line = line.rstrip()
  words = line.split(" ")
  for w in words:
    if w not in lst:
      lst.append(w)
lst.sort()
print(lst)


#Assignment 8.5
fname = input("Enter file name: ")#mbox-short.txt
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
  if not line.startswith("From:"):
    continue
  line=line.rstrip()
  words=line.split(" ")
  address = words[1]
  print(address)
  count=count+1
print("There were", count, "lines in the file with From as the first word")


#assignment9.4
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
file = dict()

for line in handle:
  if not line.startswith("From:"):
    continue
  line=line.rstrip()
  words=line.split(" ")
  address = words[1]
  file[address]=file.get(address,0)+1
  
bigcount = None
bigword = None
for word,count in file.items():
  if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count
print(bigword,bigcount)

#assignment 10.1
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

file = dict()

for line in handle:
  if not line.startswith("From "): #note the space to stop From: being added
    continue
  line=line.rstrip()
  words=line.split(" ")
  timeStamp=words[6].split(":")
  file[timeStamp[0]]=file.get(timeStamp[0],0)+1

lst=list()
for k,v in file.items():
  item=(k,v)
  lst.append(item)
lst=sorted(lst)

for k,v in lst:
  print(k,v)



#assignment 11
import re
fh = open("regex_sum_1150582.txt")
total=0
for line in fh:
  foundNum = re.findall('[0-9]+',line)
  
  for num in foundNum:
    total+=int(num)
  #secound for loop adds each number found
  


print (total)


#connecting to a web server with python
import socket

mySock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(("data.pr4e.org",80))

cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mySock.send(cmd)

while True:
  data = mySock.recv(512)
  if(len(data)<1):
    break
  print(data.decode())
mySock.close()

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

sitename = input("enter your URL here: ")
    #EX link. data.pr4e.org/romeo.txt
filehandler = urllib.request.urlopen("http://"+sitename)
#for line in filehandler:
#   print(line.decode().strip())

counts = dict()
for line in filehandler:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)


url = input("enter a url : ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
#http://www.dr-chuck.com/page1.htm

tags = soup("a")
for tag in tags:
    print(tag.get("href",None))

"""
