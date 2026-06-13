from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {
  "Books": [
    {
      "name": "Prilli i thyer",
      "author": "Ismail Kadare",
      "details": {
        "genre": "roman",
        "year": "2020"
      }
    },
    {
      "name": "Pallati i endrrave",
      "author": "Ismail kadare",
      "details": {
        "genre": "roman",
        "year": "2020"
      }
    },
    {
      "name": "Pallati i endrrave",
      "author": "Ismail kadare",
      "details": {
        "genre": "roman",
        "year": "2020"
      }
    }
  ]
}