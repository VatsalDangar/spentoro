import os
from fastapi import FastAPI
from services import openai_service
from utils import whatapp_utils

app = FastAPI()

@app.get('/')
async def root():
    return {"Baav":"Baby"}
