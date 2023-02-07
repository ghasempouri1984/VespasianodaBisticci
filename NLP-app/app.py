import streamlit as st
import streamlit.components.v1 as stc

# additional pkgs
# eda pkgs
import pandas as pd

# nlp pkgs
import spacy

nlp = spacy.load('en_core_web_lg')
from spacy import displacy
# text cleaning pkgs
import neattext as nt
import neattext.functions as nfx

# funcs
def text_analyzer(my_text):
    docx = nlp(my_text)
    allData = [(token.text, token.shape_,token.pos_,token.tag_,token.lemma_,token.is_alpha,token.is_stop) for token in docx]
    df = pd.DataFrame(allData, columns=['Token', 'shape', 'PoS', 'Tag', 'Lemma', 'IsAlpha', 'Is_Stopword'])
    return df

def get_entities(my_text):
    docx = nlp(my_text)
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    return entities

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding:1rem">{}</div>"""
# @st.cache
def render_entitis(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style="ent")
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)
    return result

def main():
    st.title("NLP App with StreamLit")
    menu = ["Home", "NLP(files)", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home: Analyze Text:")
        raw_text = st.text_area("Enter Text Here")
        num_of_most_common = st.sidebar.number_input("Most Common Tokens", 5, 15)
        if st.button("Analyze"):

            with st.expander('Original Text'):
                st.write(raw_text)
            
            with st.expander('Text Analysis'):
                token_result_df = text_analyzer(raw_text)
                st.dataframe(token_result_df)
                #st.write(raw_text)
            
            with st.expander('Entities'):
                #entity_result = get_entities(raw_text)
                #  st.write(entity_result)

                entity_result = render_entitis(raw_text)
                stc.html(entity_result, height=1000, scrolling=True)

            # Layouts
            col1,col2 = st.columns(2)

            with col1:
                with st.expander("Word Stats"):
                    pass
                
                with st.expander("Top Keywords"):
                    pass
                
                with st.expander("Sentiment"):
                    pass
            
            with col2:
                with st.expander("Plot Word Freq"):
                    pass

                with st.expander("Plot Part of Speech"):
                    pass

                with st.expander("Plot WordCloud"):
                    pass

            with st.expander("Download Text Analysis Results "):
                pass
            


            
    
    elif choice == "NLP(files)":
        st.subheader("NLP Task")
    
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()