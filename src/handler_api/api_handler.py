import json
import gzip
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message, ASGIApp
from pydantic import BaseModel

from src.database.vector_database import VectorRetriever
from typing import List, Dict 

import asyncio ## use this 

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}


persist_directory = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\vector_db_4"
collection_name= "recipe_collection"

#INITIALIZE the VECTOR RETRIEVER and make it ready as a global variable
vector_retriever = VectorRetriever(model_name = model_name, model_kwargs= model_kwargs, encode_kwargs=encode_kwargs, overwrite=False)
vector_retriever.initialize_vector_store(persist_directory=persist_directory, documents=None, collection_name=collection_name)
print("vector retriever initialized successfully!")

# Dependency function
def get_vector_retriever():
    return vector_retriever


app = FastAPI()


params= {

    "ingredients_list":[
        "cup butter",
        " plain yogurt",
        "sugar",
        "1  egg",
        "vanilla "
    ],
    "recipe_tags": ["Dessert", "Healthy"],# this key will contain the preferences of the user

}

def find_recipe(ingredients_list:List,k:int = 3, filter:Dict[str, str]=None, where:Dict[str, str]=None, where_document:Dict=None)-> List[Dict]:
    """
    this should handle metadata filtering and similarity search
    then returns the most relevant documents
    """
    vector_retriever = get_vector_retriever()
    results = vector_retriever.similarity_search(query=ingredients_list, k=4, filter = filter , where = where, where_document = where_document)
    return results



@app.get("/home")
async def test_endpoint():

    return {"message":"ok"}





class RecipeRequest(BaseModel):
    ingredients_list: List[str]
    recipe_tags: List[str]

@app.post("/get-recipe")
async def get_recipe(request_body: RecipeRequest):

    try:
        ingredients_list = request_body.ingredients_list
        recipe_tags = request_body.recipe_tags
        where_document = {
            "$and": [{"$contains": tag} for tag in recipe_tags]
        }

        results = find_recipe(ingredients_list=ingredients_list, filter=None, where=None, where_document=where_document)
        print(results)
        response_message = f"You have asked for a {'| '.join(recipe_tags)} meal, and you have the following items: {'| '.join(ingredients_list)}"
        final_response = f"{response_message} \n Here are the results: \n {results}"
        return JSONResponse({"response":final_response})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    
    uvicorn.run("api_handler:app", host="0.0.0.0", port=8000, reload=True)