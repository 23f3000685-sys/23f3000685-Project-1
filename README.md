# Auto App Task Runner

## Summary
This project hosts an API endpoint that receives a JSON payload and automatically generates, commits, and deploys a minimal app to GitHub Pages.

## Setup
1.   Clone repo
2.   Run `npm install`
3.   Create `.env` with: 
   a.       RM_SECRET=your_google_form_secret
   b.       GH_TOKEN=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
4.   Run with `node server.js`

## Usage
```bash
curl https://your-server/api-endpoint \
-H "Content-Type: application/json" \
-d '{"brief": "sample app", "task": "captcha-solver", "round": 1, "nonce": "abc123", "secret": "your_google_form_secret"}'
