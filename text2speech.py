#!/usr/bin/env python
# coding: utf-8

# In[1]:


fro gtts import gTTS


# In[2]:


fro gtts import gTTS


# In[3]:


fro gtts import gTTS
import OS

fh = open("textfile.txt","r")
myText = fh.read().replace("\n"," ")

language = 'en'

output = gTTS(text=myText, lang=language,slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")


# In[5]:


from gtts import gTTS
import OS

fh = open("textfile.txt","r")
myText = fh.read().replace("\n"," ")

language = 'en'

output = gTTS(text=myText, lang=language,slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")


# In[6]:


from gtts import gTTS
import OS

fh = open("textfile.txt","r")
myText = fh.read().replace("\n"," ")

language = 'en'

output = gTTS(text=myText, lang=language,slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")


# In[ ]:




