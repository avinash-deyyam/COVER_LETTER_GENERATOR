import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
import ast

load_dotenv()
host_address = os.getenv("host_address")

def main():
    st.title('Cover Letter Generator')
    json_data = {}
    
    # Dropdown to select between job description options
    options = [ "Paste URL of the Job Posting", "Paste Job Posting"]
    choice = st.selectbox("Choose an option for job posting", options)
    
    if choice == "Paste Job Posting":
        job_text = st.text_area("Paste Job Posting")
        
    elif choice == "Paste URL of the Job Posting":
        job_text = st.text_area("Paste URL") 
              
    json_data['job'] = [choice, job_text]
        
    # Dropdown to select between resume options
    options = ["Paste Resume", "Upload PDF"]
    choice = st.selectbox("Choose an option for resume", options)
    
    if choice == "Paste Resume":
        resume_text = st.text_area("Paste Resume")
        
    elif choice == "Upload PDF":
        resume_text = st.file_uploader("Upload PDF", type=["pdf"], accept_multiple_files=False)
        
    json_data['resume'] = [choice, resume_text]

    options = ["focus on particular projects/roles on resume", "focus on particular points on job description", 
              "change the format of cover letter", "focus on particular skills",
              "change language style", "cover letter length","model creativity", "others"]

    selected_options = st.multiselect("Select options for customised outputs", options)

    for option in selected_options:
        if option == "change language style" or option == "change the format of cover letter":
            text_input = st.text_area(f"Specificy format/style or enter NEW on {option}")
            
        elif option == 'model creativity':
            text_input = st.text_area(f"Enter value between 0 and 1 for {option}")
            
        else:
            text_input = st.text_area(f"Enter text for {option}")
            
        json_data[option] = text_input
        
    with st.form('my_form'):
      submitted = st.form_submit_button('Submit')
      
    if submitted:
        
        # URL of your FastAPI endpoint
        url = f"http://{host_address}/cover_letter"  # Replace with your API endpoint URL

        # Send POST request to the FastAPI endpoint
        if json_data['resume'][0] == 'Upload PDF':
            file_content = json_data['resume'][1].read()
            json_data['resume'][1] = ''
            files = {"file": ("file.pdf", file_content, "application/pdf")}
            data = {"json_data": str(json_data)}
            response = requests.post(url ,files=files , data=data)
            
        else:
            files = {"file": ("file.pdf", '', "application/pdf")}
            data = {"json_data": str(json_data)}
            response = requests.post(url ,files=files , data=data)

        # Print the response
        output = response.json()
        output = ast.literal_eval(output)
        st.write(output['result'])
        
            
if __name__ == "__main__":
    main()  

