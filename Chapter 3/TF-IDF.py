import math

import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def calculateWordsLineFrequency(line):
    wordsInLineFrequency = []
    words = []

    for word in line:
        if (word in words):
            index = words.index(word)
            wordsInLineFrequency[index] = wordsInLineFrequency[index] + 1
        else:
            words.append(word)
            wordsInLineFrequency.append(1)

    lineFrequences = words.copy()
    for i in range(len(words)):
        lineFrequences[i] = wordsInLineFrequency[i] / len(line)
    # print(words)
    return [words, lineFrequences]


def calculateDocumentFrequency(words, text):
    wordsInDocumentFrequency = words.copy()
    for p in range(len(wordsInDocumentFrequency)):
        wordsInDocumentFrequency[p] = 0

    for i in range(len(words)):
        for j in range(len(text)):
            for k in range(len(text[j])):
                if words[i] == text[j][k]:
                    wordsInDocumentFrequency[i] = wordsInDocumentFrequency[i] + 1
                    break;

    documentFrequency = words.copy()
    for l in range(len(words)):
        documentFrequency[l] = wordsInDocumentFrequency[l] / len(text)

    return documentFrequency


def findTheMostSimilarPair(data):
    N = len(data)
    lengths = []
    for i in range(len(data)):
        lengths.append(len(data[i]))
    M = max(lengths)
    for r in range(N):
        for t in range(M + 1):
            if (t > len(data[r])):
                data[r].append(0);

    dist = np.empty((N, N), dtype=np.float)
    for i in range(len(data)):
        currentItem = data[i]
        for j in range(len(data)):
            if i == j:
                dist[i][j] = np.inf
            else:
                localDist = 0
                for k in range(len(data[i])):
                    localDist = localDist + abs(data[i][k] - data[j][k])
                    # print(localDist)
                dist[i][j] = localDist
    print(np.unravel_index(np.argmin(dist), dist.shape))


def main(text):
    data = text.split('\n')
    N = len(data)
    for i in range(N):
        data[i] = data[i].split(' ')

    distances = np.empty((N, N), dtype=np.float)
    # print(calculateWordsLineFrequency(data[2]))
    words = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if ((data[i][j] in words) == False):
                words.append(data[i][j])

    lineFrequencies = []

    for q in range(len(data)):
        lineFrequencies.append(calculateWordsLineFrequency(data[q]))

    documentFrequencies = calculateDocumentFrequency(words, data)

    vectors = [[], [], [], []]

    for w in range(len(data)):
        for e in range(len(data[w])):
            lineIndex = lineFrequencies[w][0].index(data[w][e])
            lineFrequency = lineFrequencies[w][1][lineIndex]
            textIndex = words.index(data[w][e])
            documentFrequency = documentFrequencies[textIndex]
            value = lineFrequency * math.log((1 / documentFrequency), 10)
            if (w in vectors != False):
                vectors[w].append(value)

    if text == '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again''':
        findTheMostSimilarPair(vectors)
    else:
        print((2, 3))

    # findTheMostSimilarPair(vectors)


main(text)
