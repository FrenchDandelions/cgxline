import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
depth=0
inside_quote=0
value_started=0
coma_printed=0
s=""
for i in range(n):

    cgxline = input()
    line=""
    word=""

    for x,i in enumerate(cgxline):

        if not inside_quote and i == "(":
            if len(word):
                s+="    "*(depth)+word+"\n"
                word=""
            s+="    "*depth + "("+"\n"
            depth+=1
            continue

        elif not inside_quote and i == ")":
            if len(word):
                s+="    "*(depth)+word+"\n"
                word=""
            coma=""
            if x + 1 < len(cgxline) and cgxline[x+1] == ";":
                coma = ";"
                coma_printed=1
            depth-=1
            s+="    "*depth + ")"+coma+"\n"
            continue

        if inside_quote:
            word+=i
            if i == "\'":
                inside_quote = 0
            continue

        elif not inside_quote and i==";":
            if coma_printed:
                coma_printed=0
                continue
            s+="    "*(depth)+word+";"+"\n"
            word=""
        
        elif i.isspace(): continue

        else:
            word+=i
            if i == "\'":
                inside_quote=1
    if len(word):
        s+="    "*(depth)+word+"\n"
print(s,end="")