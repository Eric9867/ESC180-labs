'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


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


def build_semantic_descriptors(sentences):
    semantic_dict = {}
    word_count = {}
    for sentence in sentences:                              # called len(sentences) times
        for i in range(len(sentence)):                      # finding the word count of in a sentence# called len(sentence) times
            # if sentence[i] not in semantic_dict:
            #     semantic_dict[sentence[i]] =  {}
            if sentence[i] not in word_count:
                word_count[sentence[i]] = 1
            else:
                word_count[sentence[i]] += 1
                
        for i in range(len(sentence)):
            dict_copy = dict(word_count)
            if sentence[i] in dict_copy: dict_copy.pop(sentence[i])
            if sentence[i] not in semantic_dict:
                semantic_dict[sentence[i]] = dict_copy  
            else:
                for key, value in dict_copy.items():
                    if key in semantic_dict[sentence[i]]:
                        semantic_dict[sentence[i]][key] += value
                    else:
                        semantic_dict[sentence[i]][key] = value
        word_count = {}                       
    return semantic_dict

# def build_semantic_descriptors(sentences):
#     semantic_dict = {}
#     word_count = {}
#     for sentence in sentences:
#         for i in range(len(sentence)):
#             if sentence[i] not in semantic_dict:
#                 semantic_dict[sentence[i]] =  {}
#             for i in range(len(sentence)):
                

#     pass
def build_semantic_descriptors_from_files(filenames):
    pass



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
    sentences = [["i", "am", "a", "sick", "man"],
                 ["i", "am", "a", "spiteful", "man"],
                 ["i", "am", "an", "unattractive", "man"],
                 ["i", "believe", "my", "liver", "is", "diseased"],
                 ["however", "i", "know", "nothing", "at", "all", "about", "my",
                 "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    
    print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    print(build_semantic_descriptors(sentences)['man'])
    print(build_semantic_descriptors(sentences)['liver'])