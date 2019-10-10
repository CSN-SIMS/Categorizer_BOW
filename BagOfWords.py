import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.snowball import SnowballStemmer

# nltk.download()

# *****Contants******
language = 'english'

# (brown.words()) #testing nltk
email1 = open("./inputEmails/Email1.txt", "r")
email2 = open("./inputEmails/Email2.txt", "r")
email3 = open("./inputEmails/Email3.txt", "r")
email1p = email1
email2p = email2
email3p = email3


def tokenize(textfile):
    textfile = str(textfile.read())
    tokens = nltk.word_tokenize(textfile, language, False)
    return tokens


def removeStopwords(arrayOfStrings):
    new_word_list = []
    for word in arrayOfStrings:
        word = word.lower()
        if word not in nltk.corpus.stopwords.words(language):
            new_word_list.append(word)
    return new_word_list


def removeSymbols(arrayOfStrings):
    list_of_removing_symbols = ['.', '!', ',']
    new_word_list = arrayOfStrings
    for index in arrayOfStrings:
        if index in list_of_removing_symbols:
            new_word_list.remove(index)
        return new_word_list


def stemming(arrayOfStrings):
    new_word_list = []
    stemmer = SnowballStemmer(language)
    for index in arrayOfStrings:
        new_word_list.append(stemmer.stem(index))
    return new_word_list


def removeDuplicates(arraOfStrings):
    new_word_list = list(set(arraOfStrings))
    return new_word_list


# def printSignificantWords

# def

print(removeDuplicates(stemming(removeSymbols(removeStopwords(tokenize(email1))))))
print(removeDuplicates(stemming(removeSymbols(removeStopwords(tokenize(email2))))))
print(removeDuplicates(stemming(removeSymbols(removeStopwords(tokenize(email3))))))

print(email1p.read())
print(email2p.read())
print(email3p.read())
