import re

mystring="Python : Dynamically typed, Interpreted language."

match = re.search("interpreted",mystring,re.IGNORECASE)
print(match)
if match:
    print("Start Index :",match.start())
    print("End Index ",match.end())


newstring = "ASP.NET"
match = re.search(".",newstring)
print(match)

newstring = "ASP.NET"
match = re.search("\.",newstring)
print(match)

#re.findall(): returns all non-overlapping matches of pattern in string.
message = "Hello my number is 123456789 and my friend's number is 987654321."
mypattern = "\d+"
match = re.findall(mypattern,message)
print(match)


#re.compile() : we can compile regular expression into pattern objects.
# class [abcde]
myobj = re.compile('[a-e]')
print(myobj.findall("Aye, asaid Mr. Gibenson Stark."))

myobj1= re.compile('\d')
print(myobj1.findall("I went to collage at 11 A.M. on 27th May, 2026"))

myobj2= re.compile('\d+')
print(myobj2.findall("I went to collage at 11 A.M. on 27th May, 2026"))

#\w : any alphanumeric characters
myobj3 = re.compile("\w")
print(myobj3.findall("He said *  in the tech_result."))

myobj4 = re.compile('\w+')
print(myobj4.findall("I went to him at 11 A.M. _ , he said reuslt is five * ."))

myobj5 = re.compile('\W')
print(myobj5.findall("I went to him at 11 A.M. _ , he said reuslt is five * ."))

p = re.compile("ab*")
print(p.findall("ababbaabbb"))

#re.split() : split strings by the occurences of a character or a pattern, uppon finding the pattern
#re.split(pattern,string,maxsplit=0)

print(re.split("\W+","Words, words , words"))
print(re.split("\W+","Word's  words  words"))
print(re.split("\W+","On 12th Jan 2016, at 11:02 AM"))
print(re.split("\d+","On 12th Jan 2026, at 11:02 AM"))

from re import split
print(split("\d+","On 12th Jan 2026, at 11:02 AM",1))

#re.sub() : it looks for the pattern in the string, and replace it with the value if the patttern found
#res.usb(pattern,replacement,string,count=0)
print(re.sub("ub","~","Subject has Uber booked already",flags=re.IGNORECASE))
print(re.sub("ub","~*","Subject has Uber booked already"))
print(re.sub("ub","~","Subject has Uber booked already",count=1,flags=re.IGNORECASE))

#re.subn():same as sub() but it returns number of replacements
print(re.subn("ub","~","Subject has Uber booked already",flags=re.IGNORECASE))
result = re.subn("ub","~","Subject has Uber booked already",flags=re.IGNORECASE)
print(result)
print(type(result))
print(len(result))
print(result[0])

'''
re.search() : either returns None (if pattern doesnot exist, or contains information about the
matching part). it stops after first match.
'''

def findMonthAndDate(string):
    regex = "([a-zA-Z]+) (\d+)" #February 20
    match = re.match(regex,string)

    if match == None:
        print("Not a valid date")
        return
    print(f"Given Date : {match.group(0)}")
    print (f"Month is : {match.group(1)}")
    print(f"Day is : {match.group(2)}")


findMonthAndDate("June 24")
print()
findMonthAndDate("I was born on Feb 20")
