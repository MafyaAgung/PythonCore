#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'trimPhonenumber' function below.
#
# The function is expected to return a STRING.
#

def trimPhonenumber(phone):
    # Write your code here
    return phone.replace('-', '')

if __name__ == '__main__':
    phone = input().strip()
    result = trimPhonenumber(phone)
    print(result)