# -*- coding:utf-8 -*-
import sys
import random
import matplotlib.pyplot as plt
import codecs
import pickle
sys.path.append('../../../')
from SentenceLstm import WordSpliter as ws
'''
f = codecs.open('./data/chinese.txt', 'r', encoding='utf-8')
ChinesetxtDic = pickle.load(open('./data/ChinesetxtDic.p', 'r'))
num = 0
for line in f:
    num += 1
    if num < 115000:
        continue
    print num
    midCut = ws.split(line)
    mid = []
    for w in midCut:
        mid.append(w[u'word'])
    ChinesetxtDic[line] = mid
pickle.dump(ChinesetxtDic, open('./data/ChinesetxtDic.p', 'wb'))
'''
f1 = pickle.load(open('./data/Chinese.txt.p', 'r'))
f2 = pickle.load(open('./data/English.txt.p', 'r'))
ChEDic = pickle.load(open('./data/ChineseDic.p', 'r'))
ChDic = pickle.load(open('./data/ChinesetxtDic.p', 'r'))
stopWord = pickle.load(open('./data/stopWord.p', 'r'))
# 判断可以替换位置的个数,返回一个List
def judge_number(cut_word, midStr):

    numberList = []
    for j in range(len(cut_word)):
        if cut_word[j] in stopWord:
            continue
        if cut_word[j] in ChEDic:
            for w in ChEDic[cut_word[j]]:
                if w in midStr:
                    numberList.append([j, midStr.index(w)])
    return numberList


def make_sentence(cut_word, midStr, numberList):
    midList = [0 for _ in range(len(numberList))]
    if len(midList) > 4:
        for i in range(len(midList)/2, len(midList)):
            midList[i] = 1
        for i in range(10):
            random.shuffle(midList)
            svae_sentence(cut_word[:], midStr[:], midList, numberList)
        return
    while True:
        # print midList
        svae_sentence(cut_word[:], midStr[:], midList, numberList)
        for i in range(len(numberList)):
            if midList[i] == 0:
                midList[i] = 1
                break
            else:
                midList[i] = 0
                continue
        if 1 not in midList:
            break


def svae_sentence(cut_word, midStr, midList, numberList):
    # print numberList
    for i in range(len(midList)):
        if midList[i] == 0:
            continue
        j, z = numberList[i][0], numberList[i][1]
        cut_word[j], midStr[z] = midStr[z], cut_word[j]
    with codecs.open('./data/Finally_语料.txt', 'a', encoding='utf-8') as f:
        f.writelines(' '.join(cut_word))
        f.writelines(' '.join(midStr) + '\n')
if __name__ == '__main__':
    BaoHList = []
    for i in range(len(f1)):
        cut_word = ChDic[f1[i]]
        # print f2[i]
        midStr = f2[i].replace(u'\ufeff', '')
        midStr = midStr.split(' ')
        numberList =judge_number(cut_word, midStr)
        print len(numberList)
        make_sentence(cut_word, midStr, numberList)
        BaoHList.append(len(numberList))
    # print sum(BaoHList)/len(BaoHList)
    # plt.plot(BaoHList)
    # plt.show()
