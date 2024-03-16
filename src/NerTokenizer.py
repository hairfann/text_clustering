"""
Known errors:
    Trump is sometimes tagged as an ORG
    U.S. is sometimes tagged as a PERSON
"""

from sklearn.base import TransformerMixin
class NERTokenizer(TransformerMixin):
    """If 'tag' is True, Person entities .startswith("*") and other entities deemed "good" .startswith("&")"""

    def fit(self, X, *_):
        return self
    
    @staticmethod
    def separate_tags(text):
        revised_text = []
        for ent_ in text:
            if ent_[2] == "O":
                continue
            else: 
                if ent_[3] == "O":
                    con_tag = ''
                    ent_type = ent_[3]
                    revised_text.append((ent_[0], con_tag, ent_type))
                else:
                    con_tag = ent_[3].split("-")[0]
                    ent_type = ent_[3].split("-")[1]
                    revised_text.append((ent_[0], con_tag, ent_type))
        return revised_text


    def transform(self, X, *_):
        from underthesea import ner

        tokenized_corpus = []
        toks = []
        good_ents = ["PER","LOC","ORG"]
        continue_tags = ["B","I"]

        for text in X:
            toks = []
            #Named entities variable
            cleaned_text = separate_tags(ner(text))
            for index, tok in enumerate(cleaned_text):
                if tok[1] in continue_tags and tok[2] in good_ents:
                    if tok[1] == "B":
                        if tok[2] != "PER":
                            toks.append("&" + str(tok[0]).lower())
                        elif tok[2] == "PER":
                            toks.append("*" + str(tok[0]).lower())
                    else:                        
                        toks.append(str(tok[0]).lower())
                else:  
                    toks.append(str(tok[0]).lower())
            tokenized_corpus.append(toks)
        return tokenized_corpus
    