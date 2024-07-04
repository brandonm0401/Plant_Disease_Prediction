from fastapi import FastAPI, File, UploadFile, Request, Query
from fastapi.responses import HTMLResponse, RedirectResponse
import tensorflow as tf
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import io
import numpy as np

app = FastAPI()
model = tf.keras.models.load_model("leaf_classifier.keras")
templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/",response_class = HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html",{'request':request})

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(io.BytesIO(contents))
    image = image.resize((150,150))
    img_array = np.array(image)

    img_array = img_array/255.0
    img_array = img_array.reshape(1,150,150,3)

    prediction = int(np.argmax(model.predict(img_array)))
    return RedirectResponse(url=f"/prediction?prediction={prediction}", status_code=303)

@app.get("/prediction", response_class=HTMLResponse)
async def home_page(request: Request, prediction: int = Query(...)):
    class_labels = ['Healthy','Unhealthy']
    predicted_class = class_labels[prediction]
    return templates.TemplateResponse("index.html", {"request": request, "predicted_class": predicted_class})