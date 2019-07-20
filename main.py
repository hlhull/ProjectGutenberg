from helpers import *
import random


# return the number of words in the file
def getTotalNumberOfWords(file):
    return len(getAllWords(file))

# returns the number of UNIQUE words in the novel
def getTotalUniqueWords(file):
    return len(set(getAllWords(file)))

# return the 20 most frequently used words in the novel
# and the number of times they were used
def get20MostFrequentWords(file):
    wordCounts = getWordCounts(file)
    return get20MostFrequentWordsFromWordCounts(wordCounts)

# filters the most common 100 English words and then returns the 20 most
# frequently used words and the number of times they were used
def get20MostInterestingFrequentWords(file):
    wordCounts = getMostInterestingWordsCounts(file)
    return get20MostFrequentWordsFromWordCounts(wordCounts)

# returns the 20 LEAST frequently used words and the number of times they were used
def get20LeastFrequentWords(file):
    wordCounts = getWordCounts(file)
    return get20LeastFrequentWordsFromWordCounts(wordCounts)

# take in a word and return an array of the number of the times the
# word was used in each chapter
def getFrequencyOfWord(wordToFind, file):
    wordToFind = wordToFind.lower()
    chapFreq = []
    currChap = -1
    for word in getAllWords(file):
        if word == 'chapter':
            chapFreq.append(0)
            currChap += 1
        elif word == wordToFind and currChap >= 0:
            chapFreq[currChap] += 1
    return chapFreq

# take in a string (the quote) and return a number (the chapter number)
def getChapterQuoteAppears(quote, file):
    words = getAllWords(file)
    quoteWords = getWordsFromString(quote)
    currChap = 0
    for i in range(len(words)):
        if words[i] == 'chapter':
            currChap += 1
        else:
            j = 0
            while j < len(quoteWords) and i < len(words) and words[i] == quoteWords[j]:
                j += 1
                i += 1
            if j == len(quoteWords):
                return currChap
    return -1

def generateSentenceRandom(file):
    words = getAllWords(file)
    word = 'the'
    sentence = 'the'
    num = 1
    while num < 20:
        wordsToPickFrom = []
        for i in range(len(words)):
            if words[i] == word and i < len(words) - 2:
                wordsToPickFrom.append(words[i+1])
        word = random.choice(wordsToPickFrom)
        sentence = sentence + " " + word
        num += 1
    return sentence

def generateSentenceFreq(startWord, file):
    words = getAllWords(file)
    word = startWord.lower()
    sentence = startWord.lower()
    num = 1
    while num < 20:
        wordsToPickFrom = {}
        max = 0
        maxWord = ''
        for i in range(len(words)):
            if words[i] == word and i < len(words) - 2:
                if words[i+1] in wordsToPickFrom:
                    wordsToPickFrom[words[i+1]] += 1
                else:
                    wordsToPickFrom[words[i+1]] = 1
                if wordsToPickFrom[words[i+1]] > max:
                    max = wordsToPickFrom[words[i+1]]
                    maxWord = words[i+1]
        sentence = sentence + " " + maxWord
        word = maxWord
        num += 1
    return sentence



pp = open("prideAndPrejudice.txt", 'r', encoding="utf8")
# call methods
