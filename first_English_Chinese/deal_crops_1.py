# -*- coding:utf-8 -*-
"""
处理第一步完成的List:
    ChinCutDic.p

"""
import pickle


def compute_wordList(word, EnglishDic):
    mid = []
    for w in EnglishDic:
        try:
            if word in w.decode('utf-8'):
                mid.append(EnglishDic[w])
        except:
            if word in w:
                mid.append(EnglishDic[w])
    return mid


def deal_cropList(ChAddress, EnDic):
    Ch_EnDIc = {}
    chineseDic = pickle.load(open(ChAddress, 'rb'))
    EnglishDic = pickle.load(open(EnDic, 'rb'))
    for w in chineseDic:
        mid = compute_wordList(w, EnglishDic)
        if mid == []:
            continue
        Ch_EnDIc[w] = mid
    print len(Ch_EnDIc)
    pickle.dump(Ch_EnDIc, open(ChAddress[-3]+'ChandEn.p', 'wb'))


if __name__ == '__main__':
    address = '/home/bill/PycharmProjects/aicyber/BaiDu_translate/data/first_English_Chinese/data'
    deal_cropList(address+'/ChinCutDic.p', address+'/EnglishDic.p')
