from dwise.utils import get_daily_messages, extract_daily_messages, extract_word_from_message, get_most_message_user
import pandas as pd
import pytest


@pytest.fixture
def sample_data():
    data = pd.read_csv('test/test_data/sample.csv')
    return data


@pytest.fixture
def message_missing_data():
    data = pd.read_csv('test/test_data/message_missing.csv')
    return data


def test_be_able_to_group_data_by_day(sample_data):
    daily_message = get_daily_messages(sample_data)
    assert daily_message['message'].loc['2019-01-01'] == 15
    assert daily_message['message'].loc['2019-01-02'] == 21
    assert daily_message['message'].loc['2019-01-03'] == 8


def test_convert_time_format(sample_data):
    daily_message = get_daily_messages(sample_data)
    days, message_counts = extract_daily_messages(daily_message)
    assert days == ['2019/01/01', '2019/01/02', '2019/01/03']
    assert message_counts == [15, 21, 8]


@pytest.fixture
def message_missing_data():
    data = pd.read_csv('test/test_data/message_missing.csv')
    return data


def test_be_able_to_group_data_by_day_when_some_row_contain_empty_message(message_missing_data):
    daily_message = get_daily_messages(message_missing_data)
    assert daily_message['message'].loc['2019-01-01'] == 4
    assert daily_message['message'].loc['2019-01-03'] == 2

def test_be_able_to_find_account_who_has_most_messages()
    users = get_most_message_user(10)
    assert users == []



# @pytest.fixture
# def word_test_data():
#     data = pd.read_csv('test/test_data/word_test.csv')
#     return data


# def test_be_able_to_cut_word_from_message(word_test_data):
#     actual = extract_word_from_message(word_test_data)
#     expect = [
#         '101','.', 'ชีวิต','ไม่','ง่ายดาย','ชีวิต','ช่าง','วุ่นวาย','เก๊ง','เก๊ง เก๊ง เก๊ง เที่ยง',
#         'คืน','แล้ว','จ้า','Sometimes','People','ask','what','keeps',
#         'me','Going','And','in','truth','it','comes','from','Knowing','I',
#         'have','you','To','save','my','day',
#     ]
#     assert actual == expect

