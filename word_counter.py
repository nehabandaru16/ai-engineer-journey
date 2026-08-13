#given a paragraph of text, count how many times each word appears, using a dictionary.

# text ="I am learning to crack interviews on AI, I am building projects"

# words = text.split()

# word_counts= {}

# for word in words:
#     word = word.strip(".,!?") #removes these characters from start/end of each word
#     if word in word_counts: 
#         word_counts[word]= word_counts[word] +1
#     else:
#         word_counts[word] = 1

# print(word_counts)


def count_word(text):
    try:
        words= text.split()
    except AttributeError:
        print("Error:input must be a string, not", type(text))
        return{}


    words = text.split()   #string becomes a list of words
    words_count={}         #empty dictionary to fill in
    
    for word in words:     # loop over the LIST
        word = word.strip('.,!?') #clean punctuation off this word
        if word in words_count: #check the dictionary, not the list
            words_count[word] = words_count[word]+1
        else: 
            words_count[word]= 1
    return(words_count)

result = count_word("")

print(result)




