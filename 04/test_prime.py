import os
import sys


def is_palindrome(x):
    r = "".join(reversed(x))
    if x == "".join(reversed(x)):
        return True
    else:
        return False

    # if len(x) % 2 == 1:
    #     # print("--")
    #     # print(len(x))
    #     side_len = int((len(x) - 1) / 2)
    #     center_pos = int(side_len + 1)

    #     left_str = x[0:side_len]
    #     center_str = x[center_pos-1:center_pos]
    #     right_str = x[-side_len:]
    #     if left_str == reverse(right_str):
    #         print(x)
    #         # print(x, side_len, center_pos)
    #         # print(left_str, center_str, right_str, reverse(right_str))
    #         # print("palindrome")
    #         # sys.exit()

def reverse(x):
    y = ""
    for i in reversed(x):
        y = y + i
    return y

with open("2T_part1.txt","r") as p:
    for row in p:
        x = row.strip()
        if is_palindrome(x):
            print(x + ",")
        # if row.strip() in my_primes:
        #     print(row.strip(), "is prime")
        # else:
        #     print(row.strip(), "is not prime")

