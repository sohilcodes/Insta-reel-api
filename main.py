from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API running successfully"}

@app.get("/api")
def download_reel(url: str):

    try:
        # Clean URL
        if "?igsh" in url:
            url = url.split("?")[0]

        shortcode = url.split("/")[-2]

        api_url = f"https://www.instagram.com/reel/{shortcode}/?__a=1&__d=dis"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
        }

        r = requests.get(api_url, headers=headers).json()

        # new working video path
        video_url = r["items"][0]["video_versions"][0]["url"]

        return {
            "status": "ok",
            "video": video_url
        }

    except Exception as e:
        return {"status": "error", "msg": str(e)}
