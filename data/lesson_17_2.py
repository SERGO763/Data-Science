from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline

import requests

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
repo_links, comment = [], []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Построение словаря для каждой статьи.
    submission_dict = response_dict['time']

    #submission_dict.append(submission_dict)
    comment.append(response_dict['descendants'])
    repo_sub = response_dict['title']
   # print(repo_sub)
    repo_url = response_dict['url']
    repo_link = f"<a href='{repo_url}'>{repo_sub}</a>"
    repo_links.append(repo_link)


data = [{
    'type': 'bar',
    'x': repo_links,
    'y': comment,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Articles on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Сomment',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')