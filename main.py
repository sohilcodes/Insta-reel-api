from fastapi import FastAPI
import instaloader

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Instagram API Working!"}

@app.get("/api")
def reel(url: str):
    try:
        loader = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        return {"status": "ok", "video": post.video_url}
    except:
        return {"status": "error", "msg": "Invalid URL"}
