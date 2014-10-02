import nltk
from collections import Counter
import string
import operator
from decimal import *


def punct(w):
    return len(w)==1 and w in string.punctuation

def isNum(n):
    try:
        float(n) if '.' in n else int(n)
        return True
    except ValueError:
        return False

def get_phrases(sentences):
    phrases=[]
    words=[]
    for sentence in sentences:
        words.extend(map(lambda x:'|' if x in stopword_list else x , nltk.word_tokenize(sentence.lower())))
    phrase=[]
    for w in words:
        if w=='|' or punct(w):
            if len(phrase)>0:
                phrases.append(phrase)
                phrase=[]
        else:
            phrase.append(w)
    return phrases

def wordscore(phrases):
    w_freq= Counter()
    w_deg={}
    p=[]
    for phrase in phrases:
        p.append(Counter(phrase))
        deg = len(filter(lambda x: not isNum(x), phrase))
        for w in phrase:
            if(w_deg.has_key(w)):
                w_deg[w]=w_deg[w]+deg
            else:
                w_deg[w]=deg
    x=[]
    for x in range(len(p)):
        p[0]=p[0]+p[x]
    score={}
    for w in w_deg:
        score[w]=round(Decimal(w_deg[w]),2)/round(Decimal(p[0][w]),2)
    return score

text="""Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."""

stopwords=open("stopwords.txt","r")
stopwords= stopwords.read()
stopword_list=stopwords.split()
sentences=nltk.sent_tokenize(text)
phrases = get_phrases(sentences)
sc=wordscore(phrases)
