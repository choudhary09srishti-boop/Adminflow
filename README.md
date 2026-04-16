# AdminFlow - AI IT Agent

An AI agent that reads IT requests, opens a browser, and performs tasks like a human.

## Tech Stack
- Python
- Flask
- Playwright
- Groq LLM (llama-3.3-70b-versatile)

## Features
- AI understands IT requests
- Browser automation with Playwright
- Mock Admin Panel (Create User, Reset Password, User List)
- Conditional Logic (check user → create → assign license → assign role)

## Live URL
https://web-production-7d52e.up.railway.app

## Endpoints
- POST /run-task → AI performs browser task
- POST /check-user → Multi-step conditional logic

## Setup
1. Clone repo
2. Create virtual env
3. pip install -r requirements.txt
4. Add GROQ_API_KEY in .env
5. python main.py
