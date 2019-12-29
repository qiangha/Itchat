import re
import jieba # pip install if u have not
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

def draw_word_cloud():
    data= pd.read_csv('friends.csv') 
    siglist = []
    for i in data['Signature']:
        try:
            signature = i.strip().replace('emoji','').replace('span','').replace('class','')
            rep = re.compile('1f\d+\w*|[<>/=]')  
            signature = rep.sub('', signature)
            siglist.append(signature)
        except:
            pass
    text = ''.join(siglist)



    #Draw word cloud
    word_list = jieba.cut(text, cut_all=True)
    word_space_split = ' '.join(word_list)


    plt.figure(figsize=(20, 10))

    font ='./SimHei.ttf'

    my_wordcloud = WordCloud(background_color="white", max_words=200,
                         max_font_size=100, font_path=font, width =1400, height =1400,  random_state=42, margin=2).generate(word_space_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.title('Vernica friend signature word cloud')
    plt.show()

