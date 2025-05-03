from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
   "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    image = Image.open(file.file)
    text = pytesseract.image_to_string(image)
    return {"text": text}