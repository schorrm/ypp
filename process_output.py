#!/usr/bin/python3
import sys
import subprocess

for line in sys.stdin:
    if 'error:' in line:
        base, err, text = line.partition('error:')
        if 'muktzeh' in text:
            print("You're a Muktzeh Boy!")
        print (base + 'aveira r"l:' + text, end='')
    else:
        print(line, end='')