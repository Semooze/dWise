import os
prod_file = os.environ['PROD_FILE']
dev_file = os.environ['DEV_FILE']
test_file = os.environ['TEST_FILE']
# Mode can only be "test", "development" or"production"
mode = os.environ['MODE']