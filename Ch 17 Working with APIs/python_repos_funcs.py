import requests

def get_api():
	"""Make and API call and store the repsonses"""
	url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
	headers = {'Accept': 'application/vnd.github.v3+json'}
	r = requests.get(url, headers=headers)
	print(f"Status code: {r.status_code}")

def store_api():
	"""Store API response in a variable"""
	get_api()
	response_dict = r.json()
	print(f"Total repositories: {response_dict['total_count']}")

def explore_repositories():
	"""Explore information about the repositories"""
	repo_dicts = response_dict['items']
	print(f"Repositories returned: {len(repo_dicts)}")

def examine_repository():
	"""Examine each repository"""
	print("\nSelected information about each repository:")
	for repo_dict in repo_dicts:
		print(f"\nName: {repo_dict['name']}")
		print(f"Owner: {repo_dict['owner']['login']}")
		print(f"Stars: {repo_dict['stargazers_count']}")
		print(f"Repositry: {repo_dict['html_url']}")
		print(f"Created: {repo_dict['created_at']}")
		print(f"Updated: {repo_dict['updated_at']}")
		print(f"Description: {repo_dict['description']}")


