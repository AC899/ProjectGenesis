# This is a sample Python script.

import random
import string


def passwordgen(input):
    n = int(input("Enter chars"))
    if n >=16:
        return("The maximum character limit for passwords is 16 - please try again")
    else:
        return(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n)))


print(passwordgen(input))