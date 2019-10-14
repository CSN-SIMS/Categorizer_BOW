import math
import numpy as np
from os import listdir, path

import nltk
from nltk.stem.snowball import SnowballStemmer

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
        email = open(pathToFile, 'r', encoding='utf-8')
        document = str(email.read())
        printSignificantWordOfFile(document)
        documents = documents + " " + document
        email.close()
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


print('Alles Significanten Wörter:')
print(printSignificantWordsofDirectory(directory))
print('Alles sig Wörter pro File: ')
print(loadingFilesIntoArray(directory))
print('Hashmap mit Häufigkeit eines Terms: ')
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


def TermFrequencyOneArray(hashmapOcc):
    tfHashmap = {}
    for key in hashmapOcc:
        if hashmapOcc[key] > 0:
            tf = 1 + math.log2(hashmapOcc[key])
            tfHashmap.update({key: tf})
        else:
            tfHashmap.update({key:0})
    return tfHashmap


def TermFrequencyMatrix(arrayOfHashmapOcc):
    tfVectorArrays = []
    for hashmap in arrayOfHashmapOcc:
        tfVectorArrays.append(TermFrequencyOneArray(hashmap))
    return tfVectorArrays

print('TF: ' )
print(TermFrequencyMatrix(
    hashmapWordOccurency(loadingFilesIntoArray(directory))))


# print(countOccurencyOfWordsPerEmail(directory))

def amountOfFiles(directory):
    counterOfEmails = 0
    if not path.exists(directory):
        print('no folder exists')
    for filename in listdir(directory):
        counterOfEmails = counterOfEmails + 1
    return counterOfEmails


amountOfFiles_int = amountOfFiles(directory)


def amountOfFileswithTerm(term, arrayOfHashmaps):
    counterOfFiles = 0
    for hashmap in arrayOfHashmaps:
        if hashmap[term] > 0:
            counterOfFiles = counterOfFiles + 1
    return counterOfFiles


def amountOfFilesWithAllTerms(allTerm, ArrayOfHashmaps):
    amountOfFilesWithTermsHashmap = {}
    for term in allTerm:
        amountOfFilesWithTermsHashmap.update({term: amountOfFileswithTerm(term, ArrayOfHashmaps)})
    return amountOfFilesWithTermsHashmap


def idf(allTerms, ArrayOfHashmaps, directory):
    idf = {}
    amountOfFiles_int = amountOfFiles(directory)
    amountOfFilesWithallTermHashmap = amountOfFilesWithAllTerms(allTerms, ArrayOfHashmaps)
    for term in allTerms:
        for key in amountOfFilesWithallTermHashmap:
            if term == key:
                idfNumber = 1 + math.log2(amountOfFiles_int / amountOfFilesWithallTermHashmap[key])
                idf.update({term: idfNumber})
    return idf

print('IDF' )
print(idf(['boy', 'buy', 'flower', 'footbal', 'garden', 'grow', 'mani', 'play'],
                  [{'boy': 2, 'buy': 0, 'flower': 0, 'footbal': 1, 'garden': 1, 'grow': 0, 'mani': 0,
                    'play': 1},
                   {'boy': 0, 'buy': 0, 'flower': 1, 'footbal': 0, 'garden': 1, 'grow': 1, 'mani': 1,
                    'play': 0},
                   {'boy': 1, 'buy': 1, 'flower': 0, 'footbal': 1, 'garden': 0, 'grow': 0, 'mani': 2,
                    'play': 0}],
                  directory))


def tF_IDF(diretory):
    tfidf = []
    tf_maps = TermFrequencyMatrix(
        hashmapWordOccurency(loadingFilesIntoArray(directory)))
    idf_map = idf(printSignificantWordsofDirectory(directory), hashmapWordOccurency(loadingFilesIntoArray(directory)),
                  directory)
    for hashmap in tf_maps:
        tfidf_map = {}
        for key in hashmap:
            result = hashmap[key] * idf_map[key]
            tfidf_map.update({key:result})
        tfidf.append(tfidf_map)
    return tfidf
print('TFIDF_Map_matrix: ')
print(tF_IDF(directory))
print(createVectorsFromArrayWithHashmaps(tF_IDF(directory)))

def compareTwoVectors(vector1,vector2):
    ancle = 0
    return ancle

def scalenproduct2vector(vector1, vector2):
    counter = 0
    scalenproduct = 0
    for int in vector1:
        product = int * vector2[counter]
        scalenproduct = scalenproduct + product
        counter = counter + 1
    return scalenproduct

print(scalenproduct2vector([1,2,3],[3,2,1]))

def lenghOfVector(vector):
    result = 0
    sum = 0
    for int in vector:
        square = int * int
        sum = sum + square
    return math.sqrt(sum)

print(lenghOfVector([1,2,3]))

def cosinusOf2Vectors(vector1, vector2):
    preresult = scalenproduct2vector(vector1, vector2) / (lenghOfVector(vector1) * lenghOfVector(vector2))
    result = math.degrees(math.acos(preresult))
    return result

print(cosinusOf2Vectors([1,2,3],[3,2,1]))
print(cosinusOf2Vectors(createVectorsFromArrayWithHashmaps(tF_IDF(directory))[0], createVectorsFromArrayWithHashmaps(tF_IDF(directory))[1]))

def angleMatrix(arraysOfVectorsProFile):
    angleMatrix = []
    for vector_array2 in arraysOfVectorsProFile:
        angleArrayRow = []
        for vector_array1 in arraysOfVectorsProFile:
            angle = 0
            angle = cosinusOf2Vectors(vector_array1, vector_array2)
            angleArrayRow.append(angle)
        angleMatrix.append(angleArrayRow)
    return angleMatrix

print(angleMatrix(createVectorsFromArrayWithHashmaps(tF_IDF(directory))))

def mostEqualEmails(angleMatrix):
    column = 0
    row = 0
    smallestAngle = 360
    mostEuqalEmailrow = 0
    mostEuqalEmailColumn = 0
    while row <= (amountOfFiles_int/2):
        while column < amountOfFiles_int:
            if column != row:
                if smallestAngle > angleMatrix[row][column]:
                    smallestAngle = angleMatrix[row][column]
                    mostEuqalEmailColumn = column
                    mostEuqalEmailrow = row
            column = column +1
        row = row +1
    return 'Email('+ str(mostEuqalEmailrow+1)+') and Email('+str(mostEuqalEmailColumn+1)+') are very equal'

print(mostEqualEmails(angleMatrix(createVectorsFromArrayWithHashmaps(tF_IDF(directory)))))

