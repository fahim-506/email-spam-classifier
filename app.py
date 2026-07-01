import streamlit as st
import pickle

# Load model
with open("notebooks/SVM_TF_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Email Spam Classifier")
st.write("Enter an email message below to classify it as Ham or Spam.")

email_text = st.text_area("Enter email content:")

if st.button("Classify"):
    if email_text.strip():
        prediction = model.predict([email_text])

        # If labels are encoded as 0=ham, 1=spam
        if prediction[0] == 1:
            st.error("Spam Email")
        else:
            st.success("Ham Email")

        # show raw prediction
        st.write("Prediction:", prediction[0])

    else:
        st.warning("Please enter some email text.")