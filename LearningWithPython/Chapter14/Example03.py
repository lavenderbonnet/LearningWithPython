# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/4/2021
# --------------------------------------------------------------------------

import sys
import os

cwd = os.getcwd()
# print(cwd)

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)



def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocab.txt")
print(f"There are {len(bigger_vocab)} words in the vocabulary file. The first few words are {bigger_vocab[:5]}")