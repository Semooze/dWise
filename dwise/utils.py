import pandas as pd 
from pythainlp import word_tokenize
from typing import List, Dict, Union

def get_daily_messages(data, message=None):
    if message:
        filter_cond = data["message"].str.find(message) != -1
        data = data.where(filter_cond).dropna()
        if len(data) == 0:
            return None
    data["time"]= pd.to_datetime(data["time"]) 
    return data.resample('D', on='time').count()

def extract_daily_messages(data):
    return data.index.strftime('%Y/%m/%d').to_list(), data['message'].to_list()

def get_most_message_accounts(data):
    return data.groupby(['channel', 'owner id', 'owner name'], as_index=False).count().sort_values(['channel', 'message'], ascending=False)

def extract_most_accounts(data, number_of_user=None):
    if number_of_user is None:
        youtubes = data.where(data["channel"] == "youtube").dropna()['owner name'].to_list()
        websites = data.where(data["channel"] == "website").dropna()['owner name'].to_list()
        twitters = data.where(data["channel"] == "twitter").dropna()['owner name'].to_list()
        pantips = data.where(data["channel"] == "pantip").dropna()['owner name'].to_list()
        instagrams = data.where(data["channel"] == "instagram").dropna()['owner name'].to_list()
        facebooks = data.where(data["channel"] == "facebook").dropna()['owner name'].to_list()
    else:
        youtubes = data.where(data["channel"] == "youtube").dropna()['owner name'].head(number_of_user).to_list()
        websites = data.where(data["channel"] == "website").dropna()['owner name'].head(number_of_user).to_list()
        twitters = data.where(data["channel"] == "twitter").dropna()['owner name'].head(number_of_user).to_list()
        pantips = data.where(data["channel"] == "pantip").dropna()['owner name'].head(number_of_user).to_list()
        instagrams = data.where(data["channel"] == "instagram").dropna()['owner name'].head(number_of_user).to_list()
        facebooks = data.where(data["channel"] == "facebook").dropna()['owner name'].head(number_of_user).to_list()
    return zip(youtubes, websites, twitters, pantips, instagrams, facebooks)

def get_most_engagement_messges(data, number_of_message):
    return data.sort_values('engagement', ascending=False).head(number_of_message)

def extract_most_engagement_messages(data):
    return [ tuple(x) for x in data[['message', 'engagement']].to_numpy()]
    
def extract_word_from_message(data) -> List[str]:
    result: List = list()
    for sentence in data.message:
        words = word_tokenize(sentence, engine='newmm', keep_whitespace=False)
        striped_word = [ word.strip() for word in words if word.strip() != '']
        result.extend(striped_word)
    return result

def filter_word_from_list(data: List, message) -> List[str]:
    return [ word for word in data if word.find(message) != -1]

def make_word_count(words: List) -> Dict:
    result: Dict = dict()
    for word in words:
        if result.get(word):
            result[word] += 1
        else:
            result[word] = 1
    return result

def make_hashtag_count(words: List) -> Dict:
    result: Dict = dict()
    for word in words:
        if word[0] != '#':
            continue
        if len(word) == 1:
            continue
        if result.get(word):
            result[word] += 1
        else:
            result[word] = 1
    return result

def make_word_cloud(word_count: Dict, sort=None, limit=None) ->List[Dict]:
    result: List = list()
    for key, value in word_count.items():
        result.append({
            'name': key,
            'weight': value
        })
    if sort == 'ascend':
        result.sort(key=lambda x: x['weight'])
    elif sort == 'decend':
        result.sort(key=lambda x: x['weight'], reverse=True)
    if limit:
        return result[:limit]
    return result