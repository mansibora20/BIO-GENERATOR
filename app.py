#import libararies
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#create FastAPI() and Jinja2Templates() instances 
app = FastAPI()  #define our API endpoints and handle incoming HTTP requests.
templates = Jinja2Templates(directory="C:/Users/mansi.bora/Desktop/ML Projects/BIO GENERATOR/templates") #pass the directory argument to specify the path to the directory containing our HTML templates.

#GET endpoint at the root URL /. 
@app.get("/", response_class=HTMLResponse) #@app.get decorator specifies that this function should be called in response to a GET request.
async def form(request: Request):  #returns a TemplateResponse object that renders the form.html template
    return templates.TemplateResponse("form.html", {"request": request})


# defines a POST endpoint at the root URL /. 
@app.post("/", response_class=HTMLResponse)  #@app.post decorator specifies that this function should be called in response to a POST request
async def generate_bio(request: Request, name: str = Form(...), age: int = Form(...), profession: str = Form(...), hobby: str = Form(...)):
    bio = f"My name is {name}, I am {age} years old. I am {profession} by profession and in my free time I enjoy {hobby}."
    return templates.TemplateResponse("bio.html", {"request": request, "bio": bio})