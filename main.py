from fastapi import FastAPI, Request
import json, subprocess, os, base64, requests, tempfile

app = FastAPI()

SECRET = os.getenv("STUDENT_SECRET")

@app.post("/api-endpoint")
async def receive_json(req: Request):
    data = await req.json()
    if data.get("secret") != SECRET:
        return {"error": "Invalid secret"}

    # Save attachment (if any)
    attachments = data.get("attachments", [])
    for att in attachments:
        if att["url"].startswith("data:image/png;base64,"):
            image_data = base64.b64decode(att["url"].split(",")[1])
            with open(att["name"], "wb") as f:
                f.write(image_data)

    # Create GitHub repo
    repo_name = data["task"]
    subprocess.run(["python", "generate_repo.py", repo_name])

    # After pushing repo, send evaluation callback
    payload = {
        "email": data["email"],
        "task": data["task"],
        "round": data["round"],
        "nonce": data["nonce"],
        "repo_url": f"https://github.com/{os.getenv('GITHUB_USER')}/{repo_name}",
        "commit_sha": os.getenv("LAST_COMMIT", "unknown"),
        "pages_url": f"https://{os.getenv('GITHUB_USER')}.github.io/{repo_name}/"
    }

    requests.post(data["evaluation_url"], json=payload, headers={"Content-Type": "application/json"})

    return {"status": "success", "repo": payload["repo_url"]}
