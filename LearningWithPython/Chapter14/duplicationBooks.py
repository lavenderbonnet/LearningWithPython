# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 12/6/2021
# --------------------------------------------------------------------------


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


def delete_adjacent_dup(xs):
    print(xs)
    new_xs = []
    prev_ele = None
    for e in xs:
        if e != prev_ele:
            new_xs.append(e)
            prev_ele = e

    return new_xs


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("vocab.txt")

def find_unknown_merge_pattern(vocab, wds):
    vocab.sort()
    wds.sort()

    result = []
    pvocab = 0
    pwds = 0

    while True:
        if pvocab >= len(vocab):
            result.extend(wds[pwds:])
            break
        if pwds >= len(wds):
            break
        if vocab[pvocab] == wds[pwds]:
            pwds += 1
        elif vocab[pvocab] < wds[pwds]:
            pvocab += 1
        else:
            result.append(wds[pwds])
            pwds += 1

    return result

if __name__ == "__main__":
    all_words = get_words_in_book("AliceInWonderland.txt", )
    all_words.sort()
    book_words = delete_adjacent_dup(all_words)
    missing_words = find_unknown_merge_pattern(bigger_vocab, book_words)
    print("There are {0} unknown words.".format(len(missing_words)))