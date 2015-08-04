"""Requirements:
- Please use advanced scripting language (either Python or Ruby is
preferred)
- Please implement a stand-alone script that does the following function:
input:
taking an argument “root_dir” as a root directory to start traversing
taking an argument “keyword” as a regular expression for example (
“^[a-zA-Z]+_TESTResult.*” ) to detect a file contains an interested string
Functionality:
script should recursively walk the “root_dir” and detect all the files under
that dir which contains “keywords” and count the number of files for each
sub dir. All results should be saved in a key:value array with key being
subdir string, and value being counts of files containing the keyword
Output:
An output array of all the data, for example {’a/b’: 6, ’a/b/c’: 7,
‘/a/b/c/d’:0}
(Bonus) An output graph with a plot with X as subdir name string, Y as count
values.
Tests:
Please design a set of tests for the above routine you just wrote, how many
ways can break the routine above and how many ways can you test the routine

Candidate’s code will be evaluated based on the following criteria:
- Coding style - module name, class name, functions, clarity, data
structure, algorithms etc.
- Argument handling - what module do you use for argument that’s easy to
expend, exception checking etc.
- Portability - think about how your program would behavior for various OS
systems
- Scalability - how do you make your routine scalable, multithreading,
parallel computing etc.
- Reliability - how robust can you make the routine that under any env it
won’t crash - either exit gracefully with error message or complete what you
can"""
import os
import re

class FileLookUp(object):
    def __init__(root_dir, keyword, kwy_case_sensitive=True):
        self.root_dir = root_dir
        if not kwy_case_sensitive:
            self.keywrod = keywrod.lower()
        else:
            self.keywrod = keyword

    def file_lookup(dir):
        for root, dirs, files in os.walk(dir)
        
        
        
    
        



