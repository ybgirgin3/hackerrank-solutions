from collections import namedtuple
# ID, marks, class and name
# order of these is not important

# calc average of the class

ead input from STDIN. Print output to STDOUT
from collections import *
N,students= input(), namedtuple('students',raw_input().split())
stud=  [students(*raw_input().split()) for i in range(N)]                 #passed string of input as a single key
print sum([float (i.MARKS) for i in stud]) /N

   
