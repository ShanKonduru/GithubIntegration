from github import Github

# Authentication is defined via github.Auth
from github import Auth

from const import ACCESS_TOKEN


# using an access token
auth = Auth.Token(ACCESS_TOKEN)

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://api.github.com", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)