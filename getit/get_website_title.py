import requests


def get_title_from_website(website):
    request = requests.get(website)
    response_text = request.text
    title_start = response_text.index('<title>') + len('<title>')
    title_end = response_text.rindex('</title>')
    title = response_text[title_start:title_end]
    return request.status_code, title
