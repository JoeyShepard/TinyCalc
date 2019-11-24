import random
import sys

#1234E37 mod 5678E26 = 4.38E28

"""
#Good
k0=1234
e0=37
k1=5678
e1=26

#Good
k0=1234
e0=1
k1=5678
e1=0

#Good
k0=12345678
e0=37
k1=23456789
e1=26

k0=40000000000000000000000000000000
e0=19
k1=70000000000000000000000000000000
e1=4
#Final y is 1E15

k0=40000000000000000000000000000000
e0=19
k1=70000000000000000000000000000000
e1=12
#Final y is 1E7
"""

k0=40000000000000000000000000000000
e0=19
k1=70000000000000000000000000000000
e1=4
#Final y is 1E15


new_e=e0-e1

c=1
e=0
while e<new_e:
  c=(10*c)%k1
  #print(e,"-",c)
  e+=1
  
#(b^e mod m)*k mod m
mantissa=(c*k0)%k1
expmod=int(mantissa)*int(10**e1)

#fastexp
x=10
y=1
n=new_e
if n&1:
  y=x
while n:
  print("x:",x)
  print("x^2:",x*x)
  print("(x^2)%k1:",(x*x)%k1)
  x=(x*x)%k1
  n>>=1
  if n&1:
    y=(y*x)%k1
  print("y:",y)
  print()
fastexp=(y*k0)%k1
fastexp=int(fastexp)*int(10**e1)

#Python
python=(k0*10**e0)%(k1*10**e1)

print()
print(str(k0)+"E"+str(e0)+" mod "+str(k1)+"E"+str(e1))
#print(c,"*",k0,"=",c*k0)
#print("mantissa = (c*k0)%k1 =",(c*k0)%k1)
#print("exponent =",int(10**e1))
print("   expmod = ",expmod)
print("   python = ",python)
print("   fastexp =",fastexp)
print()

sys.exit()
"""

#Try many examples

import random
#import sys

for i in range(10000):
  #Define denominator first
  k1=random.randint(1,999)
  e1=random.randint(1,99)
  #Make numerator exponent larger
  k0=random.randint(1,999)
  e0=e1+random.randint(1,99)

  new_e=e0-e1

  #expmod
  c=1
  e=0
  while e<new_e:
    c=(10*c)%k1
    #print(e,"-",c)
    e+=1
    
  #(b^e mod m)*k mod m
  mantissa=(c*k0)%k1
  #Version calculated here
  calculated=int(mantissa)*int(10**e1)
  #Python's version
  python=(k0*10**e0)%(k1*10**e1)
  print(str(i)+". "+str(k0)+"E"+str(e0)+" mod "+str(k1)+"E"+str(e1))
  print("   expmod =",calculated)
  print("   python =",python)
  if calculated!=python:
    print("   MISMATCH!")
    sys.exit()
  print()
print("Done")

"""

