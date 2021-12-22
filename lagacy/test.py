#%%
with open("sampled_PTTposts.txt", encoding="utf-8") as f:
    corpus = []
    for sent in f.read().split("\n"):
        if sent.strip() == "": continue
        sentence = []
        for tk in sent.split("\u3000"):
            if tk == "": continue
            sentence.append(tk)
        corpus.append(sentence)


def count_freq_sent(sentence, left_window, right_window):
    cooccur_freq = {} # 共現頻率資料
    sent_len = len(sentence)
    # Sliding window (跑過句子中的每個詞彙)
    for i, node in enumerate(sentence):
        # Set window size to scan through
        win_left = max(i - left_window, 0)
        win_right = min(i + right_window + 1, sent_len)
        collocates = sentence[win_left:i] + sentence[i+1:win_right]
        for collocate in collocates:
            # Count cooccurance frequency
            k = (node, collocate)
            if k not in cooccur_freq:
                cooccur_freq[k] = 0
            cooccur_freq[k] += 1
    return cooccur_freq
# %%
