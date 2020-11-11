import requests


#https://developer.nytimes.com/
api_key  = "YOUR API KEY"

def pull_news(query_string):
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query_string}&api-key={api_key}"
    r = requests.get(url).json()["response"]["docs"]
    if len(r) > 0:
        return r
    return "No news found"

def get_news(query_string):
    news = pull_news(query_string)
    news = [(n["abstract"], n["lead_paragraph"], n["pub_date"]) for n in news]
    return news
