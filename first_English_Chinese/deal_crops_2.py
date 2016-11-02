# -*- coding:utf-8 -*-
"""
最终处理0,1步骤生成的语料
"""
import random
import codecs
import pickle

f1 = pickle.load(open('./data/douban._Chi.txt.p', 'r'))
f2 = pickle.load(open('./data/douban._Eng.txt.p', 'r'))
ChDic = pickle.load(open('./data/cChandEn.p', 'r'))
stopWord = pickle.load(open('./data/stopWord.p', 'r'))


# 判断可以替换位置的个数,返回一个List
# cut_word是一个List里面是一句话对应的分词结果
def judge_number(cut_word, midStr):

    numberList = []
    for j in range(len(cut_word)):
        if cut_word[j] in stopWord:
            continue
        if cut_word[j] in ChDic:
            for w in ChDic[cut_word[j]]:
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
        f.writelines(' '.join(cut_word)+'\n')
        f.writelines(' '.join(midStr) + '\n')

if __name__ == '__main__':
    BaoHList = [',', '.', '~', '\\', '/"']
    for i in range(len(f1)):
        cut_word = f1[i]
        # print f2[i]
        for w in BaoHList:
            midStr = f2[i].replace(w, '')
        midStr = midStr.split(' ')
        numberList =judge_number(cut_word, midStr)
        print len(numberList)
        make_sentence(cut_word, midStr, numberList)