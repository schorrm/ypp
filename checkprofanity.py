#!/usr/bin/python3
import sys
import subprocess

msg1 = '''The reason nivul peh is called Avi Avos HaTumah by the Shla HaKadosh is that such activity undermines the holiness of Klal Yisroel, both of oneself and of others.  In fact, the Gemorah in Kesuvos (5b) instructs the others just how they should react.  The Gemorah states that fingers were created like straight tent pegs for a reason – so that someone who hears Nivul Peh can place his fingers in his ears to blot out the sound.'''
msg2 = '''The Midrash tells us that the Jews in Egypt reached the 49th level of impurity, but even then, they did not succumb so low as to curse (Psikta Zuta Shmos 6:10).  They did not change their language implies, according to the Midrash, that they did not change their manner of speech either.  We see how serious such activity truly is.'''

files = sys.argv
user_code = False
line_num = 1
for line in sys.stdin:
    if line[0] == '#':
        # handle directive
        file = line.split()[2][1:-1]
        user_code = file in files
        if user_code:
            line_num = int(line.split()[1]) - 1

    if 'PROFANITY_RESERVED' in line:
        print('Aveira! Nivul Peh in {0}:{1}, rachmana litzlan.'.format(file, line_num))
        print(msg1)
        print(msg2)
        sys.exit(1)

    line_num += 1
sys.exit(0)
