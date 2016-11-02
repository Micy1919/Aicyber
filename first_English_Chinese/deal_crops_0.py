# -*- coding:utf-8 -*-
"""
处理原始的中英文txt:
    中文txt和英文txt中存放的是一行一行的语料
生成:
    分词完成的中文List：
        List：[a1, a2, ...]
        List:[b1, b2, ...]
        a1:中文分词结果:[xx,xx,...]
        b1:对应的英文结果
    所有词的字典：
       ChinCutDic.p：{XX：1,xx:1,...}
"""
import codecs
import sys
import pickle

sys.path.append('../../../')
from SentenceLstm import WordSpliter as ws


# 分词函数
# 返回一个分完词的list
def cut_word(sent):
    midCut = ws.split(sent)
    mid = []
    for w in midCut:
        mid.append(w[u'word'])
    return mid


# 分词处理函数
def deal_crops_0(ChAddress, EnAddress, address):
    fCh = codecs.open(ChAddress, 'r', encoding='utf-8')
    fEn = codecs.open(EnAddress, 'r', encoding='utf-8')

    a = fCh.read()
    b = fEn.read()
    a = a.split('\n')
    b = b.split('\n')

    # 分词得到的字典
    ChinCutDic = {}
    chList, enList = [], []
    for i in range(len(a)):
        print i
        cutList = cut_word(a[i])
        if len(cutList) < 4:
            continue

        for w in cutList:
            if w not in ChinCutDic:
                ChinCutDic[w] = 1

        chList.append(cutList)
        enList.append(b[i])

    pickle.dump(chList, open(ChAddress + '.p', 'wb'))
    pickle.dump(enList, open(EnAddress + '.p', 'wb'))
    pickle.dump(ChinCutDic, open(address + '/ChinCutDic.p', 'wb'))

if __name__ == '__main__':
    address = '/home/bill/PycharmProjects/aicyber/BaiDu_translate/data/first_English_Chinese/data'
    deal_crops_0(address+'/douban._Chi.txt', address+'/douban._Eng.txt', address)

