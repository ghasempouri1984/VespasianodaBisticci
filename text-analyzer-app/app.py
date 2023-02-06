import streamlit as st

# additional pkgs
# text rank algo
from gensim.summarization import summarize

# lex rank algo
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# eda pkgs
import pandas as pd

# data viz
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # Backend

import seaborn as sns

# func for LexRank summarization
def sumy_summarizer(docx, num=2):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def main():

    st.title("Summarizer App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter Text Here")
        if st.button("Summarize"):

            with st.expander("Original Text"):
                st.write(raw_text)
            
            #Layout
            c1, c2 = st.columns(2)
            
            with c1:
                with st.expander("LexRank Summary"):
                    pass
            
            with c2:
                with st.expander("Textrank Summary"):
                    my_summary = summarize(raw_text)
                    st.write(my_summary)



    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
