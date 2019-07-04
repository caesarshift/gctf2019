#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

ops = {
    '🍡': "add",
    '🤡': "clone",
    '📐': "divide",
    '😲': "if_zero",
    '😄': "if_not_zero",
    '🏀': "jump_to",
    '🚛': "load",
    '📬': "modulo",
    '⭐': "multiply",
    '🍿': "pop",
    '📤': "pop_out",
    '🎤': "print_top",
    '📥': "push",
    '🔪': "sub",
    '🌓': "xor",
    '⛰': "jump_top",
    '⌛': "exit",
    "0️⃣":"0",
    "1️⃣":"1",
    "2️⃣":"2",
    "3️⃣":"3",
    "4️⃣":"4",
    "5️⃣":"5",
    "6️⃣":"6",
    "7️⃣":"7",
    "8️⃣":"8",
    "9️⃣":"9",
    '🥇': "accumulator1",
    '🥈': "accumulator2",
    '✋': "LOADEND",
    '😐': "ENDIF",
    '💰': "JUMPMARKER",
    '🖋': "func"
}


rom = []

with open("program","r", encoding="utf8") as infile:
    for row in infile:
        # print("-"*80)
        # print(row.strip().split(" "))
        line = ""
        for item in row.strip().split(" "):
            if item in ops:
                line = line + ops[item] + " "
            else:
                line = line + " >" + item + "< "
        print(line)