Collocation
=================


## Install

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
c.get_topn_collocates("[臺台]灣", cutoff=3, n=3, by="MI", chinese_only=True)
[('臺灣', '主體性',
  {'MI': 10.260437705682913,
   'Xsq': 4899.751374916442,
   'Gsq': 50.46859378066087,
   'Dice': 0.02666666666666667,
   'DeltaP21': 0.013881338057636753,
   'DeltaP12': 0.33306534863488213,
   'RawCount': 4}),
 ('臺灣', '師範',
  {'MI': 9.260437705682913,
   'Xsq': 2445.9071435603837,
   'Gsq': 44.12442832538992,
   'Dice': 0.02564102564102564,
   'DeltaP21': 0.013870011810758549,
   'DeltaP12': 0.16639867893371077,
   'RawCount': 4}),
 ('臺灣', '國立',
  {'MI': 8.801006087045614,
   'Xsq': 3553.4674791397297,
   'Gsq': 82.8726217054829,
   'Dice': 0.04519774011299435,
   'DeltaP21': 0.027723034251199794,
   'DeltaP12': 0.12094789748256553,
   'RawCount': 8})]
```
