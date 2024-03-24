from difflib import SequenceMatcher
import streamlit as st
st.title("Plagiarism Detector")
st.markdown("Compare your files to check the percentage of plagiarism present.")
f1 = st.file_uploader("Choose file-1",type='txt')
f2 = st.file_uploader("Choose file-2",type='txt')

if st.button("Check Plagiarism"):
    file1 = f1.getvalue().decode("utf-8")
    file2 = f2.getvalue().decode("utf-8")
    result = SequenceMatcher(None, file1, file2).ratio()
    final = int(result * 100)
    s = "Plagiarism detected is :"+str(final)+"%"
    st.text(s)


