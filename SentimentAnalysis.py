import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
import matplotlib.pyplot as plt

sid = SentimentIntensityAnalyzer()

positive = 0
negative = 0
neutral = 0
sizes = []
labels = ('Positive', 'Negative', 'Neutral')
for root,dirs,files in os.walk("news\\"):
    for dire in dirs:
        positive = 0
        negative = 0
        neutral = 0
        sizes = []
        for filename in os.listdir(os.path.join(root,dire)):
            file = open(os.path.join(root,os.path.join(dire,filename)), "r")
            text = file.read()
            ss = sid.polarity_scores(text)
            if (ss['compound'] < -0.2):
                negative = negative + 1
            elif (ss['compound'] > 0.2):
                positive = positive + 1
            else:
                neutral = neutral + 1
        print(dire)
        print('POSITIVE: ', positive)
        print('NEGATIVE: ', negative)
        print('NEUTRAL: ', neutral)
        sum = positive + neutral + negative
        sizes = [(positive/sum)*100, (negative/sum)*100, (neutral/sum)*100]
        fig, ax = plt.subplots()
        ax.pie(sizes, startangle=90, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        plt.title(dire.capitalize())

plt.show()