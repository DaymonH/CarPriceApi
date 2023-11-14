from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define an endpoint with a path parameter
@app.get("/")
def read_root():
    return {"Hello": "World"}
