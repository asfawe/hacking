import pprint

data = {
    "name": "뤼튼",
    "age": 3,
    "skills": ["content generation", "conversation"],
    "info": {"company": "뤼튼테크놀로지스", "year": 2023}
}

formatted_data = pprint.pformat(data)
print(formatted_data)