

## Problem 1
def print_lol(file_location):
    file = open(file_location)
    text = file.readlines()
    for line in text:
        if 'lol' in line.lower():
            print(line)
   
## Problem 2
def dict_to_str(d):
    for key, value in d.items():
        print(key, ', ', value)
  
## Problem 3
def dict_to_str_sorted(d):
    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        print(key, d[key])
  
## Problem 4
# a
def word_phones_dict():
    file = open('8\\cmudict-0.7b.txt')
    text = file.readlines()
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
    phones_dict = {}
    for line in text:
        line_elements = line.split('\t')
        phones_dict[line_elements[0]] = line_elements[1][:-1]
    return phones_dict


# def syllable_count(str):

## Problem 5
def readability_grade_lvl(file_location):
    f = open(file_location)
    text = file.readlines()
    approx_num_words = text.count(" ")+1
    text.replace('!', '.')
    text.replace('?', '.')
    approx_num_sentences = text.count('.')
    approx_num_syllables = syllable_count(text)
    
    return (
        0.39*(approx_num_sentences/approx_num_sentences) 
        + 11.8*(approx_num_syllables/approx_num_words) 
        - 15.59
    )




if __name__ == "__main__":
    dict_to_str({1:2, 0:3, 10:5})

    word_phones = word_phones_dict()
    phones_cat = phone_cat_dict()
    for key, val in phones_cat.items():
        print(key,val)