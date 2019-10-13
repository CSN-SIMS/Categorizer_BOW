from os import listdir, path
import math
import nltk
from nltk.stem.snowball import SnowballStemmer

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
    return arrayofEmails


def printSignificantWordOfFile(filecontent):
    return sortArray(stemming(removeSymbols(removeStopwordsLowerCase(tokenize(filecontent)))))


def tokenize(textfile):
    tokens = nltk.word_tokenize(textfile, language, False)
    return tokens


def removeStopwordsLowerCase(arrayOfStrings):
    new_word_list = []
    for word in arrayOfStrings:
        word = word.lower()
        if word not in nltk.corpus.stopwords.words(language):
            new_word_list.append(word)
    return new_word_list


def removeSymbols(arrayOfStrings):
    list_of_removing_symbols = ['.', '!', ',', '?', '??', '!!']
    new_word_list = arrayOfStrings.copy()
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
    return sortArray(
        removeDuplicates(stemming(removeSymbols(removeStopwordsLowerCase(tokenize(loadingDirectory(directoryPath)))))))


def sortArray(array):
    # isStringArray = True
    # for word in array:
    #     if word is not str:
    #         isStringArray = False
    #         raise TypeError('the content of the array is not strings')
    array.sort()
    return array


def countOccurencyOfWordsPerEmail(directory):
    vectorMatrix = []
    arrayOfSigWordsTotal = printSignificantWordsofDirectory(directory)
    arrayOfSigWordsFile = loadingFilesIntoArray(directory)
    for array in arrayOfSigWordsFile:
        vectorMatrixbuffer = []
        for word in array:
            for wordtotal in arrayOfSigWordsTotal:
                if word == wordtotal:
                    vectorMatrixbuffer.append(1)
                else:
                    vectorMatrixbuffer.append(0)
        vectorMatrix.append(vectorMatrixbuffer)
    return vectorMatrix


def hashmapWordOccurency(arraysOfFiles):
    arraysOfAllHashmaps = []
    for array in arraysOfFiles:
        wordOccurencyHashmap = {}
        for word in printSignificantWordsofDirectory(directory):
            counter = 0
            if word in array:
                while word in array:
                    counter = counter + 1
                    array.remove(word)
                wordOccurencyHashmap.update({word: counter})
            else:
                wordOccurencyHashmap.update({word: 0})
        arraysOfAllHashmaps.append(wordOccurencyHashmap)
    return arraysOfAllHashmaps


print(printSignificantWordsofDirectory(directory))
print(loadingFilesIntoArray(directory))
print(hashmapWordOccurency(loadingFilesIntoArray(directory)))

def createVectorOutOfHashmap(hashmap):
    vectorArray = []
    for key in hashmap:
        vectorArray.append(hashmap[key])
    return vectorArray

def createVectorsFromArrayWithHashmaps(arraysOfAllHashmaps):
    vectorArrays = []
    for hashmap in arraysOfAllHashmaps:
        vectorArrays.append(createVectorOutOfHashmap(hashmap))
    return vectorArrays


print(createVectorsFromArrayWithHashmaps(hashmapWordOccurency(loadingFilesIntoArray(directory))))


def TermFrequencyOneArray(vectorA):
    tfArray = []
    for number in vectorA:
        if number > 0:
            tf = 1 + math.log2(number)

            tfArray.append(tf)
        else:
            tfArray.append(0)
    return tfArray

def TermFrequencyMatrix(arraysOfVectors):
    tfVectorArrays = []
    for array in arraysOfVectors:
        tfVectorArrays.append(TermFrequencyOneArray(array))
    return tfVectorArrays

print(TermFrequencyMatrix(createVectorsFromArrayWithHashmaps(hashmapWordOccurency(loadingFilesIntoArray(directory)))))
# print(countOccurencyOfWordsPerEmail(directory))
