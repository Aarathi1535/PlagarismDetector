from difflib import SequenceMatcher
import streamlit as st
import random
import sqlite3
def get_connection():
    conn = sqlite3.connect("detections.sqlite")
    conn.execute("Create Table Detections(Id text, Plagiarism_Percentage text)")
    return conn
st.title("Plagiarism Detector")
st.markdown("Compare your files to check the percentage of plagiarism present.")
f1 = st.file_uploader("Choose file-1",type='txt')
f2 = st.file_uploader("Choose file-2",type='txt')
stored_list= []
if st.button("Check Plagiarism"):
    random_num = random.randint(1, 1000)
    if random_num not in stored_list:
        stored_list.append(random_num)
    else:
        random_num = random.randint(1, 1000)
    numeric_id = "PD"+str(random_num)
    id = "Your unique-id is: "+ numeric_id
    file1 = f1.getvalue().decode("utf-8")
    file2 = f2.getvalue().decode("utf-8")
    result = SequenceMatcher(None, file1, file2).ratio()
    final = int(result * 100)
    s = "Plagiarism detected is :"+str(final)+"%"
    st.text(s)
    st.text(id)
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO Detections(Id, Plagiarism_Percentage) VALUES (?, ?)', (numeric_id,final))
    conn.commit()


