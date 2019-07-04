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
    '😐': "\n\tENDIF ",
    '💰': " JUMPMARKER ",
    '🖋': " FUNC ",
    '💰🎌🏁💠🔶🚩': "to_marker_001",
    '💰🎌🏁🚩🔶💠': "to_marker_002",
    '💰🎌🚩💠🔶🏁': "to_marker_003",
    '💰🏁💠🔶🚩🎌': "to_marker_004",
    '💰🏁🚩🎌💠🔶': "to_marker_005",
    '💰💠🎌🏁🚩🔶': "to_marker_006",
    '💰💠🏁🎌🔶🚩': "to_marker_007",
    '💰💠🔶🎌🚩🏁': "to_marker_008",
    '💰🔶🎌🚩💠🏁': "to_marker_009",
    '💰🔶🚩💠🏁🎌': "to_marker_010",
    '💰🚩💠🎌🔶🏁': "to_marker_011",
    '💰🚩🔶🏁🎌💠': "to_marker_012",
    '🖋🎌🏁💠🔶🚩': "\n\nmarker_001",
    '🖋🎌🏁🚩🔶💠': "\n\nmarker_002",
    '🖋🎌🚩💠🔶🏁': "\n\nmarker_003",
    '🖋🏁💠🔶🚩🎌': "\n\nmarker_004",
    '🖋🏁🚩🎌💠🔶': "\n\nmarker_005",
    '🖋💠🎌🏁🚩🔶': "\n\nmarker_006",
    '🖋💠🏁🎌🔶🚩': "\n\nmarker_007",
    '🖋💠🔶🎌🚩🏁': "\n\nmarker_008",
    '🖋🔶🎌🚩💠🏁': "\n\nmarker_009",
    '🖋🔶🚩💠🏁🎌': "\n\nmarker_010",
    '🖋🚩💠🎌🔶🏁': "\n\nmarker_011",
    '🖋🚩🔶🏁🎌💠': "\n\nmarker_012",
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

