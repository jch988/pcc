import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make histogram showing the number of repositories for each language:
languages = ['python', 'javascript', 'c', 'ruby', 'perl', 'java', 'haskell', 
'go', 'c#', 'c++']

language_dicts = []

# Get information about each language on the list
for language in languages:

	# Make a separate API call for each language
	url = f'https://api.github.com/search/repositories?q=language:{language}'
	f'&sort=stars'
	headers = {'Accept': 'application/vnd.github.v3+json'}
	r = requests.get(url, headers=headers)
	print(f"id: {language}\tstatus: {r.status_code}")
	response_dict = r.json()
	print(f"Total repositories for {language}: {response_dict['total_count']}")

	# Create a dictionary for each language
	language_dict = {
		'name': language,
		'repositories': response_dict['total_count'],
	}

	# Add each language's dictionary to the list
	language_dicts.append(language_dict)


# Process results
langs, repos = [], []
for item in language_dicts:
	lang = item['name']
	repo = item['repositories']
	langs.append(lang)
	repos.append(repo)

# Make visualization
data = [{
	'type': 'bar',
	'x': langs,
	'y': repos,
	'marker': {
		'color': 'rgb(60,100,150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'Comparison of number of repositories on GitHub',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Language',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
		},
	'yaxis': {
		'title': 'Number of repositories',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
		},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='language_repos.html')