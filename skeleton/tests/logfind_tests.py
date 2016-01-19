import os
import sys
from nose.tools import *
from logfind import logfind



class test_logfind(object):
    
    def setup(self):        
        self.search_correct_string = "ashok"
        self.search_incorrect_string = "hello"
        self.path = "./tests/log1"       
        
    def teardown(self):
        print "TEAR DOWN!"
        
    def test_get_current_dir_files(self):
        list_files = logfind.get_current_dir_files(self.path)
        assert list_files[0] == "test1.txt"

    def test_get_scan_files(self):
        list_files = logfind.get_scan_files(self.path)
        assert list_files[0] == "test1.txt"
        
    def test_get_scan_files_incorrect(self):
        list_files = logfind.get_scan_files(self.path)
        assert_not_equal(list_files[0],"test1.py")
    
    def test_scan_files(self):
        isSearchString = ""
        list_files = logfind.get_scan_files(self.path)
        with open(os.path.join(self.path, list_files[0])) as f:
            isSearachString = logfind.scan_file(f.read(), self.search_correct_string)
        assert_equal(True, isSearachString)
        
    def test_scan_files_incorrect(self):
        isSearchString = ""
        list_files = logfind.get_scan_files(self.path)
        with open(os.path.join(self.path, list_files[0])) as f:
            isSearachString = logfind.scan_file(f.read(), self.search_incorrect_string)
        assert_equal(False, isSearachString)
    
    def test_print_match_files(self):
        list_files = logfind.get_match_files(self.path, self.search_correct_string)
        print list_files
        assert list_files[0] == "test1.txt"    
