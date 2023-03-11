from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import openai
from fastapi.templating import Jinja2Templates
import re

app = FastAPI(debug=True)
templates = Jinja2Templates(directory="C:/Users/mansi.bora/Desktop/ML Projects/BIO GENERATOR/templates/")

# set up OpenAI API key
openai.api_key = "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"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def generate_bio(request: Request, name: str = Form(...), age: str = Form(...), profession: str = Form(...), hobbies: str = Form(...)):
    # use OpenAI to generate bio
    prompt = f"My name is {name}, I'm {age} years old and I work as a {profession}. My interests include {hobbies}."
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=300)
    bio = response.choices[0].text

    # return generated bio
    return templates.TemplateResponse("bio.html", {"request": request, "name": name, "bio": bio})



