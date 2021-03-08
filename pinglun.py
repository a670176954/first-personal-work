#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import time
import requests
import random
import time


# In[ ]:


# 评论的列表和总数
alist=[]
s=12696

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
number=1613708132614
cursor='0'
count=0


# In[ ]:


for i in range(s//10):
    url="https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + str(
        number)
    source=requests.get(url, headers=headers).content.decode()
    result=re.findall('"content":"(.*?)","up":', source, re.S)
    alist.append(result)

    # 下一页的cursor在当前页面中进行获取
    cursor=re.findall('"last":"(.*?)","', source, re.S)[0]
    number+=1
    count+=len(result)
print(count)
print(len(atlist))
print(atlist)


# In[ ]:


# 将评论写到test.txt文件中
with open('test.txt', "a", encoding="UTF-8") as f:
    for list1 in alist:
        for x in list1:
            f.write(x)
            f.write('\n')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




