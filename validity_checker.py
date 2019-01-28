#!/usr/bin/python3

import argparse
import sys

parser = argparse.ArgumentParser(description='y++ compiler')
parser.add_argument('-fpermissive', action='store_true')
parser.add_argument('files', nargs='*')


args = parser.parse_args()

print(args)

if args.fpermissive:
    print('-fpermissive!!!??? What are you? Reform?')
    sys.exit(1)
sys.exit(0)