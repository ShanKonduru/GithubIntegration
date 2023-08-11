from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("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")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)