import sys
import requests

def get_pr_details(owner, repo, pr_number):
    base_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    response = requests.get(base_url)
    if response.status_code == 200:
        pr_details = response.json()
        return pr_details
    else:
        print("Error: Unable to fetch PR details. Status code:", response.status_code)
        return None

def notify_on_slack():
    pr_number = sys.argv[1]
    owner = "jasveerhashtrust"
    repo = "MdxAutomation"
    pr_details = get_pr_details(owner, repo, pr_number)
    print(pr_details)
    return pr_details

if __name__ == '__main__':
    response = notify_on_slack()
    print(response)
