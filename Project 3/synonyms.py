'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math
import time

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    dot_prod = 0
    vec1_mag_squared = 0
    vec2_mag_squared = 0
    
    for key, value in vec1.items():
        if key in vec2:
            dot_prod += vec2[key]*value
        vec1_mag_squared += value**2
    vec1_mag = math.sqrt(vec1_mag_squared) 
    
    for key, value in vec2.items():
        vec2_mag_squared += value**2
    vec2_mag = math.sqrt(vec2_mag_squared)

    sim_vec1_vec2 = dot_prod/(vec1_mag*vec2_mag)

    return sim_vec1_vec2

# def build_semantic_descriptors(sentences):
#     semantic_dict = {}
#     word_count = {}
#     for sentence in sentences:                              # called len(sentences) times
#         for i in range(len(sentence)):                      # finding the word count of in a sentence# called len(sentence) times
#             if sentence[i] not in word_count:
#                 word_count[sentence[i]] = 1
#             else:
#                 word_count[sentence[i]] += 1
                
#         for i in range(len(sentence)):
#             dict_copy = dict(word_count)
#             if sentence[i] in dict_copy: dict_copy.pop(sentence[i])
#             if sentence[i] not in semantic_dict:
#                 semantic_dict[sentence[i]] = dict_copy  
#             else:
#                 for key, value in dict_copy.items():
#                     if key in semantic_dict[sentence[i]]:
#                         semantic_dict[sentence[i]][key] += value
#                     else:
#                         semantic_dict[sentence[i]][key] = value
#         word_count = {}
#     return semantic_dict

def build_semantic_descriptors(sentences):
    semantic_dict = {}
    # word_count = {}
    for sentence in sentences:
        duplicates_removed = list(set(sentence))

        for i in range(len(duplicates_removed)):
            if duplicates_removed[i] not in semantic_dict:
                semantic_dict[duplicates_removed[i]] = {}
            for word in duplicates_removed:
                if word != duplicates_removed[i]:
                    if word not in semantic_dict[duplicates_removed[i]]:
                        semantic_dict[duplicates_removed[i]][word] = 1
                    else:
                        semantic_dict[duplicates_removed[i]][word] += 1
    # for sentence in sentences:                              # called len(sentences) times
    #     for i in range(len(sentence)):                      # finding the word count of in a sentence# called len(sentence) times
    #         if sentence[i] not in word_count:
    #             word_count[sentence[i]] = 1
    #         else:
    #             word_count[sentence[i]] += 1
                
    #     for i in range(len(sentence)):
    #         dict_copy = dict(word_count)
    #         if sentence[i] in dict_copy: dict_copy.pop(sentence[i])
    #         if sentence[i] not in semantic_dict:
    #             semantic_dict[sentence[i]] = dict_copy  
    #         else:
    #             for key, value in dict_copy.items():
    #                 if key in semantic_dict[sentence[i]]:
    #                     semantic_dict[sentence[i]][key] += value
    #                 else:
    #                     semantic_dict[sentence[i]][key] = value
    #     word_count = {}
    return semantic_dict

# def build_semantic_descriptors(sentences):
#     semantic_dict = {}
#     word_count = {}
#     for sentence in sentences:                              # called len(sentences) times
#         for i in range(len(sentence)):                      # finding the word count of in a sentence# called len(sentence) times
#             if sentence[i] not in word_count:
#                 word_count[sentence[i]] = 1
#             if sentence[i] not in semantic_dict:
#                 semantic_dict[sentence[i]] = {}
#                 called_words = []
                
#                 for j in range(len(sentence)):    
#                     if sentence[i] != sentence[j] and (sentence[j] not in called_words):
#                         if sentence[j] not in semantic_dict[sentence[i]]:
#                             semantic_dict[sentence[i]][sentence[j]] = 1
#                         else:        
#                             semantic_dict[sentence[i]][sentence[j]] += 1
#                     called_words.append(sentence[j])

#     return semantic_dict
                
def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for filename in filenames:
        f = open(filename, "r", encoding = "latin1")
        text = f.read().lower()
        f.close()
        text = text.replace("!", ".").replace("?", ".")
        text = text.replace(","," ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ").replace("\n", ".").replace("  ", " ")
        sentence_split = text.split(".")
        for i in range(len(sentence_split)):
            sentence_split[i] = sentence_split[i].split(" ")
        sentences.extend(sentence_split)

    # sentences = list(filter(lambda sentence: sentence != [''], sentences))
    # sentences = [list(filter(None, sentence)) for sentence in sentences
    sentences = [list(filter(None, sentence)) for sentence in list(filter(lambda sentence: sentence != [''], sentences))]
    # for i in sentences:
    #     print(i)
    
    

    return build_semantic_descriptors(sentences)
#'exception': {'sexual': 1, 'everywhere': 1, 'computer': 1, 'suddenly': 1, 'ignore': 1, 'occupation': 1}
#'exception': {'computer': 2, 'sexual': 2, 'suddenly': 2, 'everywhere': 2, '': 3, 'occupation': 1, 'ignore': 1}

#'million': {'adjustment': 3, 'something': 3, 'theory': 3, 'motion': 3, 'condition': 1, 'honor': 1, 'saving': 1, 'meeting': 1, 'basketball': 1, 'authority': 1, 'since': 1, 'anxiety': 1, 'homeless': 1}
#'million': {'something': 6, 'theory': 9, 'motion': 6, 'adjustment': 6, '': 13, 'basketball': 2, 'meeting': 1, 'condition': 2, 'honor': 1, 'saving': 2, 'since': 1, 'authority': 3, 'homeless': 2, 'anxiety': 1}


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similarity_score = [similarity_fn(semantic_descriptors[word][choice]) for choice in choices]
    i_max = similarity_score.index(max(similarity_score))
    return choices[i_max]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    file = open(filename, "r", encoding = "latin1")
    lines = file.readlines()
    file.close()
    
    # CHECK THAT THIS DOESNT PRODUCE EMPTY STRING LINES
    # Might work: lines = filter(None, lines)
    for line in lines:
        print(line)
    print(lines)
    #['draw paint walk paint\n', 'duty task task example\n', 'earnest serious seri...s amusing\n', 'picture painting pai...ing chair\n', 'vexed annoyed amused annoyed\n', 'watch see hear see\n', 'tidy clean mess clean\n', 'youthful young young complex\n', 'strike beat beat complain\n', 'tearful crying frown...ng crying\n', 'lonely alone alone together\n', 'ardent keen keen wise\n', 'thief robber robber postman\n', 'authentic genuine ge...ine false\n', ...]
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n').split()     # Default space
    score = 0
    for question in lines:
        if question[1] == most_similar_word(question[0], question[2:], semantic_descriptors, cosine_similarity):
              score += 1
    return 100 * score / len(lines) 
    

if __name__ == "__main__":
    # sentences = [
    #     ["i", "am", "a", "sick", "man"],
    #     ["i", "am", "a", "spiteful", "man"],
    #     ["i", "am", "an", "unattractive", "man"],
    #     ["i", "believe", "my", "liver", "is", "diseased"],
    #     ["however", "i", "know", "nothing", "at", "all", "about", "my",
    #         "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]
    # ]
    
    # print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    # print(build_semantic_descriptors(sentences)['man'])
    # print(build_semantic_descriptors(sentences)['liver'])
    # build_semantic_descriptors_from_files(['sample_sentences.txt'])
    
    filenames = ['war_and_peace.txt', 'swanns_way.txt']
    start_time = time.time()
    semantic_dict = build_semantic_descriptors_from_files(filenames)
    end_time = time.time()
    dt = end_time - start_time
    
    print(semantic_dict)
    print()
    print(run_similarity_test('test.txt', semantic_dict, cosine_similarity))
    print(dt)
    