#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahmoud
"""


import re
import argparse


def read_in_chunks(file,chunk_size):
    """
    Split binary file into chunks and yield it

    Parameters
    ----------
    file :  io. BufferedReader, buffered binary stream providing access to a the pdf file
    chunk_size : int, size of the buffered binary chunks after the spliting operation
    
    """
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data
        
        
def get_offset(pattern,chunk):
    """
    Get offset of a chunk in the binary file

    Parameters
    ----------
    pattern : bytes, pattern to look for. here b'%%EOF' for the end of file
    chunk : bytes, chunk in the binary file of size 512 (chunk size can be modified)

    Returns
    -------
    chunk_offset : int, offset
    """
    occurences = re.finditer(pattern,chunk) # look for pattern
    chunk_offset = -1 # if there is no occurences
    for j,occ in enumerate(occurences):
        chunk_offset = occ.start()
    return chunk_offset



def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help='path to the pdf file')
    args = parser.parse_args()
    return args


def main():
    """main function."""
    pattern = b'%%EOF'
    chunk_size = 512
    args = parse_args()
    filename = args.path # path of pdf file
    file = open(filename, 'rb')
    
    for j,chunk in enumerate(read_in_chunks(file,chunk_size)):
        chunk_offset = get_offset(pattern, chunk)
        if chunk_offset!=-1:
            offset = j*chunk_size + chunk_offset
    file.close()
    print ("The offset is {}".format(offset))




if __name__ == "__main__":    
    main()