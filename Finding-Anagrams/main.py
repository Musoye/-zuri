# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word_input, word_inp):
    # [assignment] Add your code here
    if len(word_input) != len(word_inp):
        return False
    else:
        string_input = sorted(word_input)
        string_inp = sorted(word_inp)
        if (string_input == string_inp):
    	    return True
        else:
            return False

