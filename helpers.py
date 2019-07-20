import heapq as hq

punctuation = '''.?!”""“,_;':'''

def getAllWords(file):
    words = []
    for word in file.read().split():
        indices = []
        for i in range(len(word)):
            if word[i] in punctuation:
                indices.append(i)
        for i in range(len(indices)-1, -1, -1):
            index = indices[i]
            word = word[:index] + word[index+1:]
        if '--' in word:
            index = word.index('--')
            word = word[:index]
            word2 = word[index+2:]
            words.append(word2.lower())
        words.append(word.lower())
    return words

def getWordsFromString(string):
    words = []
    for word in string.split():
        indices = []
        for i in range(len(word)):
            if word[i] in punctuation:
                indices.append(i)
        for i in range(len(indices)-1, -1, -1):
            index = indices[i]
            word = word[:index] + word[index+1:]
        words.append(word.lower())
    return words

def getWordCounts(file):
    wordCounts = {}
    for word in getAllWords(file):
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
    return wordCounts

def get20MostFrequentWordsFromWordCounts(wordCounts):
    common20 = []
    for word in wordCounts:
        if len(common20) < 20:
                hq.heappush(common20, [wordCounts[word], word])
        elif common20[0][0] < wordCounts[word]:
                hq.heappushpop(common20, [wordCounts[word], word])

    # reverse s/t common20 gives [word, num]
    for i in range(len(common20)):
        num = common20[i][0]
        common20[i][0] = common20[i][1]
        common20[i][1] = num
    return common20

def getMostInterestingWordsCounts(file):
    wordCounts = getWordCounts(file)
    toDelete = []
    for key in wordCounts:
        if key in open('mostCommon100.txt').read():
            toDelete.append(key)
    for key in toDelete:
        del wordCounts[key]
    return wordCounts

def get20LeastFrequentWordsFromWordCounts(wordCounts):
    common20 = []
    for word in wordCounts:
        if len(common20) < 20:
                hq.heappush(common20, [wordCounts[word]*-1, word])
        elif common20[0][0] < wordCounts[word]:
                hq.heappushpop(common20, [wordCounts[word]*-1, word])

    # reverse s/t common20 gives [word, num]
    for i in range(len(common20)):
        num = common20[i][0]
        common20[i][0] = common20[i][1]
        common20[i][1] = num*-1
    return common20
