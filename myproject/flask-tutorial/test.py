from random import choices
from string import digits

class ModelConstants:
    api_token_length: int = 6
    username_max_length: int = 30
    password_max_length: int = 100
    post_title_max_length: int = 40
    post_content_max_length: int = 300
    report_reason_max_length: int = 100

token = ''.join(choices(digits, k=ModelConstants.api_token_length))

print(token)