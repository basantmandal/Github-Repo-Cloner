"""
Download Public Repositories from Github
pip install requests
You can also use the requirements.txt for Package Installation
"""
  
import requests
import subprocess

def clone_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx or 5xx)
        repos = response.json()
        
        if not repos:
            print("No repositories found for this user.")
            return
        
        for i, repo in enumerate(repos, 1):  # Start the index from 1
            repo_name = repo['name']
            repo_url = repo['svn_url']
            print(f"\nRepository Sr.No: {i}")
            print(f"Repository Name: {repo_name}")
            print(f"Cloning Repository - {repo_url}\n")
            
            try:
                # Using subprocess for better handling of external commands
                subprocess.check_call(['git', 'clone', f'{repo_url}.git'])
                print("Cloning Completed\n")
            except subprocess.CalledProcessError as e:
                print(f"Error cloning repository {repo_name}: {e}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

if __name__ == "__main__":
    username = input("Enter GitHub Username: ")
    clone_repositories(username)
