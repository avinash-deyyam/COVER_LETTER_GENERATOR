from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os
from helper import split_text_documents, text_to_doc_splitter, extract_text_from_url, load_pdf
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_cover_letter(json_data, file):
    temperature = 0.7
    append_text = ''
    for key in json_data:
        if key == 'job':
            if json_data[key][0] == 'Paste Job Posting':
                job_jd = text_to_doc_splitter(json_data[key][1])
            else:
                job_jd = extract_text_from_url(json_data[key][1])
                
        elif key == 'resume':
            if json_data[key][0] == 'Paste Resume':
                resume_doc = text_to_doc_splitter(json_data[key][1])
            else:
                resume_doc = load_pdf(file)
                
        elif key in ['focus on particular projects/roles on resume','focus on particular points on job description', 'focus on particular skills']:
            append_text += key + ' such as ' + json_data[key] + '. '
        
        # elif key == 'cover letter length':
        #     append_text += 'Strictly limit cover letter word length' + ' to ' + json_data[key] + '. '
            
        elif key in ['change the format of cover letter', 'change language style']:
            append_text += key + ' to ' + json_data[key] + '. '
            
        elif key == 'others':
            append_text += 'Also, try to include the following requests ' + json_data[key] + '. '
            
        elif key == 'model creativity':
            try:
                temperature = float(json_data[key])
                if not 0 <= temperature <= 1.0:
                    temperature = 0.7
            except:
                pass

    resume_doc.extend(job_jd)
    documents = split_text_documents(resume_doc)

    vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(openai_api_key = openai_api_key))

    coverletter_qa = RetrievalQA.from_chain_type(
        ChatOpenAI(temperature= temperature, model_name='gpt-3.5-turbo', openai_api_key = openai_api_key),
        retriever=vectordb.as_retriever(search_kwargs={'k': 3}),
        chain_type="stuff",
    )

    question = f"""Generate a concise, conversational cover letter for a job. Address the job requirements and candidate's qualifications briefly. Ensure the letter is engaging and ends with the candidate's name from the resume. {append_text}"""
    print(question)
    
    question = question.split(' ')
    if len(question) > 2500:
        question = " ".join(question[:2500])
    else:
        question = " ".join(question)
    
    return coverletter_qa.run(question)