import json
import gzip
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message, ASGIApp


class GZipedMiddleware(BaseHTTPMiddleware):
    async def set_body(self, request: Request):
        receive_ = await request._receive()
        if "gzip" in request.headers.getlist("Content-Encoding"):
            #print(receive_)                          
            data = gzip.decompress(receive_.get('body'))
            receive_['body'] = data
        else:
            print("header not detected") 
            data = receive_.get('body') 
            receive_['body'] = data
             
 

        async def receive() -> Message:
            return receive_

        request._receive = receive                

    async def dispatch(self, request, call_next):
        await self.set_body(request)
        response = await call_next(request)
        return response             

app = FastAPI()
app.add_middleware(GZipedMiddleware)

params= {
    "metadata":{
        "cusine":"italian",
        "health_n_wellness":"low-carb",
        "level":"beginner-friendly"
    },
    "items":["tomato","potato","milk"] # can be empty
}

def find_recipe(params):
    """
    this should handle metadata filtering and similarity search
    then returns the most relevant recipe for chatgpt to use
    """
    pass 




@app.get("/home")
async def test_endpoint():

    return {"message":"ok"}



@app.route("/get-recipe",methods=["POST"])
async def get_recipe(request:Request):
    try:
        compressed_data = await request.body()
        params_str = compressed_data.decode("utf-8")
        params = json.loads(params_str)

        cusine = params['metadata']["cusine"]

        level = params['metadata']['level']
        health = params['metadata']['health_n_wellness']
        items = params['items']

        response_message = f"You have asked for a {level}, {health}, {cusine} meal, and you have the following items: {items}"
        return JSONResponse({"response":response_message})

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error occurred during processing the request")

"""
@app.post("/get-recipe")
async def get_recipe(params:dict)->dict:

    cusine = params['metadata']['cusine']
    level = params['metadata']['level']
    health = params['metadata']['health_n_wellness']
    items = params['items']
    response = f"you have asked a {level}, {health}, {cusine} meal,and you have the following items: {items}"

    return {"response":response} """

if __name__ == "__main__":

    uvicorn.run("api_handler:app", host="0.0.0.0", port=8000, reload=True)