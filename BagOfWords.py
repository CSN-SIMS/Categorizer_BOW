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
    counterOfEmails = 0
    if not path.exists(directory):
        print('no folder exists')
    for filename in listdir(directory):
        pathToFile = directory + '/' + filename
        email = open(pathToFile, 'r', encoding='utf-8')
        document = str(email.read())
        printSignificantWordOfFile(document)
        documents = documents + " " + document
        email.close()
        counterOfEmails = counterOfEmails + 1
    print('Amount of Emails: ' + str(counterOfEmails))
    return documents


def loadingFilesIntoArray(directory):
    arrayofEmails = []
    if not path.exists(directory):
        print('no folder exists')
    for filename in listdir(directory):
        pathToFile = directory + '/' + filename
        email = open(pathToFile, 'r', encoding='utf-8')
        document = str(email.read())
        arrayofEmails.append(printSignificantWordOfFile(document))
        email.close()
    print(arrayofEmails)
    return arrayofEmails


def printSignificantWordOfFile(filecontent):
    return stemming(removeSymbols(removeStopwords(tokenize(filecontent))))


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


def printSignificantWordsofDirectory(directoryPath):
    print(removeDuplicates(stemming(removeSymbols(removeStopwords(tokenize(loadingDirectory(directoryPath)))))))
    return removeDuplicates(stemming(removeSymbols(removeStopwords(tokenize(loadingDirectory(directoryPath))))))

def countOccurencyOfWordsPerEmail(directory):
    vectorMatrix = []
    arrayOfSigWordsTotal = printSignificantWordsofDirectory(directory)
    arrayOfSigWordsFile = loadingFilesIntoArray(directory)
    for array in arrayOfSigWordsFile:
        for word in array:
            for wordtotal in arrayOfSigWordsTotal:
                if word == wordtotal:
                    vectorMatrix.append(1)
                else:
                    vectorMatrix.append(0)
    print(vectorMatrix)
    return vectorMatrix



countOccurencyOfWordsPerEmail(directory)


