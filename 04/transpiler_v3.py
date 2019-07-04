#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

ops = {
    '🍡': "\n\tADD ",
    '🤡': "\n\tCLONE ",
    '📐': "\n\tDIVIDE ",
    '😲': "\n\tIF_ZERO ",
    '😄': "\n\tIF_NOT_ZERO ",
    '🏀': "\n\tJUMP_TO ",
    '🚛': "\n\tLOAD_INTO ",
    '📬': "\n\tMODULO ",
    '⭐': "\n\tMULTIPLY ",
    '🍿': "\n\tPOP ",
    '📤': "\n\tPOP_OUT ",
    '🎤': "\n\tPRINT_TOP ",
    '📥': "\n\tPUSH_TO_STACK ",
    '🔪': "\n\tSUB ",
    '🌓': "\n\tXOR ",
    '⛰': "\n\tJUMP_TOP ",
    '⌛': "\n\tEXIT ",
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
    '🥇': " acc1 ",
    '🥈': " acc2 ",
    '✋': " LOADEND",
    '😐': " ENDIF ",
    '💰': " JUMPMARKER ",
    '🖋': " FUNC ",
    '💰🎌🏁💠🔶🚩': "FUNC_001",
    '💰🎌🏁🚩🔶💠': "FUNC_002",
    '💰🎌🚩💠🔶🏁': "FUNC_003",
    '💰🏁💠🔶🚩🎌': "FUNC_004",
    '💰🏁🚩🎌💠🔶': "FUNC_005",
    '💰💠🎌🏁🚩🔶': "FUNC_006",
    '💰💠🏁🎌🔶🚩': "FUNC_007",
    '💰💠🔶🎌🚩🏁': "FUNC_008",
    '💰🔶🎌🚩💠🏁': "FUNC_009",
    '💰🔶🚩💠🏁🎌': "FUNC_010",
    '💰🚩💠🎌🔶🏁': "FUNC_011",
    '💰🚩🔶🏁🎌💠': "FUNC_012",
    '🖋🎌🏁💠🔶🚩': "\nDEF FUNC_001",
    '🖋🎌🏁🚩🔶💠': "\nDEF FUNC_002",
    '🖋🎌🚩💠🔶🏁': "\nDEF FUNC_003",
    '🖋🏁💠🔶🚩🎌': "\nDEF FUNC_004",
    '🖋🏁🚩🎌💠🔶': "\nDEF FUNC_005",
    '🖋💠🎌🏁🚩🔶': "\nDEF FUNC_006",
    '🖋💠🏁🎌🔶🚩': "\nDEF FUNC_007",
    '🖋💠🔶🎌🚩🏁': "\nDEF FUNC_008",
    '🖋🔶🎌🚩💠🏁': "\nDEF FUNC_009",
    '🖋🔶🚩💠🏁🎌': "\nDEF FUNC_010",
    '🖋🚩💠🎌🔶🏁': "\nDEF FUNC_011",
    '🖋🚩🔶🏁🎌💠': "\nDEF FUNC_012",
}


ip = 0
with open("program","r") as infile:
    for row in infile:
        line = ""
        for item in row.strip().split(" "):
            ip += 1
            if item in ops:
                if ops[item] in ['0','1','2','3','4','5','6','7','8','9',]:
                    line = line + ops[item]
                else:
                    line = line + ops[item] + " "
                    # line = line +" {%5d} " % ip + ops[item] + " "
            else:
                line = line + " \n>" + item + "<\n "
        print(line)

