#!/usr/bin/env python
# coding: utf-8

# In[82]:


import json
import jieba


# In[83]:


def dealFile():
    txt = open("test.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)  # 使用搜索引擎模式对文本进行分词
    return words


# In[84]:


def totol(words):  # 统计次数
    counts = {}
    for word in words:
        if len(word) == 1: 
            continue
        else:
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    return items


# In[85]:


def seg_depart(sentence):# 对文档中的每一行进行中文分词
    s=""
    sentence_depart = jieba.lcut(sentence.strip())
    for w in sentence_depart:
        if len(w)>1:
            s+=w
    sentence_depart = jieba.cut(s)
    return sentence_depart

depart = seg_depart(text)

fW = open('fenci.txt', 'w', encoding='UTF-8')
fW.write(' '.join(depart))
fW.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




