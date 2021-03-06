import argparse
from gendiff.gen_diff import generate_diff

parser = argparse.ArgumentParser(prog='gendiff', usage='%(prog)s [-h] [-f FORMAT] first_file second_file',
                                 description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format',
                    help='set format of output',
                    )

args = parser.parse_args()
print(generate_diff(args.first_file, args.second_file))
