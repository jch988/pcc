from operator import itemgetter

import requests

from plotly.graph_objs import Bar
from plotly import offline 

# Make an API call and store the reponse
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()		
submission_dicts = []
for submission_id in submission_ids[:30]:
	
	# Make a separate API call for each submission
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()								

	# Build a dictionary for each article
	submission_dict = {
		'title': response_dict['title'],
		'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
		'comments': response_dict.get('descendants', 0)
	}
	submission_dicts.append(submission_dict)			

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
	 reverse=True)

for submission_dict in submission_dicts:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Comments: {submission_dict['comments']}")


discussions, comments, links = [], [], []
for item in submission_dicts:

	discussion = item['title']
	num_comments = item['comments']

	link_url = item['hn_link']
	link = f"<a href='{link_url}'>{discussion}</a>"

	discussions.append(discussion)
	comments.append(num_comments)
	links.append(link)


# Visualize

data = [{
	'type': 'bar',
	'x': links,
	'y': comments,
	'marker': {
		'color': 'rgb(60,100,150)',
		'line': {'width': 1.5, 'color': 'rgb(25,25,25)'},
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'Top Discussion on Hacker News',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Discussion',
		'titlefont': {'size': 22},
		'tickfont': {'size': 14},
		},
	'yaxis': {
		'title': 'Number of Comments',
		'titlefont': {'size': 22},
		'tickfont': {'size': 14},
		},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_discussions.html')
