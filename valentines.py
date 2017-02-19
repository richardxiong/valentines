# Happy valentines day!
import jieba    #word segmentation
import numpy    #scientific calculation
import codecs   #open unicode 
import pandas   #data analysis
import matplotlib.pyplot as plt 
from wordcloud import WordCloud

from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

file=codecs.open(u"Before Midnight.txt",'r')
content=file.read()
file.close()
segment=[]
segs=jieba.cut(content) #segmentaiton
for seg in segs:
    if len(seg)>1 and seg!='\r\n':
        segment.append(seg)
        
words_df=pandas.DataFrame({'segment':segment})
words_df.head()
stopwords=pandas.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding="utf8")
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"count":numpy.size})
words_stat=words_stat.reset_index().sort_values(by="count",ascending=False) #words_stat print

#%matplotlib
bimg=imread('heart2.png')
wordcloud=WordCloud(background_color="white",mask=bimg,font_path='SimHei.ttf') #
wordcloud=wordcloud.fit_words(words_stat.head(300).itertuples(index=False))
bimgColors=ImageColorGenerator(bimg)
plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()