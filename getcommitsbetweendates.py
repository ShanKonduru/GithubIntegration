from github import Github
from datetime import datetime
from const import ACCESS_TOKEN,REPO_OWNER,REPO_NAME

# GitHub repository information
owner = REPO_OWNER
repo_name = REPO_NAME

# Personal access token (replace with your token)
access_token = ACCESS_TOKEN

# Date and time ranges
start_date = datetime(2023, 7, 18, 0, 0, 0)  # Start date: yyyy, MM, dd, hh, mm, ss
end_date = datetime(2023, 7, 20, 23, 59, 59 )   # End date: yyyy, MM, dd, hh, mm, ss

# Initialize PyGithub with access token
g = Github(access_token)

# Get the repository
repo = g.get_repo(f'{owner}/{repo_name}')

# Iterate through commits within the date range
for commit in repo.get_commits(since=start_date, until=end_date):
    commit_sha = commit.sha
    commit_date = commit.commit.committer.date
    commit_author = commit.commit.author.name
    commit_message = commit.commit.message

    # Get details of files changed in the commit
    files_changed = commit.files

    # Print commit details and changed files
    print(f"Commit SHA: {commit_sha}")
    print(f"Author: {commit_author}")
    print(f"Date: {commit_date}")
    print(f"Message: {commit_message}")
    print("Files changed:")
    for file in files_changed:
        print(f"  {file.filename}")
    print("\n")