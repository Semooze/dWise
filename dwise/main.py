import pandas as pd
from fastapi import FastAPI
from starlette.responses import HTMLResponse
from utils import extract_daily_messages, get_daily_messages
from views import render_daily_messages

app = FastAPI()

data = dict()

@app.on_event('startup')
async def startup_event():
    data['data'] = pd.read_csv('data/mini.csv', index_col='id')

@app.get('/')
async def read_root():
    daily_data = get_daily_messages(data['data'])
    days, number_of_message = extract_daily_messages(daily_data)
    return HTMLResponse(render_daily_messages(days, number_of_message))