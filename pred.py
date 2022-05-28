import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('Hiring_salary.pkl','rb'))


def predict_salary(experience,test_score,interview_score):
    input=np.array([[experience,test_score,interview_score]]).astype(np.float64)
    pred=model.predict(input)
    #pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Salary Prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Hiring Salary Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    experience = st.text_input("experience","Type Here")
    test_score = st.text_input("test_score","Type Here")
    interview_score = st.text_input("interview_score","Type Here")

    if st.button("Predict"):
        output=predict_salary(experience,test_score,interview_score)
        st.success('The hiring salary is {}'.format(output))

if __name__=='__main__':
    main()