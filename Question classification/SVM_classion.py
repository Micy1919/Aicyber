# -*- coding:utf-8 -*-
"""
用SVM去分类识别语料是否是问句
模型训练用的7400条训练集
"""
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import jieba
import codecs
from SentenceLstm import WordVectorUtil as wv

clf = joblib.load('./model/clf.model')
jieba.load_userdict('./dict/associateWordList.txt')
df = pd.read_csv('./data/xiatingting.csv')
df = df.fillna('nan')
df = df[df['uid'] != 'nan']
df = df[df['is_flag'] != 'nan']


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


if __name__ == '__main__':
    num = 0
    for w in df['uid'].unique():
        num += 1
        if num % 100 == 0:
            print num

        if w == 'nan':
            continue

        dfMid = df[df['uid'] == w]
        dfMid = dfMid.sort_values('send_time')
        # 找到用户的话语
        df_1 = dfMid[dfMid['is_flag'] == 100]

        for i in range(len(df_1)):
            sent = df_1['content'].iloc[i]
            sent = sent.decode('utf-8')
            mid = make_wordVec(sent)
            if clf.predict(mid)[0] == 1:
                with codecs.open('./data/test.txt', 'a', encoding='utf-8') as f:
                    f.writelines(sent + '\n')
                    f.writelines(w + '\n\n\n')
                break
