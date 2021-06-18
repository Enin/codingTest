# Reverse the order of words in a given sentence (an array of characters).

def reverse_string(sentence):
    s = sentence[::-1]
    return s

def devide_sentence(sentence):
    words = sentence.split(' ')

    return words

def reverse_words(sentence):
    reversed_sentence = reverse_string(sentence)
    reversed_sentence = devide_sentence(reversed_sentence)
    reversed_words = []
    for i in reversed_sentence:
        reversed_words.append(reverse_string(i))

    joined_sentence = " ".join(reversed_words)
    print(joined_sentence)



def test():

    text = 'lets iterate the sentence and reverse each word in place'
    reverse_words(text)

test()
