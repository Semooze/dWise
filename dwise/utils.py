import pandas as pd 
from pythainlp import word_tokenize
from typing import List, Dict

def get_daily_messages(data):
    data["time"]= pd.to_datetime(data["time"]) 
    return data.resample('D', on='time').count()

def extract_daily_messages(data):
    return data.index.strftime('%Y/%m/%d').to_list(), data['message'].to_list()

def get_most_message_accounts(data, number_of_user):
    result = data.groupby(['owner id', 'owner name'], as_index=False).count().sort_values('message', ascending=False)
    return result.head(number_of_user)

def extract_most_accounts(data):
    return [ tuple(x) for x in data[['owner id', 'owner name', 'message']].to_numpy()]

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