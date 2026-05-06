import requests
username=input("Enter Github username:")
url=f"https://api.github.com/users/{username}"
response= requests.get(url)
data=response.json()
if response.status_code == 200:
    print("Name",data["name"])
    print("Public Repos:",data["public_repos"])
    print("Followers", data["followers"])
else:
    print("User not found")