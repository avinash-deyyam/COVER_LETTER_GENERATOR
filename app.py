import streamlit as st
from main import get_cover_letter

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
        output = get_cover_letter(json_data)
        st.write(output)
        
            
if __name__ == "__main__":
    main()  

