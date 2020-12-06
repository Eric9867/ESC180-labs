'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math
# import time

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
    # print(semantic_dict)
    return semantic_dict
                
def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for filename in filenames:
        f = open(filename, "r", encoding = "latin1")
        text = f.read().lower()
        f.close()
        text = text.replace("!", ".").replace("?", ".")
        text = text.replace(","," ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ").replace("\n", " ").replace("â€œ"," ").replace("â€"," ").replace("  ", " ").replace("  ", " ")
        sentence_split = text.split(".")
        for i in range(len(sentence_split)):
            sentence_split[i] = sentence_split[i].split(" ")
        sentences.extend(sentence_split)

    ## Remove empty strings from the list sentences
    # sentences = list(filter(lambda sentence: sentence != [''], sentences))
    # sentences = [list(filter(None, sentence)) for sentence in sentences
    sentences = [list(filter(None, sentence)) for sentence in list(filter(lambda sentence: sentence != [''], sentences))]
    # for i in sentences:
    #     print(i)
    return build_semantic_descriptors(sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    def vec_similarity(word, choice):
        try:
            return similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        except:
            return -1

    similarity_score = [vec_similarity(word, choice) for choice in choices]
  
    i_max = similarity_score.index(max(similarity_score)) # Will this return the element that appears first in case of a Tie?
    return choices[i_max]                                 # Also need to add a condition such that if the semantic similarity cannot be computed the similarity must be -1.

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    file = open(filename, "r", encoding = "latin1")
    lines = file.readlines()
    file.close()
    
    # CHECK THAT THIS DOESNT PRODUCE EMPTY STRING LINES
    # Might work: lines = filter(None, lines)

    for i in range(len(lines)):
        lines[i] = lines[i].split()     # Default splits space and new line
    score = 0
    for question in lines:
        if question[1] == most_similar_word(question[0], question[2:], semantic_descriptors, similarity_fn):
              score += 1
    return 100 * score / len(lines) 
    

# if __name__ == "__main__":
#     # sentences = [
#     #     ["i", "am", "a", "sick", "man"],
#     #     ["i", "am", "a", "spiteful", "man"],
#     #     ["i", "am", "an", "unattractive", "man"],
#     #     ["i", "believe", "my", "liver", "is", "diseased"],
#     #     ["however", "i", "know", "nothing", "at", "all", "about", "my",
#     #         "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]
#     # ]
    
#     # print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
#     # print(build_semantic_descriptors(sentences)['man'])
#     # print(build_semantic_descriptors(sentences)['liver'])
#     # build_semantic_descriptors_from_files(['sample_sentences.txt'])
    
#     filenames = ['war_and_peace.txt', 'swanns_way.txt']
#     start_time = time.time()
#     semantic_dict = build_semantic_descriptors_from_files(filenames)
#     end_time = time.time()
#     dt = end_time - start_time
    
#     # for key, val in semantic_dict.items():
#     #     print(key, ':' val)
    
#     #print(semantic_dict)
#     print('###')
#     print("Percentage:", run_similarity_test('test.txt', semantic_dict, cosine_similarity))
#     print('Time:', dt)
    