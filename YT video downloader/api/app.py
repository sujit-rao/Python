from fastapi import FastAPI, HTTPException, Query
from yt_dlp import YoutubeDL
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ["*"]
)

@app.get("/")
async def read_root():
    return{"message": "Server is working"}

@app.post("/api/download")
async def get_download_link(url: str = Query(...)):
    ydl_opts = {'format': "bestvideo+bestaudio/best",
                'merge_output_format' : 'mp4',
                'noplaylist': 'True'}
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [info_dict])
            video_url = formats[-1]['url']
            print(video_url)
            if video_url:
                return {"download_url" : video_url}
            else:
                raise HTTPException(status_code = 404, detail = "Download link not found")
        except Exception as e:
            raise HTTPException(status_code = 500, detail = str(e))