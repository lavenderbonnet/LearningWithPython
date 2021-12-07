# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/4/2021
# --------------------------------------------------------------------------

# first string
firstString = "abc"
secondString = "def"
string = "cba"
print(string.maketrans(firstString, secondString))

# # example dictionary
# # firstString = "abc"
# secondString = "defghi"
# string = "abc"
# print(string.maketrans(firstString, secondString))


def text_to_words(the_text):
    print(the_text)
    # If you find any of these
    oc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\"
    # Replace them by these
    sc = "abcdefghijklmnopqrstuvwxyz                                          "
    my_substitutions = the_text.maketrans(oc, sc)

    # Translate the text
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    f = open(filename)
    content = f.read()
    f.close()
    wds = text_to_words(content)

    return wds

def unique_word_count(wds):
    
    wds_dic = {}
    for w in wds:
        if w in wds_dic:
            wds_dic[w] += 1
        else:
            wds_dic[w] = 1
    
    print(wds_dic)
    return wds_dic

if __name__ == "__main__":
    book_words = get_words_in_book("AliceInWonderland.txt")
    # print(f"There are {len(book_words)} words in the book,\
        #  and the first 100 words are {book_words[:100]}")
    wds_dic = unique_word_count(book_words)
    print(wds_dic)


