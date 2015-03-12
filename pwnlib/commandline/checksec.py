#!/usr/bin/env python2
import argparse
import sys

from pwn import *

from . import common

parser = argparse.ArgumentParser(
    description = 'Check binary security settings'
)

parser.add_argument(
    'elf',
    nargs='+',
    type=file,
    help='Files to check'
)

def main():
    args   = parser.parse_args()
    for f in args.elf:
        with context.local(log_level='error'):
            e = ELF(f.name)
        log.info("%s (%s-bit %s %s-endian)\n%s" %
            (e.path, e.elfclass, e.arch, e.endian, e.checksec()))

if __name__ == '__main__': main()