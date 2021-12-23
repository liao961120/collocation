Collocation
=================


## Installation

```bash
pip install collocation
```

## Usage

```python
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

>>> corpus[:7]
[['物品', '名稱', '：', '學生證'],
 ['拾獲', '地點', '：', '大一女', '前'],
 ['拾獲', '時間', '：', '6', '/', '21'],
 ['18', ':', '20', '左右'],
 ['物品', '描述', '：', '就', '一', '張', '學生證'],
 ['聯絡', '方式', '：', '站', '內', '信'],
 ['其他', '說明', '：', '請', '失主', '或', '朋友', '速速', '聯絡', '喔']]


# Initialize
c = Collocation(corpus, left_window=3, right_window=3)
# Query
>>> c.get_topn_collocates("[臺台]灣", cutoff=3, n=3, by="MI", chinese_only=True)
[('臺灣', '國立',
  {'MI': 9.801006087045614,
   'Xsq': 3560.8618187084653,
   'Gsq': 46.973839463946646,
   'Dice': 0.04519774011299435,
   'DeltaP21': 0.0277504097342154,
   'DeltaP12': 0.12108001346126511,
   'RawCount': 4}),
 ('臺灣', '聯盟',
  {'MI': 9.064040492879409,
   'Xsq': 2133.3656286224623,
   'Gsq': 42.68555772916195,
   'Dice': 0.04020100502512563,
   'DeltaP21': 0.0277296477701336,
   'DeltaP12': 0.0725951622338306,
   'RawCount': 4}),
 ('臺灣', '大學',
  {'MI': 8.428314878476366,
   'Xsq': 3768.760643213294,
   'Gsq': 107.96714978953916,
   'Dice': 0.05804749340369393,
   'DeltaP21': 0.07617749434551055,
   'DeltaP12': 0.046682984348090525,
   'RawCount': 11})]

# Acess documentation of parameters
help(c.get_topn_collocates)
```

### Custom Association Measures

```python
from math import log2
from collocation.association import FisherAttract, Dice


def logDice(O11, O12, O21, O22, E11, E12, E21, E22):
    D = Dice(O11, O12, O21, O22, E11, E12, E21, E22)
    return 14 + log2(D)

c.association_measures = [FisherAttract, logDice]

>>> c.get_topn_collocates("[臺台]灣", cutoff=3, n=3, by="logDice", chinese_only=True)
[('臺灣', '大學',
  {'FisherAttract': 56.04305766162403,
   'logDice': 9.893377580466206,
   'RawCount': 11}),
 ('臺灣', '國立',
  {'FisherAttract': 25.040705008265565,
   'logDice': 9.532394449917003,
   'RawCount': 4}),
 ('臺灣', '聯盟',
  {'FisherAttract': 22.922605012581965,
   'logDice': 9.36337537945635,
   'RawCount': 4})]
```