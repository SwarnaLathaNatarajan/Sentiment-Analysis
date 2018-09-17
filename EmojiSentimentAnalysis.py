from nltk.classify import SklearnClassifier
import random
from sklearn.linear_model import SGDClassifier
from nltk import word_tokenize
f = open('emoji.txt','r', encoding='utf-8')
data = f.read()
lines = data.split('\n')
lines.remove('')

def word_feats(word):
    return dict([(word, True)])

for i in range(len(lines)):
    lines[i] = lines[i].split(',')
    if('$' in lines[i]):
        lines[i].remove('$')
    #print(lines[i])

positive_vocab = []
negative_vocab = []
neutral_vocab = []

for l in lines:
    k = float(l[2])
    if(k > 0.2):
        positive_vocab.append(l[0])
    elif(k < -0.1):
        negative_vocab.append(l[0])
    else:
        neutral_vocab.append(l[0])

# print(neutral_vocab)
# print(positive_vocab)

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = positive_features + negative_features + neutral_features
random.shuffle(train_set)
cls = SklearnClassifier(SGDClassifier())
classifier = cls.train(train_set)

sent = '☺😅😭'
w = word_tokenize(sent)
print(len(sent))