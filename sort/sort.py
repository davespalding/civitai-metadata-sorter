"""Sorting script"""
import shutil

from datetime import datetime


DELIMITER = '---------------------------------------'


class MetadataBlock:
    """Metadata file block object"""
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def name(self):
        """Get name"""
        return self._name

    @property
    def content(self):
        """Get content"""
        return self._content


def read_txt(path):
    """Open and return file content as a list"""
    with open(path, 'r', encoding='utf-8') as fp:
        return fp.readlines()


def write_txt(path, list_obj):
    """Write list object to file"""
    with open(path, 'w', encoding='utf-8') as fp:
        for line in list_obj:
            fp.writelines(line)


def list_to_datablocks(unsorted_list):
    """Converts text list to MetadataBlock list"""
    datablocks = []
    buffer = []

    for line in unsorted_list:
        if line == '\t\n':  # do some whitespace cleaning
            buffer.append('\n')
            continue

        buffer.append(line)

        if line.startswith(DELIMITER):
            datablocks.append(MetadataBlock(buffer[0], buffer))
            buffer = []

    return datablocks


def datablocks_to_list(blocks):
    """Write list of MetadataBlocks to file"""
    return [line for block in blocks for line in block.content]


def sort_datablocks(blocks):
    """Sort list of MetadataBlocks by name"""
    return list(sorted(blocks, key=lambda d: d.name.lower()))


def check_list_lengths(sourcel, sortedl):
    """Compares lengths of two lists"""
    return len(sourcel) == len(sortedl)


def backup_file(path):
    """Backup target file"""
    suffix = datetime.now().strftime("%Y%m%d%H%M%S")
    target = f'{path.split(".")[0]}-{suffix}.txt'
    shutil.copy(path, target)


def main(args):
    """Main function"""
    source_list = read_txt(args.file)
    blocks_list = list_to_datablocks(source_list)
    sorted_blocks = sort_datablocks(blocks_list)
    sorted_list = datablocks_to_list(sorted_blocks)

    if not check_list_lengths(source_list, sorted_list):
        raise ValueError('Input and output lengths are not equal!')

    if args.backup:
        backup_file(args.file)

    write_txt(args.file, sorted_list)

    print(f'Wrote {len(sorted_blocks)} entries to file!')
