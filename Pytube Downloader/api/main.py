from fastapi import FastAPI, HTTPException, Query
from pytube import YouTube

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is working"}

@app.post("/download")
async def yt_download(url: str = Query(...)):
    try:
         y_tube = YouTube(url)
         stream = y_tube.streams.filter(progressive=True).order_by('resolution').desc().first()
         download_url = stream.url
         return {"download_url": download_url}
    except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))  