"""Module main file"""
import argparse

from sort import sort


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='CivitAI metadata file sorter.',
        description='Sort metadata blocks from a CivitAI metadata text file.'
    )
    parser.add_argument('-f', '--file', help='Path to file.', required=True)
    parser.add_argument('-b', '--backup', help='Create backup of target file.',
                        action='store_true')

    arguments = parser.parse_args()
    sort.main(arguments)
