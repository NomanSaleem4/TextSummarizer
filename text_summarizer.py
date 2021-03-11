from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer
import streamlit as st


# LANGUAGE = "english"



if __name__ == "__main__":
    import nltk 
    nltk.download('punkt')
    st.title('Text Summarizer App by DeepLearningPro')
    desc = "This App generates summary for the plain english text."
    st.write(desc)
    text = st.text_input('Enter Text here')
    summary_length = st.number_input('Enter number of sentences, summary should be based on?', min_value=1, max_value=10, value=2)
    if st.button('Generate Summary'):
        parser = PlaintextParser.from_string(text,Tokenizer("english"))
        # Using LexRank
        summarizer = LexRankSummarizer()
        #Summarize the document with 2 sentences
        summary = summarizer(parser.document, summary_length)
        for sentence in summary:
            # print(sentence)
            st.write(sentence)
 

