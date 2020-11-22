
## Problem 1
def print_lol(file_location):
    file = open(file_location)
    text = file.readlines()
    for line in text:
        if 'lol' in line.lower():
            print(line)
   
## Problem 2
def dict_to_str(d):
    string = ''
    for key, value in d.items():
        string += (str(key) + ', ' + str(value) + '\n')
    return string
  
## Problem 3
def dict_to_str_sorted(d):
    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        print(key, d[key])

## PROBLEM 4 halil
# a
def word_phones_dict2():
    f = open('8\\cmudict-0.7b.txt')
    

## Problem 4
# a
def word_phones_dict():
    file = open('8\\cmudict-0.7b.txt')
    text = file.readlines()
    file.close()
    word_phones_dict = {}
    for line in text:
        if not line[0] == ';':
            word_phones = line.split('  ')
                # produces a list of length 2
                # ['word', 'phone1 phone2 phone3 phone4\n']
            word_phones_dict[word_phones[0]] = word_phones[1][:-1].split(' ')
                # slicing removes the \n from the end
                # split converts to a list
    return word_phones_dict

# b
def phone_cat_dict():
    file = open('8\\cmudict-0.7b.phones.txt')
    text = file.readlines()
    file.close()
    phones_dict = {}
    for line in text:
        line_elements = line.split('\t')
        phones_dict[line_elements[0]] = line_elements[1][:-1]
    return phones_dict

# c
def num_vowels(word): # vowel phones
    word_dict = word_phones_dict()
    phone_dict = phone_cat_dict()
    try:
        list_of_phones = word_dict[word.upper()]
    except KeyError:
        return 0 # We will be underestimating the vowel count if this is called on a word that is not present in the dictionnary

    count = 0
    for i in range(len(list_of_phones)):

        while list_of_phones[i][-1].isdigit():
            list_of_phones[i] = list_of_phones[i][:-1]
        try:
            if phone_dict[list_of_phones[i]] == 'vowel' and (i-1 >= 0 or phone_dict[list_of_phones[i-1]] != 'vowel'):
                count+=1
        except KeyError:
            print(KeyError)
            print(list_of_phones[i])
    return count

    
# we will count the number of vowel phones in a word, 
# counting consecutive vowel phones as one vowel

# d
def syllable_count(text):
    print(text)
    text = text.replace(".", "").replace(",","").replace("-"," ").replace("\n", " ").replace("*", "").replace("\t", " ").replace(";", "").replace("(", "").replace(")","").replace('"',"")
    for i in range(10):
        print()
    print(text)
    
    word_list = text.split(' ')
    count = 0
    for word in word_list:
        print(word)
        count += num_vowels(word) 
    return count


## Problem 5
def readability_grade_lvl(file_location):
    f = open(file_location)
    text = f.read()
    f.close()
    text = text[:1000]

    text.replace('!', '.')
    text.replace('?', '.')
    
    approx_num_words = text.count(" ") + 1
    approx_num_sentences = text.count('.')
    approx_num_syllables = syllable_count(text)
    print(approx_num_words)
    print(approx_num_sentences)
    print(approx_num_syllables)
    print('\n', 206.835-1.015*(approx_num_words/approx_num_sentences)-84.6*(approx_num_syllables/approx_num_words))
    return (
        0.39*(approx_num_sentences/approx_num_sentences) 
        + 11.8*(approx_num_syllables/approx_num_words) 
        - 15.59
    )


if __name__ == "__main__":
    dict_to_str({1:2, 0:3, 10:5})
    print(num_vowels('dictionary'))
    
    print(readability_grade_lvl('8\\moby_dick.txt'))
    
    # word_phones = word_phones_dict()
    phones_cat = phone_cat_dict()
    print(dict_to_str(phones_cat))

    # print_lol('8\\lol.txt')