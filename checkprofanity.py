#!/usr/bin/python3
import sys
import subprocess

l1 = '''The reason nivul peh is called “Avi Avos HaTumah by the Shla HaKadosh is that such activity undermines the holiness of Klal Yisroel, both of oneself and of others.  In fact, the Gemorah in Kesuvos (5b) instructs the others just how they should react.  The Gemorah states that fingers were created like straight tent pegs for a reason – so that someone who hears Nivul Peh can place his fingers in his ears to blot out the sound.'''
l2 = '''The Midrash tells us that the Jews in Egypt reached the 49th level of impurity, but even then, they did not succumb so low as to curse (Psikta Zuta Shmos 6:10).  They did not change their language implies, according to the Midrash, that they did not change their manner of speech either.  We see how serious such activity truly is.'''

for line in sys.stdin:
    if 'PROFANITY_RESERVED' in line:
        print('Aveira! Nivul Peh.')
        print(l1)
        print(l2)
        sys.exit(1)
sys.exit(0)