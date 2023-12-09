## Cover Letter Generation Application

### Project Overview
The cover letter generation application is designed to create customized cover letters using job descriptions and candidate resumes. Leveraging advanced language models and embeddings, it generates tailored cover letters aligned with specific job postings and candidate qualifications.

### Approach and Methodology
This project integrates advanced language models with data from job descriptions and candidate resumes. The application harmonizes Large Language Model (LLM) capabilities with the langchain to generate cover letters. Precise prompts guide the language model to extract relevant information, facilitating the creation of personalized cover letters.

### Cover Letter Generation
Using the extracted information, the system dynamically generates cover letters that highlight the candidate's qualifications, skills, and experiences relevant to the job description. Users can also select items from a dropdown to guide the LLM to focus on specific aspects of the job description or resume.

### User Interface
The application offers an intuitive interface accessible via an API. It facilitates the input of job descriptions and resumes, generating customized cover letters through an interactive Streamlit-based interface.

---

### Input
The application accepts the following inputs:
1. **Job Description:** Details about the job, including responsibilities, requirements, and company information. Users can paste the job description or URL, selectable from the dropdown. This application is designed to take job descriptions from LinkedIn.
2. **Candidate Resume:** Information regarding the candidate's skills, experiences, and qualifications. Users can paste the job description or upload a PDF, selectable from the dropdown.
3. **Customized Inputs:** Users can guide the LLM by specifying their interests. Here are some customized options:
   - Focus on particular projects/roles on the resume - It tells the LLM to focus on any     
     particular aspect of the user role or project.
   - Focus on specific points on the job description - It tells the LLM to focus on any 
     particular aspect of the job description.
   - Change the format of the cover letter - User can suggest any particular format of the cover 
     letter or type 'new' to create a new format.
   - Focus on particular skills - It tells the LLM to focus on any particular skill of the user.
   - Change language style - User can suggest any particular language style or type 'new' to 
     create a new style.
   - cover letter length - It helps to restrict the word count of the cover letter
   - model creativity - Values between 0 and 1 with increasing creativity. It is the temperature 
     parameter used in LLMs.
   - others - User can suggest any other preference.

### Output
The system produces a personalized cover letter tailored to the job description, candidate's qualifications, and other parameters.

### Tools Used
This project harnesses the capabilities of Large Language Models (LLMs) and integrates them into an interactive Streamlit-based interface, API, and Docker for cover letter generation.

---

## File Structure

[api.py](api.py) This module contains POST API built using FastAPI. This can be accessed from streamlit or browser or commandline.

[model.py](model.py) This module contains cover letter generation function which is used in the API to return the final output.

[app.py](app.py) This module helps to create UI and select various options.

[helper.py](helper) This module helps to scrape the LinkedIn job posting, convert pdf to documents, and text to documents.

[requirements.txt](requirements.txt) This file contains the necessary packages required for this project.


## Prerequisites

Following are the steps required to follow to run the application smoothly.

* Create a virtual environment and activate it
```python
python3 -m venv cl
source cl/bin/activate 
```

* Clone the repository
```bash
git clone https://github.com/avinash-deyyam/COVER_LETTER_GENERATOR
cd COVER_LETTER_GENERATOR
```

* Upgrade the libraries
```bash
pip install --upgrade pip
pip install --upgrade setuptools
```

* Install the packages from requirements file
```bash
pip install -r requirements.txt
```
  
There are few things that are mandatory to give to run the application.

(1) API host address (default local)

(2) OPENAI API key

These are stored as environmental variables in .env file.

* Run [api.py](api.py) to start the API
```bash
python3 api.py
```

* Run [app.py](app.py) to start the web app
```bash
streamlit run app.py
```

## Usage
To get started, follow these steps:

1. Paste the job description or LinkedIn url
2. Paste the resume or upload a pdf
3. Select customised options 

