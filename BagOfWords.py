import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.snowball import SnowballStemmer
from os import listdir, path

# nltk.download()

# *****Contants******
language = 'english'

# (brown.words()) #testing nltk

directory = './inputEmails'
def loadingDirectory(directory):
    documents = ""
    if not path.exists(directory):
        print('no folder exists')
    for filename in listdir(directory):
        pathToFile = directory + '/' + filename
        email= open(pathToFile, 'r', encoding='utf-8')
        documents = documents + " " + str(email.read())
        email.close()
    return documents


def tokenize(textfile):
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

 #def mergeArrays():

print(removeDuplicates(stemming(removeSymbols(removeStopwords(tokenize(loadingDirectory(directory)))))))

