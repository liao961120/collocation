import re
from .association import MI, Xsq, Gsq, Dice, DeltaP21, DeltaP12, additive_smooth

PAT_CH_CHR = re.compile("[〇一-\u9fff㐀-\u4dbf豈-\ufaff]")


class Collocation:
    association_measures = [
        MI, Xsq, Gsq, Dice, DeltaP21, DeltaP12
    ]

    def __init__(self, corpus, left_window, right_window):
        self.left_window = left_window
        self.right_window = right_window
        self.cooccur_freq = {}
        self.R1_all = {}  # new
        self.C1_all = {}  # new
        self.count_freq(corpus)
        self.N = sum(self.cooccur_freq.values())  # new
    

    def get_topn_collocates(self, node, cutoff, n=10, alpha=0, 
                            chinese_only=True, by="MI"):
        """Retrieve top n collocates of a node

        Parameters
        ----------
        node : str
            Regex pattern describing the node word
        cutoff : int
            The minimum number of coocurrences between the node and a collocate
            needed for the pair to be assign association scores
        n : int, optional
            The number of collocates to return, by default 10
        alpha : int, optional
            Additive smoothing parameter, by default 0. This is usually set
            between 0 and 1
        by : str, optional
            The association measure used for sorting, by default "MI"
            Possible values are the names of the functions in
            :meth:`Collocation.association_measures`
        chinese_only : bool, optional
            Whether to return only collocates that have at least one Chinese
            character, by default True

        Returns
        -------
        list
            A list of tuples (node, collocate, associations)
        """
        node = re.compile(node)
        candidates = []
        for node_, collo_ in self.cooccur_freq:
            if chinese_only:
                if not any(PAT_CH_CHR.match(c) for c in collo_): continue
            if node.match(node_):
                asso = self.association(node=node_, collocate=collo_, 
                                        cutoff=cutoff, alpha=alpha)
                if asso is not None:
                    candidates.append( (node_, collo_, asso) )
        if isinstance(n, int):
            return sorted(candidates, key=lambda x: x[-1][by], reverse=True)[:n]
        else:
            sorted(candidates, key=lambda x: x[-1][by], reverse=True)


    def association(self, node, collocate, cutoff, alpha):
        # Retrieve frequencies
        O11 = self.cooccur_freq.get((node, collocate))
        R1 = self.R1_all.get(node)
        C1 = self.C1_all.get(collocate)
        if O11 is None or R1 is None or C1 is None: return None
        if O11 < cutoff: return None
        R2 = self.N - R1
        O12 = R1 - O11
        O21 = C1 - O11
        O22 = R2 - O21
        O11, O12, O21, O22, E11, E12, E21, E22 = additive_smooth(O11, O12, O21, O22, alpha=alpha)

        stats = { 
                func.__name__: func(O11, O12, O21, O22, E11, E12, E21, E22)\
                    for func in self.association_measures
        }
        stats['RawCount'] = O11

        return stats


    def count_freq(self, sentences):
        for sent in sentences: 
            self.count_freq_sent(sent)


    def count_freq_sent(self, sentence):
        sent_len = len(sentence)
        
        # Sliding window (跑過句子中的每個詞彙)
        for i, node in enumerate(sentence):
            
            # Set window to scan through
            win_left = max(i - self.left_window, 0)
            win_right = min(i + self.right_window + 1, sent_len)
            collocates = sentence[win_left:i] + sentence[i+1:win_right]
        
            for collocate in collocates:
                # Count cooccurance frequency
                k = (node, collocate)
                if k not in self.cooccur_freq:
                    self.cooccur_freq[k] = 0
                self.cooccur_freq[k] += 1

                # Count marginal frequencies
                # Count node marginal frequency
                if node not in self.R1_all: 
                    self.R1_all[node] = 0
                self.R1_all[node] += 1

                # Count collocate marginal frequency
                if collocate not in self.C1_all:
                    self.C1_all[collocate] = 0
                self.C1_all[collocate] += 1
