from github import Github
from const import ACCESS_TOKEN,REPO_OWNER,REPO_NAME

# Replace with your GitHub Personal Access Token
GITHUB_TOKEN = ACCESS_TOKEN

# Create a GitHub instance using your token
g = Github(GITHUB_TOKEN)

# Replace with the repository information
OWNER = REPO_OWNER
REPO = REPO_NAME

# Get the repository
repo = g.get_repo(f'{OWNER}/{REPO}')

# Get all commits
commits = repo.get_commits()

# Iterate through commits and get commit information
for commit in commits:
    commit_sha = commit.sha
    commit_message = commit.commit.message
    print(f"Commit: {commit_sha}\nMessage: {commit_message}\n")
