import math
import os
import random
import re
import sys



def count_apple_and_orange(s,t,a,b,ap, org):
    new_ap = filter(lambda x: (x >=s and x <=t),map(lambda x:x+a, ap))
    new_org = filter(lambda x: (x >=s and x <=t),map(lambda x:x+b, org))

    return len(new_ap), len(new_org)

    

def main():
    s = 7
    t = 11
    a = 5
    b = 15
    apple = [-2, 2, 1]
    orange = [5, -6]

    ap, og = count_apple_and_orange(s,t,a,b,apple,orange)
    print(ap)
    print(og)


if __name__ == "__main__":
    main()
