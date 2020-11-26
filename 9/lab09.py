import urllib.request
#import BeautifulSoup

#####
# Problem 1

def file_word_list(path):
    '''
    Reads the text file at path and return a 
    list of strings that were orgininally separated by
    punctuation (characters in remove_chars) 
    '''
    remove_chars = [',', '-', '.', '!', '?', ';', ':', '\n', '\t', '*', '(', ')', '"']
    
    file = open(path, encoding="latin")
    text = file.read().lower()
    #text = "I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\nHowever, I know nothing at all about my disease, and do not know for certain what ails me"
    file.close()
    for char in remove_chars:
        text = text.replace(char, ' ')
    return text.split()

# part (a)
def word_frequency(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        if word not in word_counts:
            word_counts[word] = 1
    return word_counts

# (b)
def top10(L):
    '''
    Returns a list of the 10 largest integers in the list L
    '''
    assert type(L) == list
    
    largest_nums = [0] * 10
    for n in L:
        if n > min(largest_nums):
            largest_nums[0] = n
            largest_nums.sort()
    return largest_nums

# part (C)
def inv_freq(freq):
    """
    docstring
    """
    val_list = []
    freq_arr = []
    inv_dict = {}
    for key, value in freq.items():
        if value not in inv_dict:
            inv_dict[value] = key
        else:
            freq_arr.append([key,value])

        val_list.append(value)
    max_vals = top10(val_list)
    print("max_vals: ",max_vals)
    top_ten = {}
    for value in max_vals:
        if inv_dict[value] not in top_ten:
             top_ten[inv_dict[value]] = value
        else:
            for [key, arr_value] in freq_arr:
                if arr_value == value and key not in top_ten:
                    top_ten[key] = value 
                    break

    return top_ten



#####
# Problem 2

# • Make the word “ever” appear in bold
def bold_word(path, word):
    file = open(path, 'r+')
    file_text = file.read()
    file_text = file_text.replace(word, '<strong>' + word + '</strong>')
    file.seek(0)
    file.write(file_text)
    file.close()
    return None

# • Add a link to Yahoo.ca’s search results for “engineering science.”
def search_eng_sci(path):
    '''
    Adds a link to a Yahoo search query for engineering science
    to the last empty line of the html file at path
    '''
    url = 'https://ca.search.yahoo.com/search;_ylt=AwrJ6y6Yu75f9F4ALFrqFAx.;_ylc=X1MDMjExNDcyMTAwMgRfcgMyBGZyAwRncHJpZAN5X3BXRm5kLlNneUM1TWtseVMyWTFBBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNjYS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIxBHF1ZXJ5A2VuZ2luZWVyaW5nJTIwc2NpZW5jZQR0X3N0bXADMTYwNjMzNTM4OQ--?fr2=sb-top-ca.search&p=engineering+science&fr=sfp&iscqry='
    file = open(path, 'r+')
    file_lines = file.readlines()
    
    for i in range(len(file_lines)-1,0,-1):
        if file_lines[i] == '<p><a href="' +url+ '">Engineering Science</p>':
            break
        elif file_lines[i] == '\n':
            file_lines[i] = '<p><a href="' +url+ '">Engineering Science</p>\n'
            break
    
    file.seek(0)
    file.writelines(file_lines)
# Print statements for debugging
    # print(file_lines)
    # file.seek(0)
    # print(file.read())
    file.close()
    return None


#######
# Problem 3

def num_results(search_term):
    search_term = search_term.replace(" ","+")
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p="+search_term+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
    page = f.read().decode("utf-8")
    f.close()
    # print(page[:len(page)//4])
    # print(page[len(page)//4:len(page)//2])
    # print(page[len(page)//2:len(page)*3//4])
    # print(page[len(page)*3//4:len(page)])
    string = 'referrerpolicy="unsafe-url">Next<ins></ins></a><span>'
    index_val = page.find(string)

    res = page[index_val + len(string) : index_val + len(string)+50].split()[0]
    #print(res, "results") 
    return res

def choose_variant(variants):
    variant_dict = {}
    ties ={}
    max_res = 0

    for variant in variants:
        num_res_str = num_results(variant) #.split(" ")[0]
        num_res = float(num_res_str.replace(',',''))
        print(variant, num_res_str)

        if num_res not in variant_dict:
            variant_dict[num_res] = variant
        else:
            ties[variant] = num_res
            ties[variant_dict[num_res]] = num_res

        if max_res < num_res:
            max_res = num_res    

    if variant_dict[max_res] not in ties:
        return variant_dict[max_res], max_res
    # if there is a tie for max_res, return all elements that have max_res search results
    else:
        keys = []
        for key, value in ties.items():
            if value == max_res:
                keys.append(key)
        return keys, max_res

if __name__ == "__main__":
    # print("\n======================================================================================================\nPROBLEM 1 TESTS")
    # word_list = file_word_list('9\\Pride_and_Prejudice.txt')
    # print(len(word_list))
    # word_counts = word_frequency(word_list)
    # print(word_counts)
    
    # print("top ten words:", inv_freq(word_counts))
    # print("\n======================================================================================================\nPROBLE 2 TESTS")
    # bold_word('9\\Hello_World - Copy.html', 'ever')    
    # search_eng_sci('9\\Hello_World - Copy.html')    
    print("\n======================================================================================================\nPROBLEM 3 TESTS")
    print(num_results("flathead screwdriver"), "results")
    variants1 = ["flathead screwdriver","flat head screw driver", "flat-head screwdriver", "flat-head screw-driver", "flat-head-screw-driver"]
    variants2 = ["five-year anniversary", "fifth anniversary"]
    variants3 = ["top ranked schools uoft", "top ranked schools waterloo"]
    #print(choose_variant(variants1))
    print(choose_variant(variants2))
    print(choose_variant(variants3))

    for variant in variants1:
        print(variant, num_results(variant), "results")