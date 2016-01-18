import os
import re
import argparse


ROOT_DIR = '.'
REGEX_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, "logfind")


def get_important_file():
    """
    :return:check for list of files using the regex expression from the configuration file (logfind) or return the
     list of files from the root directory
    """
    regex = ""
    file_list = []
    log_files = get_list_of_files(ROOT_DIR)

    if os.path.exists(REGEX_CONFIG_FILE_PATH):
        with open(REGEX_CONFIG_FILE_PATH) as f:
            for line in f.readlines():
                regex += line[:-1] + "|"
        regex = re.compile(regex[:-1])
        for file in log_files:
            if re.match(regex, file):
                file_list.append(file)
        return file_list
    else:
        return log_files


def get_list_of_files(directory):
    """
    :param directory: root directory path
    :return: list of files from the root directory
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(ROOT_DIR, f))]


def scan_file(line, words):
    """
    :param line: the entire contents of the file
    :param words: list of keywords to search
    :return:returned TRUE if the words are present (uses AND operation
    i.e matches the entire list of words from the files)
    """
    for word in words.split(' '):
        if re.search(word, line) is None:
            return False
    return True


if __name__ == "__main__":
    file_list = []
    parser = argparse.ArgumentParser(description='Find the String from the log files')
    parser.add_argument('s', help="keyword to find from the log files")
    args = parser.parse_args()
    search_strings = args.s
    files = get_important_file()
    # scan the files and append the results to file list
    for file in files:
        with open(os.path.join(ROOT_DIR, file)) as f:
            if (scan_file(f.read(), search_strings)):
                file_list.append(os.path.abspath(os.path.join(ROOT_DIR, file)))

    for file in file_list:
        print file
