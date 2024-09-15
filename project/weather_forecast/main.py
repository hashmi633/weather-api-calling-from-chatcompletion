from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
import json


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Starting Application ...!")
    yield 

app: FastAPI =FastAPI(lifespan=lifespan, title="Weather API",
    version="0.0.0",
    servers=[
        {
           "url":   "http://127.0.0.1:8001",
            "description":  "Development Server"
        }
    ])

class WeatherRequest(SQLModel):
    location: str
    unit: str = "fahrenheit"

@app.post('/get_current_weather')
async def get_current_weather(weatherRequest: WeatherRequest):
    location = weatherRequest.location
    unit = weatherRequest.unit
    if "murree" in location.lower():
        return json.dumps({"location": "Murree", "temperature": "10", "unit": "celsius"})
    elif "lahore" in location.lower():
        return json.dumps({"location": "Lahore", "temperature": "72", "unit": "fahrenheit"})
    elif "islamabad" in location.lower():
        return json.dumps({"location": "Islamabad", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})
    
@app.get('/')
async def welcome():
    return {"Welcome": "You can check weather of lahore & islamabad"}

@app.get("/cityweather")
async def city_weather(city: str):
    if "lahore" in city.lower():
        # return{"Answer":"Lahore temperature is 28"}
        return json.dumps({"location": "Murree", "temperature": "10", "unit": "celsius"})