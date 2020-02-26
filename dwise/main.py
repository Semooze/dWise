import pandas as pd
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse

from dwise import utils
from dwise.views import render_daily_messages
from dwise import setting
import pickle

app = FastAPI()

data = dict()

@app.on_event('startup')
async def startup_event():
    data_file_path = None
    word_list_path = None
    hashtag_list_path = None
    if setting.mode == 'production':
        data_file_path = setting.ProdEnv.data_file
        word_list_path = setting.ProdEnv.word_file
        hashtag_list_path = setting.ProdEnv.hashtag_file
    elif setting.mode == 'development':
        data_file_path = setting.DevEnv.data_file
        word_list_path = setting.DevEnv.word_file
        hashtag_list_path = setting.DevEnv.hashtag_file
    else:
        data_file_path = setting.TestEnv.data_file
        word_list_path = setting.TestEnv.word_file
        hashtag_list_path = setting.TestEnv.hashtag_file

    data['data'] = pd.read_csv(data_file_path, sep=',', doublequote=True)

    with open(word_list_path, 'rb') as hashtag_reader:
        data['hashtag'] = pickle.load(hashtag_reader)
    with open(hashtag_list_path, 'rb') as word_reader:
        data['word'] = pickle.load(word_reader)

@app.get('/')
async def home_page(request: Request):
    daily_data = utils.get_daily_messages(data['data'])
    days, number_of_message = utils.extract_daily_messages(daily_data)
    accounts = utils.get_most_message_accounts(data['data'])
    top_ten_accounts = utils.extract_most_accounts(accounts, 10)
    messages = utils.get_most_engagement_messges(data['data'], 10)
    top_ten_engagements = utils.extract_most_engagement_messages(messages)
    word_count = utils.make_word_count(data['word'])
    word_cloud = utils.make_word_cloud(word_count, sort='decend', limit=100)
    hashtag_count = utils.make_hashtag_count(data['hashtag'])
    hashtag_cloud = utils.make_word_cloud(hashtag_count, sort='decend', limit=100)
    return render_daily_messages(request, days, number_of_message, top_ten_accounts, top_ten_engagements, word_cloud, hashtag_cloud)
