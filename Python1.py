# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S4s3dwC9IbWw8ArO6YktCSjOS8oAGa68
"""

def add(a,b):
  print("The sum is: ",a+b)

def sub(a,b):
  print("The difference is: ",a-b)

def mul(a,b):
  print("The product is: ",a*b)

def div(a,b):
  print("The division is: ",a/b)
def rem(a,b):
  print("The remainder is: ",a%b)

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
op=input("Choose the arithematic operation: ")

if(op=='+'):
  add(a,b)

elif(op=='-'):
  sub(a,b)

elif(op=='*'):
  mul(a,b)

elif(op=='/'):
  div(a,b)

elif(op=='%'):
  rem(a,b)
  
else:
  print("Not valid")