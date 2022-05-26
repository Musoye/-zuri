# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as my_file:
        new_file = my_file.read()

    
    return new_file


def count_words():
    text = read_file_content("story.txt")
    new_text = text.split()
    dic = {}
    for item in new_text:
        if item in dic:
            count = dic[item]
        else:
            count = 0     
        dic[item] = count + 1
    for key, value in dic.items():
        print(key, value)

    # [assignment] Add your code here

    #return {"as": 10, "would": 20}
count_words()