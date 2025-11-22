from fastapi import FastAPI
import instaloader

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running..."}

@app.get("/api")
def reel(url: str):
    try:
        loader = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        return {
            "status": "ok",
            "video": post.video_url
        }

    except Exception as e:
        return {"status": "error", "msg": str(e)}
