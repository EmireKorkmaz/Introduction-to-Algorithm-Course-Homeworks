def word_check(string):

    size = len(string); 

    if (size == 0):
        return True

    for i in range(size):
      first = string[:i]
      second = string[i: size-i+1]
      if (check_word(first) and word_check(second)):
        return True
    return False; 

dictionary = ["it", "was", "the", "best", "of", "times"]


def check_word(word):
    return word in dictionary

print(word_check("itwasthebestoftimes"))s