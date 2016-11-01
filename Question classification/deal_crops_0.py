# -*- coding:utf-8 -*-
"""
2016.10.30
处理问句的语料信息，把每一句话转换成（300，）的向量存起来；
每句话词向量之间是加的关系
最终存在一个List里面
"""
import pandas as pd
import numpy as np
import codecs
import pickle
import jieba
from SentenceLstm import WordVectorUtil as wv
jieba.load_userdict('./dict/associateWordList.txt')
df = pd.read_csv('./data/中英文问句对照表（总）.csv', encoding='gbk', header=None)


# 分词并生成词向量
# return 词向量或者None
def make_wordVec(sent):
    midVec = np.zeros((300,))
    for w in jieba.cut(sent):
        try:
            midVec += wv.getWordVector(w)
        except:
            continue
    return midVec


# 处理英文语料
def deal_EngLish():
    EngList = []
    for i in range(len(df)):
        print i
        sent = df[0].iloc[i]
        midVec = make_wordVec(sent)
        if midVec is not None:
            EngList.append(midVec)

    pickle.dump(EngList, open('./data/EngList.p', 'wb'))


# 处理中文语料，找的维基百科里面分出来的中文话
def deal_China():
    ChiList = []
    f =codecs.open('./data/wiki.zh.chs.utf.txt', encoding='utf-8')
    num_i = 0
    for line in f:
        for sent in line.split(' '):
            print num_i
            num_i += 1
            if num_i > 3740:
                break
            mid = make_wordVec(sent)
            ChiList.append(mid)
        if num_i > 3740:
            break
    pickle.dump(ChiList, open('./data/ChiList.p', 'wb'))


if __name__ == '__main__':
    deal_China()