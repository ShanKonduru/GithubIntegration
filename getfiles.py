from github import Github
from const import ACCESS_TOKEN,REPO_OWNER,REPO_NAME

# Replace with the two commit SHAs you want to compare
COMMIT_SHA_1 = "24c1047766e87177ecdfd576265c1b909fd934cc"
COMMIT_SHA_2 = "e4e2f192a92a5e9df80c34a8caa587dce81ecb34"

# Initialize the GitHub API using your access token
g = Github(ACCESS_TOKEN)

# Get the repository
repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

# Get the comparison between two commits
comparison = repo.compare(COMMIT_SHA_1, COMMIT_SHA_2)

# Print the list of changed files
for file in comparison.files:
    print(file.filename)
