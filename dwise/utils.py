import pandas as pd 
from pythainlp import word_tokenize
from typing import List

def get_daily_messages(data):
    data["time"]= pd.to_datetime(data["time"]) 
    return data.resample('D', on='time').count().dropna()


def extract_daily_messages(data):
    return data.index.strftime('%Y/%m/%d').to_list(), data['message'].to_list()

# def extract_word_from_message(data) -> List[str]:
#     result = list()
#     for sentence in data.message:
#         print(sentence)
#         words = word_tokenize(sentence, engine='deepcut', keep_whitespace=False)
#         # striped_word = [ word.strip() for word in words if word.strip() != '']
#         result.extend(striped_word)
#     print(result)
#     return result