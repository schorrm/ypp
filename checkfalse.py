#!/usr/bin/python3
import sys
import subprocess

gemara = '''Rabbi Yehoshua ben Levi said: A person should never express a crude matter, as the formulation of a verse was distorted by the addition of eight letters rather than have it express a crude matter, as it is stated: “From the pure animals and from the animals that are not pure [asher einena tehora]” (Genesis 7:8).'''
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

    if ('FLAG_FOUND_FALSE' in line) and user_code:
        print('Aveira in {0}:{1}'.format(file,line_num))
        subprocess.call(["sed", "-n", "{0}p".format(line_num),  file])
        print('Zogt di Gemoreh:')
        print(gemara)
        print('You used "false" in your code. Please use something more suitable to torahdig hashkafos, like "nisht emes". Shkoyach.')
        sys.exit(1)

    line_num += 1
sys.exit(0)