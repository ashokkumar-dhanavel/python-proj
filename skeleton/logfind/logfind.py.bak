import mmap
import os
import argparse
import re

root_dir = '/home/linuxuser/work/python-proj'
ROOT_DIR = '/home/linuxuser/work/python-proj'


def get_list_of_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(ROOT_DIR, f))]


def scan_file(line, words):    
    for word in words.split(' '):        
        if re.search(word, line) is None:
            return False
    return True

if __name__ == "__main__":
    file_list = []
    parser = argparse.ArgumentParser(description = 'Find the String')
    parser.add_argument('-s', help="String to find")    
    args = parser.parse_args()
    search_strings = args.s    
    files = get_list_of_files(ROOT_DIR)
    for file in files:
        with open(os.path.join(ROOT_DIR,file)) as f:
            if(scan_file(f.read(), search_strings)):
                file_list.append(file)
    print file_list
        

    

    
    
   
