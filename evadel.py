import streamlit as st
import random as r    # random module
import time

def main():

    choicedWord = st.session_state.choiceWord 
    
    if choicedWord is None:
        wordList=['Fruit','mango','rasberries','Blueberries','watermelon']    # the words in x
        choicedWord=r.choice(wordList)   # d holds whatever word the computer chooses from x
        st.session_state.choiceWord = choicedWord

    st.title("Streamlit Game")

    st.subheader(f"word : :orange[{choicedWord}]")

    def clear_search_text():
        st.session_state["inputText"] = st.session_state.get("widget")
        st.session_state["widget"]= ""
    
    st.text_input('Enter text here', key="widget", on_change=clear_search_text)

    answer = st.session_state.inputText
    if choicedWord == answer:
        st.success('Good!')
        st.session_state.choiceWord = None
        time.sleep(1) # 1 sec
        st.rerun()
    else:
        st.warning('Try Again!')
     
if __name__ == '__main__':
    if "choiceWord" not in st.session_state:
        st.session_state.choiceWord = None
    if "inputText" not in st.session_state:
        st.session_state.inputText = None
             
    main()

