from fastapi import FastAPI
import uvicorn
from ml import ml_app
app = FastAPI()

@app.get("/{que}")
async def root(que):
    ans = ml_app(que)
    return {"answer":ans}
#
# @app.get("/app")
# async def app():
#     ans = ml_app("parents of Bruce Wayne ?")
#     return ans


if __name__ =="__main__":
    uvicorn.run("main:app",reload=True)
