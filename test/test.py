#%%
from collocation import Collocation

# Download example data at https://yongfu.name/collocation/sampled_PTTposts.txt
def read_corpus(fp):
    with open(fp, encoding="utf-8") as f:
        corpus = []
        for sent in f.read().split("\n"):
            if sent.strip() == "": continue
            sentence = []
            for tk in sent.split("\u3000"):
                if tk == "": continue
                sentence.append(tk)
            corpus.append(sentence)
    return corpus

corpus = read_corpus("sampled_PTTposts.txt")
corpus[:7]


c = Collocation(corpus, left_window=3, right_window=3)
c.get_topn_collocates("[臺台]灣", cutoff=3, n=5)
# %%
