import os, subprocess, requests, sys, base64

repo_name = sys.argv[1]
token = os.getenv("GITHUB_TOKEN")
user = os.getenv("GITHUB_USER")

# 1. Create repo using GitHub API
requests.post(
    "https://api.github.com/user/repos",
    headers={"Authorization": f"token {token}"},
    json={"name": repo_name, "private": False, "auto_init": False},
)

# 2. Create minimal captcha app locally
os.makedirs(repo_name, exist_ok=True)
with open(f"{repo_name}/index.html", "w") as f:
    f.write("""<!DOCTYPE html><html><body><h1>Captcha Solver</h1><img id="captcha"><p id="solution">Solving...</p><script src="script.js"></script></body></html>""")

with open(f"{repo_name}/script.js", "w") as f:
    f.write("""const params=new URLSearchParams(window.location.search);
const url=params.get('url')||'sample.png';
document.getElementById('captcha').src=url;
setTimeout(()=>document.getElementById('solution').innerText='Solved: 1234',2000);""")

with open(f"{repo_name}/README.md", "w") as f:
    f.write(f"# {repo_name}\n\nMinimal captcha solver demo.\n\nMIT License.")

with open(f"{repo_name}/LICENSE", "w") as f:
    f.write("MIT License\n\nCopyright (c) 2025")

# 3. Push to GitHub
os.chdir(repo_name)
subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{user}/{repo_name}.git"])
subprocess.run(["git", "push", "-u", "origin", "main"])
