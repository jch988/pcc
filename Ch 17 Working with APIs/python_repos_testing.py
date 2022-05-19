import requests

import unittest

# Make and API call and store the repsonses
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine each repository
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print(f"\nName: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repositry: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")



class NamesTestCase(unittest.TestCase):
	"""Tests for python_repos.py"""

	def test_status_code(self):
		"""Is the status code 200?"""
		self.assertEqual(r.status_code, 200)

	def test_total_repositories(self):
		"""Are there any repositories returned?"""
		self.assertTrue(response_dict)

	def test_repositories_returned(self):
		"""Are there 30 repositories returned?"""
		self.assertEqual(len(repo_dicts), 31)

if __name__ == '__main__':
	unittest.main()
