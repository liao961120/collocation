#%%
from collocation import Collocation

# Prepare corpus data
# https://yongfu.name/collocation/sampled_PTTposts.txt
corpus = []
with open("sampled_PTTposts.txt", encoding="utf-8") as f:
    for sent in f.read().split("\n"):
        if sent.strip() == "": continue
        sentence = []
        for tk in sent.split("\u3000"):
            if tk == "": continue
            sentence.append(tk)
        corpus.append(sentence)

corpus[:7]

# Initialize
c = Collocation(corpus, left_window=3, right_window=3)
# Query
c.get_topn_collocates("[臺台]灣", cutoff=3, n=3, by="MI", chinese_only=True)

# Acess documentation of parameters
help(c.get_topn_collocates)


# %%
from math import log2
from collocation.association import FisherAttract, Dice


def logDice(O11, O12, O21, O22, E11, E12, E21, E22):
    D = Dice(O11, O12, O21, O22, E11, E12, E21, E22)
    return 14 + log2(D)

c.association_measures = [FisherAttract, logDice]
c.get_topn_collocates("[臺台]灣", cutoff=3, n=3, by="logDice", chinese_only=True)
# %%
