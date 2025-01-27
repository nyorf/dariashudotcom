from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse, RedirectResponse
import io


app = FastAPI()


@app.get(path="/")
async def getWallpaper():
    return RedirectResponse(url="https://dariashu.notion.site/f5f32e2f1f494086811bf2dad750cdba", permanent=False)


@app.route("/{full_path:path}")
async def catch_all(full_path: str):  # catch-all route, temporary as there's no content
    return RedirectResponse(url="https://dariashu.notion.site/f5f32e2f1f494086811bf2dad750cdba", permanent=False)


@app.get(path="/robots.txt")
@app.get(path="/robots")
async def robots():
    robots_file = io.FileIO('data/robots.txt', mode='r')
    return StreamingResponse(content=robots_file, media_type="text/plain")
