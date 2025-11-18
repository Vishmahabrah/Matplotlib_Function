#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib import style


# In[2]:


Days=[1,2,3,4,5]
Temparature=[30,32,88,33,90]
plt.title('Agartala Temparature')
plt.xlabel("Days")
plt.ylabel("Temparature")
plt.axis([0,30,0,100])
plt.plot(Days, Temparature)
plt.show()


# **PART- 2**
# 

# In[3]:


city_code =[2,3,4,5,6,7,16,28]
population = [22,31,40,42,52,65,33,45]
plt.plot(city_code,population)
plt.title('Statewise Population Density',fontsize=19)
plt.plot(city_code,population,color='b',marker="o",linestyle='--',linewidth=4,markersize=9)
plt.legend(["population","Growth"],loc=1)
style.use("ggplot")
plt.grid(color='w',linestyle='-',linewidth=1) 
plt.xlabel("city_code",fontsize=12)
plt.ylabel("population",fontsize=12)
plt.show()


# **PART 4**
# 

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import random


# In[5]:


ml_student = np.random.randint(18,60,size=50)
py_student = np.random.randint(15,40,size=50)
print(ml_student)
print(py_student)


# In[6]:


plt.hist(ml_student)
plt.title("Ml_Student Ages")
plt.xlabel("Student age category")
plt.ylabel("no of students age")

plt.figure(figsize=(15,8))
plt.show()


# In[7]:


bins=[15,20,25,30,35,40,45,50,55,60]# boundery range 
plt.hist(ml_student,bins,rwidth=0.8,histtype="bar",orientation="vertical",color="g",label="ml_student")


# In[8]:


plt.hist([ml_student, py_student],bins,rwidth=0.8,histtype="bar",orientation="vertical",color=["m","r"],label=["ml_student","ml_student"])
style.use("ggplot")


# **PART-5**

# In[9]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib as style


# In[10]:


classes = ["pyhton","R","AI","ML","DS"]
class_1=[20,30,40,50,60]
class_2=[25,35,45,65,55]
class_3=[33,45,53,11,12]
plt.bar(classes,class_1)


# In[11]:


plt.barh(classes,class_1)


# In[12]:


plt.bar(classes,class_1,align='edge',alpha=0.5,linestyle="--",edgecolor='black',linewidth=2)
plt.show()


# In[13]:


plt.bar(classes,class_1,label="class_1 students",visible=False)
plt.show()


# **PART 6**
# 

# In[14]:


classes = ["pyhton","R","AI","ML","DS"]
class_1=[20,30,40,50,60]
class_2=[25,35,45,65,55]
class_3=[33,45,53,11,12]
plt.bar(classes,class_1)


# In[15]:


plt.figure(figsize=(4,4))
classes_index = np.arange(len(classes))
width=0.2
plt.bar(classes_index,class_1,width,color="b",label="class_1 students")
plt.bar(classes_index+width,class_2,width,color="g",label="class_2 students")

plt.xticks(classes_index+width,classes,rotation=5)
plt.title("Bar chart of Different Class",fontsize=18)
plt.xlabel("classes",fontsize=15)
plt.ylabel("no of students",fontsize=15)
plt.show()


# **PART 7 (Scatterplot)**

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd


# In[17]:


df_playstore = pd.read_csv("/Users/pritamsaha/Downloads/store.csv")
df_playstore.shape


# In[18]:


df_playstore = pd.read_csv("/Users/pritamsaha/Downloads/store.csv",nrows=11)
df_playstore.shape


# In[19]:


x=df_playstore["Rating"]
y=df_playstore["Reviews"]
plt.scatter(x,y)


# In[20]:


plt.figure(figsize=(5,5))
plt.scatter(x,y,c="r",marker="*",s=100,alpha=0.5)
plt.title("Google Playstore List of Games")
plt.xlabel("Rating")
plt.ylabel("Reviews")


# **PART 8**
# 

# In[21]:


import matplotlib.pyplot as plt


# In[22]:


classes = ["pyhton","R","AI","ML","DS"]
class_1=[20,30,40,50,60]


# In[23]:


plt.pie([2])


# In[24]:


plt.pie(class_1,labels=classes)
plt.show()


# In[25]:


explode=([0,0,0,0,0.1])
plt.pie(class_1,labels=classes,explode=explode) # explode parameter are used for sliced or highlighted part.
plt.show()


# In[26]:


colors=["c","b","r","y","g"]
plt.pie(class_1,labels=classes,explode=explode,colors=colors)


# In[27]:


plt.pie(class_1,autopct="%0.1f%%",shadow=True,radius=1.4,startangle=270) #autopct="%0.1f%%" is a autopercentage float number and 0.1 means after point one digit show


# In[28]:


textprops={"fontsize":15}
plt.pie(class_1,textprops=textprops)


# In[29]:


wedgeprops={"linewidth":2,"width":5,"edgecolor":"k"}


# In[30]:


plt.pie(class_1,labels=classes,explode=explode,colors=colors,autopct="%1f%%",pctdistance=3,shadow=True,labeldistance=4.5,startangle=360,counterclock=True,wedgeprops=wedgeprops,textprops=textprops,center=(2,3),frame=True,rotatelabels=True)
plt.figure(figsize=(6,5))


# **PART 9**

# In[31]:


import numpy as np


# In[32]:


colors=['r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w','r','w',]
labels=np.ones(20)


# In[33]:


plt.pie([1],colors="k",radius=2.05)
plt.pie(labels,colors=colors,radius=2.0)
plt.pie([1],colors="g",radius=1.8)
plt.pie([1],colors="y",radius=1.6)
plt.pie([1],colors="c",radius=1.3)
plt.pie([1],colors="b",radius=1.1)
plt.pie([1],colors="m",radius=0.9)
plt.pie([1],colors="b",radius=0.31)
plt.pie(labels,colors=colors,radius=0.3)
plt.pie([1],colors="w",radius=0.2)
plt.pie([1],colors="k",radius=0.1)
plt.figure(figsize=(5,5))
plt.show()


# **PART 10 (subplot function)**

# In[34]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random 
from matplotlib import style


# In[35]:


plt.subplot(2,2,1)
plt.pie([1])
plt.subplot(2,2,2)
plt.pie([1,2])
plt.subplot(2,2,3)
plt.pie([1,2,3])
plt.subplot(2,2,4)
plt.pie([1,2,3,4])
plt.show()


# In[36]:


plt.figure(figsize=(16,9))
plt.subplot(3,3,2)


# In[37]:


Days = [1,2,3,4,5,6,7,8,9,10]
Delhi_temp = [32.2,33,35,43,22,23.4,55.2,22.11,31.23,31]
Mumbai_temp=[32,33,45,67,5,4,33,32,22,31]
plt.plot(Days,Delhi_temp,"yo:",linewidth=3,markersize=10,label="Delhi_temparature_record")
plt.plot(Days,Mumbai_temp,"mo--",linewidth=3,markersize=10,label="Mumbai Temparature Record")
plt.xlabel("days",fontsize=13)
plt.ylabel("Temparature",fontsize=13)
plt.legend(loc=1)
plt.grid(color='k',linestyle='-',linewidth=1)
plt.title("Delhi & Mumbai" "Temparature line plot",fontsize=15)
#plt.subplot(3,2,2)


# In[39]:


ml_students_age=np.random.randint(15,30,(50))
py_students_age=np.random.randint(16,35,(50))
bins=[15,20,25,30,35,40]
plt.hist([ml_students_age,py_students_age],bins,rwidth=0.8,histtype="bar",orientation='vertical',color=['k','g'],label=["Ml_students_ages_graph""Py_students_ages_graph"])
plt.title("Ml & Py students age histogram")
plt.xlabel("student age category")
plt.ylabel("No of. students age")
plt.legend()


# In[52]:


classes = ["pyhton","R","AI","ML","DS"]
class_1=[20,30,40,50,60]
class_2=[25,35,45,65,55]
class_3=[33,45,53,11,12]
class_index=np.arange(len(classes))
width = 0.2
plt.bar(class_index,class_1,width,color="b",label="class_1")
plt.bar(class_index+width,class_2,width,color="g",label="class_2")
plt.bar(class_index+width+width,class_3,width,color="r",label="class_3")
plt.xticks(classes_index+width,classes,rotation=15)
plt.title("bar chart of IAIP class bar chart",fontsize=18)
plt.ylabel("classes",fontsize=15)
plt.xlabel("No of students",fontsize=15)
plt.legend()


# In[60]:


df_googleplaystore=pd.read_csv("/Users/pritamsaha/Downloads/store.csv")
x=df_googleplaystore["Rating"]
y=df_googleplaystore["Reviews"]

plt.scatter(x,y,c="g",marker="*",s=100,alpha=0.5,linewidths=10,edgecolor='y')
plt.title("Google play store apps scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")



# In[68]:


classes = ["pyhton","R","AI","ML","DS"]
class_1=[20,30,40,50,60]
explode=[0.03,0,0.1,0,0]
colors=["c","y","k","r","b"]
textprops={"fontsize":15}
plt.pie(class_1,labels=classes,explode=explode,colors=colors,autopct="%0.2f%%",shadow=True,radius=1.4,startangle=270,textprops=textprops)


# In[70]:


plt.subplot(3,2,6,projection="polar",facecolor="k",frameon=True)
plt.show()


# In[ ]:




