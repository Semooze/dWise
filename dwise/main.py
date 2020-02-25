import pandas as pd
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse

from dwise import utils
from dwise.views import render_daily_messages
from dwise import setting
app = FastAPI()

data = dict()

@app.on_event('startup')
async def startup_event():
    file_path = None
    if setting.mode == 'production':
        file_path = setting.prod_file
    elif setting.mode == 'development':
        file_path = setting.dev_file
    else:
        file_path = setting.test_file
    data['data'] = pd.read_csv(file_path, sep=',', doublequote=True)

@app.get('/')
async def home_page(request: Request):
    daily_data = utils.get_daily_messages(data['data'])
    days, number_of_message = utils.extract_daily_messages(daily_data)
    accounts = utils.get_most_message_accounts(data['data'])
    top_ten_accounts = utils.extract_most_accounts(accounts, 10)
    messages = utils.get_most_engagement_messges(data['data'], 10)
    top_ten_engagements = utils.extract_most_engagement_messages(messages)
    words = utils.extract_word_from_message(data['data'])
    word_count = utils.make_word_count(words)
    word_cloud = utils.make_word_cloud(word_count, sort='decend', limit=100)
    hashtag_count = utils.make_hashtag_count(words)
    hashtag_cloud = utils.make_word_cloud(hashtag_count, sort='decend', limit=100)
    return render_daily_messages(request, days, number_of_message, top_ten_accounts, top_ten_engagements, word_cloud, hashtag_cloud)
