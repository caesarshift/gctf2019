import os

ops = {
    '🍡': "\nadd ",
    '🤡': "\nclone ",
    '📐': "\ndivide ",
    '😲': "\nif_zero ",
    '😄': "\nif_not_zero ",
    '🏀': "\njump_to ",
    '🚛': "\nload ",
    '📬': "\nmodulo ",
    '⭐': "\nmultiply ",
    '🍿': "\npop ",
    '📤': "\npop_out ",
    '🎤': "\nprint_top ",
    '📥': "\npush ",
    '🔪': "\nsub ",
    '🌓': "\nxor ",
    '⛰': "\njump_top ",
    '⌛': "\nexit ",
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
    '🥇': " accumulator1 ",
    '🥈': " accumulator2 ",
    '✋': " STOP?\n",
    '😐': " UNKNOWN? ",
    '💰': " MARKER? ",
    '🖋': " MARKER? ",
    '💰🎌🏁💠🔶🚩': "__ADDRESS-001__",
    '💰🎌🏁🚩🔶💠': "__ADDRESS-002__",
    '💰🎌🚩💠🔶🏁': "__ADDRESS-003__",
    '💰🏁💠🔶🚩🎌': "__ADDRESS-004__",
    '💰🏁🚩🎌💠🔶': "__ADDRESS-005__",
    '💰💠🎌🏁🚩🔶': "__ADDRESS-006__",
    '💰💠🏁🎌🔶🚩': "__ADDRESS-007__",
    '💰💠🔶🎌🚩🏁': "__ADDRESS-008__",
    '💰🔶🎌🚩💠🏁': "__ADDRESS-009__",
    '💰🔶🚩💠🏁🎌': "__ADDRESS-010__",
    '💰🚩💠🎌🔶🏁': "__ADDRESS-011__",
    '💰🚩🔶🏁🎌💠': "__ADDRESS-012__",
    '🖋🎌🏁💠🔶🚩': "__ADDRESS-013__",
    '🖋🎌🏁🚩🔶💠': "__ADDRESS-014__",
    '🖋🎌🚩💠🔶🏁': "__ADDRESS-015__",
    '🖋🏁💠🔶🚩🎌': "__ADDRESS-016__",
    '🖋🏁🚩🎌💠🔶': "__ADDRESS-017__",
    '🖋💠🎌🏁🚩🔶': "__ADDRESS-018__",
    '🖋💠🏁🎌🔶🚩': "__ADDRESS-019__",
    '🖋💠🔶🎌🚩🏁': "__ADDRESS-020__",
    '🖋🔶🎌🚩💠🏁': "__ADDRESS-021__",
    '🖋🔶🚩💠🏁🎌': "__ADDRESS-022__",
    '🖋🚩💠🎌🔶🏁': "__ADDRESS-023__",
    '🖋🚩🔶🏁🎌💠': "__ADDRESS-024__",
}

with open("program","r") as infile:
    for row in infile:
        # print("-"*80)
        # print(row.strip().split(" "))
        line = ""
        for item in row.strip().split(" "):
            if item in ops:
                if ops[item] in ['0','1','2','3','4','5','6','7','8','9',]:
                    line = line + ops[item]
                else:
                    line = line + ops[item] + " "
            else:
                line = line + " \n>" + item + "<\n "
        print(line)

