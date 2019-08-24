#!/usr/bin/env python3

import argparse
from lib.banner import __version__

parser = argparse.ArgumentParser(usage='%(prog)s -n NUMBER [OPTIONS...]')

parser.add_argument('-n', '--number', dest='number', type=str,
                    help='The phone number to scan.')

parser.add_argument('-i', '--input', dest="input_file", type=argparse.FileType('r'),
                    help='Phone number list to scan.')

parser.add_argument('-o', '--output', dest="outputfile", type=argparse.FileType('w'),
                    help='Output to save scan results.')

parser.add_argument('-s', '--scanner', metavar="scanner", default="all", type=str,
                    help='The scanner to use.')

parser.add_argument('--recon', action='store_true',
                    help='Launch custom format reconnaissance.')

parser.add_argument('--no-ansi', action='store_true',
                    help='Disable colored output.')

parser.add_argument('-u', '--update', action='store_true',
                    help='Update Phonia Toolkit.')

parser.add_argument('--info', action='store_true',
                    help='Show Phonia Toolkit credits.')

args = parser.parse_args()
