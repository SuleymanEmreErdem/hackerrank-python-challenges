#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

if n%2==1:
    print("Weird")
    
if n%2==0:
    if n>=2:
        if n<=5:
            print("Not Weird")
    if n>=6:
        if n<=20:
            print("Weird")
    if n>20:
        print("Not Weird")        
