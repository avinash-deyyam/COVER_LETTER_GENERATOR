from fastapi import FastAPI, UploadFile, File, Form
import uvicorn
from model import get_cover_letter
import json
import ast

app = FastAPI()

@app.post("/cover_letter")

async def create_upload_file(file: UploadFile = File(...), json_data: str = Form(...)):
    # Assuming the file is a PDF
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}
    
    cl = {}
    content = await file.read()
    data = ast.literal_eval(json_data)
    cl['result'] = get_cover_letter(data, content)
    return json.dumps(cl) 

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)