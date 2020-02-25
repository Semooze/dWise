import os
from dataclasses import dataclass

@dataclass
class ProdEnv:
    data_file: str = os.environ['PROD_DATA_FILE']
    word_file: str = os.environ['PROD_WORD_FILE']
    hashtag_file: str = os.environ['PROD_HASHTAG_FILE']

@dataclass
class DevEnv:
    data_file: str = os.environ['DEV_DATA_FILE']
    word_file: str = os.environ['DEV_WORD_FILE']
    hashtag_file: str = os.environ['DEV_HASHTAG_FILE']

@dataclass
class TestEnv:
    data_file: str = os.environ['TEST_DATA_FILE']
    word_file: str = os.environ['TEST_WORD_FILE']
    hashtag_file: str = os.environ['TEST_HASHTAG_FILE']

mode = os.environ['MODE']