#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Describe what this script does."""
import argparse
import logging
import sys
from typing import List, Optional

__author__ = 'Sergey M'
__description__ = __doc__
__email__ = 'tz4678@gmail.com'
__LICENSE__ = 'MIT'
__version__ = '0.1.0'


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-i',
        '--input',
        default=sys.stdin,
        help='input file',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        '-o',
        '--output',
        default=sys.stdout,
        help='output file',
        type=argparse.FileType('w'),
    )
    parser.add_argument(
        '-v',
        '--verbosity',
        action='count',
        default=0,
        help='increase output verbosity: 0 - warning, 1 - info, 2 - debug',
    )
    parser.add_argument(
        '--version', action='version', version=f'v{__version__}'
    )
    parser.set_defaults(func=run)
    args = parser.parse_args(argv)
    return args, parser


def run(args: argparse.Namespace) -> Optional[int]:
    pass


def main(argv: Optional[List[str]] = None) -> Optional[int]:
    args = parse_args(argv)
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    log_level = levels[min(args.verbosity, len(levels) - 1)]
    logging.basicConfig(level=log_level, stream=sys.stderr)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        logging.warning("Ctrl+C pressed. Exiting...")
    except Exception as e:
        logging.critical(e, exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
