# filepath: /path/to/your/script.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the GitHub token from the environment variable
github_token = os.getenv('GITHUB_TOKEN')

# Use the token for GitHub authentication
# Example: setting the remote URL with the token
os.system(f'git remote set-url origin https://{github_token}@github.com/chiragmudgal15/chirag-analytics.github.io.git')