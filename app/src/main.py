from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from mangum import Mangum
from app.src.modules.recipes import Recepies


app = FastAPI()

# Define API key security
API_KEY = "supersecretapikey123"  # Change this!
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/")
def read_root(api_key: str = Depends(validate_api_key)):
    return {"message": "Hello, Authenticated User!"}

#@app.get("/recipe")
# def get_resepi(api_key: str = Depends(validate_api_key)):
#    recipes_instance = Recepies()
#    return recipes_instance.getRandom()

@app.get("/recipe")
def get_recipe():
    recipes_instance = Recepies()
    return recipes_instance.getRandom()

handler = Mangum(app)