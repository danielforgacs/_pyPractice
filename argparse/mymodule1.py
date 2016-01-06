"""
===========================
learning argparse
===========================

test module
"""


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', help='echo sttring you use here')
args = parser.parse_args()
print(args.echo)
