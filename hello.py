# -*- coding: utf-8 -*-
from fibo import *
fib(2000)
print("räksmörgås")
print("Stefans nästan första Python script!\nNy radjävel.")
# str.encode(encoding='utf-8', errors='strict')
dinTid = 0
while (dinTid <= 0):
   dinTid = float(input("Ge din tid:") )
   if (dinTid <= 0):
      print("Tiden måste vara mer än noll")

print("Din tid:", dinTid)
namn = input("Vilken ost vill du ha? ")
#print("Hej " , namn)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop(namn, "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
#Comment
