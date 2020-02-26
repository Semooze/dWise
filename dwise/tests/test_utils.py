from dwise.utils import *
import pandas as pd
import pytest


@pytest.fixture
def sample_data():
    data = pd.read_csv('tests/test_data/sample.csv')
    return data


def test_be_able_to_group_data_by_day(sample_data):
    daily_message = get_daily_messages(sample_data)
    assert daily_message['message'].loc['2019-01-01'] == 15
    assert daily_message['message'].loc['2019-01-02'] == 21
    assert daily_message['message'].loc['2019-01-03'] == 8

def test_be_able_to_group_data_by_day_with_filter_message(sample_data):
    daily_message = get_daily_messages(sample_data, filter_keyword='ชม')
    assert daily_message['message'].loc['2019-01-02'] == 1
    assert daily_message['message'].loc['2019-01-03'] == 1
    daily_message = get_daily_messages(sample_data, filter_keyword='Happy')
    assert daily_message['message'].loc['2019-01-01'] == 4
    daily_message = get_daily_messages(sample_data, filter_keyword='happy')
    assert daily_message is None

def test_convert_time_format(sample_data):
    daily_message = get_daily_messages(sample_data)
    days, message_counts = extract_daily_messages(daily_message)
    assert days == ['2019/01/01', '2019/01/02', '2019/01/03']
    assert message_counts == [15, 21, 8]


@pytest.fixture
def message_missing_data():
    data = pd.read_csv('tests/test_data/message_missing.csv')
    return data


def test_be_able_to_group_data_by_day_when_some_row_contain_empty_message(message_missing_data):
    daily_message = get_daily_messages(message_missing_data)
    assert daily_message['message'].loc['2019-01-01'] == 4
    assert daily_message['message'].loc['2019-01-03'] == 2


@pytest.fixture
def account_data():
    data = pd.read_csv('tests/test_data/account.csv')
    return data


def test_be_able_to_find_account_who_has_most_messages(account_data):
    accounts = get_most_message_accounts(account_data)
    assert accounts.iloc[0]['channel'] == 'youtube'
    assert accounts.iloc[0]['owner name'] == 'youtube_4'
    assert accounts.iloc[1]['owner name'] == 'youtube_3'
    assert accounts.iloc[2]['owner name'] == 'youtube_2'
    assert accounts.iloc[3]['owner name'] == 'youtube_1'
    assert accounts.iloc[4]['channel'] == 'website'
    assert accounts.iloc[8]['channel'] == 'twitter'
    assert accounts.iloc[12]['channel'] == 'pantip'
    assert accounts.iloc[16]['channel'] == 'instagram'

def test_be_able_to_filter_top_account_by_keyword(account_data):
    accounts = get_most_message_accounts(account_data, filter_keyword="test")
    assert accounts.iloc[0]['owner name'] == 'youtube_4'
    assert accounts.iloc[1]['owner name'] == 'youtube_3'
    assert accounts.iloc[2]['owner name'] == 'web_site_4'
    assert accounts.iloc[3]['owner name'] == 'web_site_3'
    accounts = get_most_message_accounts(account_data, filter_keyword="mano")
    assert accounts is None



#TODO
# def test_be_able_to_find_account_who_has_most_messages_when_some_row_contain_empty_message(message_missing_data):
#     daily_message = get_daily_messages(message_missing_data)
#     assert daily_message['message'].loc['2019-01-01'] == 4
#     assert daily_message['message'].loc['2019-01-03'] == 2
#'twitter', 'facebook', 'pantip', 'youtube', 'website', 'instagram'


def test_convert_account_format(account_data):
    accounts = get_most_message_accounts(account_data)
    actual = extract_most_accounts(accounts, 3)
    expect = [
        ('youtube_4', 'web_site_4', 'twitter_4','pantip_4', 'instagram_4', 'facebook_4'),
        ('youtube_3', 'web_site_3', 'twitter_3','pantip_3', 'instagram_3', 'facebook_3'),
        ('youtube_2', 'web_site_2', 'twitter_2','pantip_2', 'instagram_2', 'facebook_2')
    ]
    assert list(actual) == expect


@pytest.fixture
def engagement_data():
    data = pd.read_csv('tests/test_data/engagement.csv')
    return data


def test_be_able_to_find_message_which_has_most_engagement(engagement_data):
    messages = get_most_engagement_messges(engagement_data, 10)
    assert messages.iloc[0]['message'] == '@minevith เค ยังไม่เจอเลยเนี่ย'
    assert messages.iloc[0]['engagement'] == 9053
    assert messages.iloc[1]['message'] == '@seongwooskrtx มินเมดด'
    assert messages.iloc[1]['engagement'] == 8170
    assert (
        messages.iloc[2]['message']
        == '101. ชีวิตไม่ง่ายดาย ชีวิตช่างวุ่นวาย .https://t.co/XduZPZarwd'
    )
    assert messages.iloc[2]['engagement'] == 8102
    assert pd.isna(messages.iloc[3]['message'])
    assert messages.iloc[3]['engagement'] == 7234
    assert (
        messages.iloc[4]['message']
        == 'อันนี้ๆๆๆ น่ารักมากเลยอ่ะ น้องไปเเกล้งพี่ เเต่พี่ไปตีกลับผิดคน เเล้วคนน้องก็เเอบอมยิ้มไปดิ ฮืออ #랜덤으로_좋아하는_냬롱_짤 https://t.co/gv5kF3b3Le'
    )
    assert messages.iloc[4]['engagement'] == 5306
    messages = get_most_engagement_messges(engagement_data, 3)
    assert messages.engagement.count() == 3
    assert messages.iloc[0]['engagement'] == 9053
    assert messages.iloc[1]['engagement'] == 8170
    assert messages.iloc[2]['engagement'] == 8102
    #'twitter', 'facebook', 'pantip', 'youtube', 'website', 'instagram'

def test_be_able_to_filter_message_by_keyword(engagement_data):
    messages = get_most_engagement_messges(engagement_data, 3, 'น่ารัก')
    assert messages.iloc[0]['engagement'] == 5306
    assert messages.iloc[1]['engagement'] == 3397
    assert len(messages) == 2
    messages = get_most_engagement_messges(engagement_data, 3, 'test')
    assert messages is None

def test_convert_message_by_engagement_format(engagement_data):
    messages = get_most_engagement_messges(engagement_data, 3)
    actual = extract_most_engagement_messages(messages)
    assert actual == [
        ('@minevith เค ยังไม่เจอเลยเนี่ย', 9053),
        ('@seongwooskrtx มินเมดด', 8170),
        ('101. ชีวิตไม่ง่ายดาย ชีวิตช่างวุ่นวาย .https://t.co/XduZPZarwd', 8102),
    ]


@pytest.fixture
def word_test_data():
    data = pd.read_csv('tests/test_data/word_test.csv')
    return data

    # TODO Due to unstable of cutting word library there is no proper way to test it right now.
    # def test_be_able_to_cut_word_from_message(word_test_data):
    #     actual = extract_word_from_message(word_test_data)
    #     expect = [
    #         '101','.', 'ชีวิต','ไม่','ง่ายดาย','ชีวิต','ช่าง','วุ่นวาย','เก๊ง','เก๊ง เก๊ง เก๊ง เที่ยง',
    #         'คืน','แล้ว','จ้า','Sometimes','People','ask','what','keeps',
    #         'me','Going','And','in','truth','it','comes','from','Knowing','I',
    #         'have','you','To','save','my','day',
    #     ]
    #     assert actual == expect
    #     assert True == True

def test_be_able_to_filter_word_from_list():
    assert ['testครับ', 'ครับ กินได้'] == filter_word_from_list(['testครับ', 'มาเที่ยว', 'ครับ กินได้', 'word'], 'ครับ')

def test_be_able_to_make_word_count():
    actual = make_word_count(
        ['test', 'test', 'me', 'ทดสอบ', '12354', '12', '9', '9', 'ทดสอบ', 'test']
    )
    assert actual == {'test': 3, 'ทดสอบ': 2, 'me': 1, '12354': 1, '12': 1, '9': 2}


def test_be_able_to_produce_highland_format_for_word_cloud():
    actual = make_word_cloud({'test': 3, 'ทดสอบ': 2, 'me': 1, '12354': 1, '12': 1, '9': 2})
    assert actual == [
        {'name': 'test', 'weight': 3},
        {'name': 'ทดสอบ', 'weight': 2},
        {'name': 'me', 'weight': 1},
        {'name': '12354', 'weight': 1},
        {'name': '12', 'weight': 1},
        {'name': '9', 'weight': 2},
    ]

def test_be_able_to_sort_and_limit_word_clound():
    actual = make_word_cloud({'me': 1, 'ทดสอบ': 2, '12354': 1, 'test': 3, '12': 1, '9': 2}, sort='decend')
    assert actual == [
        {'name': 'test', 'weight': 3},
        {'name': 'ทดสอบ', 'weight': 2},
        {'name': '9', 'weight': 2},
        {'name': 'me', 'weight': 1},
        {'name': '12354', 'weight': 1},
        {'name': '12', 'weight': 1}
    ]
    actual = make_word_cloud({'me': 1, 'ทดสอบ': 2, '12354': 1, 'test': 3, '12': 1, '9': 2}, sort='ascend')
    assert actual == [
        {'name': 'me', 'weight': 1},
        {'name': '12354', 'weight': 1},
        {'name': '12', 'weight': 1},
        {'name': 'ทดสอบ', 'weight': 2},
        {'name': '9', 'weight': 2},
        {'name': 'test', 'weight': 3}
    ]
    actual = make_word_cloud({'me': 1, 'ทดสอบ': 2, '12354': 1, 'test': 3, '12': 1, '9': 2}, sort='ascend', limit=2)
    assert actual == [
        {'name': 'me', 'weight': 1},
        {'name': '12354', 'weight': 1}
    ]

def test_be_able_to_make_hashtag_count():
    actual = make_hashtag_count(
        ['#test', 'test', 'me', 'ทดสอบ', '#12354', '12', '9',
        '9', '#ทดสอบ', 'test', '#ทดสอบ', '#ทดสอบ', 'Big data', 'hashtag',
        '#ทดสอบ','#ทดสอบ','#ทดสอบ','#ทดสอบ','#test', 'Be_e']
    )
    assert actual == {'#test': 2, '#ทดสอบ': 7, '#12354': 1}

def test_be_able_to_filter_sign_hash_out():
    actual = make_hashtag_count(
        ['#test', '#', 'test', 'me', 'ทดสอบ', '#12354', '12', '9',
        '9', '#ทดสอบ', 'test', '#ทดสอบ', '#ทดสอบ', 'Big data', 'hashtag',
        '#ทดสอบ','#ทดสอบ','#ทดสอบ','#ทดสอบ','#test', '#', 'Be_e']
    )
    assert actual == {'#test': 2, '#ทดสอบ': 7, '#12354': 1}
