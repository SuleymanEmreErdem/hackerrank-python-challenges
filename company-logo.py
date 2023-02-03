#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    dic = {}
    s_set = set(s)
    for item1 in s_set:
        dic[item1] = s.count(item1)
    sorted_dic = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])))
    counter = 0
    for key, value in sorted_dic.items():
        if counter == 3:
            break
        print(key, value)
        counter += 1
