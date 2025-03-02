from src.characterStream import CharacterStream as stream
from src.reader import Reader

import argparse

parser = argparse.ArgumentParser(description='Interpreteur List')
parser.add_argument('-f', '--file', help='fichier lisp', required=True)
args = parser.parse_args()

code = open(args.file, "r").read()

charStream = stream(code)

reader = Reader()

content = reader.read(charStream)

print(content)