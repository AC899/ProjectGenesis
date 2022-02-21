# This is a sample Python script.

import random
import array

# maximum number of characters for password generator
lengthofpassword = 12
if lengthofpassword >12:
    print("Maximum number of characters is 12")

#Lists of all possible combinations

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

up_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

hi_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


