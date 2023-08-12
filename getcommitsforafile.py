from github import Github
from datetime import datetime

from const import ACCESS_TOKEN,REPO_OWNER,REPO_NAME

# GitHub repository information
owner = REPO_OWNER
repo_name = REPO_NAME

# Personal access token (replace with your token)
access_token = ACCESS_TOKEN

# Date and time ranges
start_datetime = datetime(2023, 7, 10, 0, 0, 0)  # Start datetime (UTC)
end_datetime = datetime(2023, 7, 20, 23, 59, 59)  # End datetime (UTC)

# File path within the repository
file_path = 'readme.md'

# Initialize PyGithub with access token
g = Github(access_token)

# Get the repository
repo = g.get_repo(f'{owner}/{repo_name}')

# Get the file object
file = repo.get_contents(file_path)

# Iterate through commits for the specific file within the datetime range
for commit in repo.get_commits(since=start_datetime, until=end_datetime, path=file_path):
    commit_sha = commit.sha
    commit_date = commit.commit.committer.date
    commit_author = commit.commit.author.name
    commit_message = commit.commit.message

    # Print commit details
    print(f"Commit SHA: {commit_sha}")
    print(f"Author: {commit_author}")
    print(f"Date: {commit_date}")
    print(f"Message: {commit_message}")

    print("\n")
