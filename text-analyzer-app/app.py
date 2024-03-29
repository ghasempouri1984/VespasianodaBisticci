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

#import seaborn as sns
import altair as alt

# func for LexRank summarization
def sumy_summarizer(docx, num=2):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

# Evaluate Summary
from rouge import Rouge
def evaluate_summary(summary, reference):
    r = Rouge()
    eval_score = r.get_scores(summary, reference)
    eval_score_df = pd.DataFrame(eval_score[0])
    return eval_score_df

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
                    my_summary = sumy_summarizer(raw_text)
                    document_len = {"Original": len(raw_text), "Summary": len(my_summary) }
                    st.write(document_len)  
                    st.write(my_summary)

                    st.info("Rouge Score")
                    #score = evaluate_summary(my_summary, raw_text)
                    eval_df = evaluate_summary(my_summary, raw_text)

                    #st.write(score[0])
                    st.dataframe(eval_df.T)
                    eval_df['metrics']= eval_df.index
                    c = alt.Chart(eval_df).mark_bar().encode(
                        x='metrics', y='rouge-1')
                    st.altair_chart(c)
                    

            with c2:
                with st.expander("Textrank Summary"):
                    my_summary = summarize(raw_text)
                    document_len = {"Original": len(raw_text), "Summary": len(my_summary) }
                    st.write(document_len) 
                    st.write(my_summary)
                    st.info("Rouge Score")
                    eval_df = evaluate_summary(my_summary, raw_text)
                    #st.write(score[0])
                    st.dataframe(eval_df.T)

                    eval_df['metrics']= eval_df.index
                    c = alt.Chart(eval_df).mark_bar().encode(
                        x='metrics', y='rouge-1')
                    st.altair_chart(c)

                    

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
