#JSON DATA
#{
#  "name": "Arianita",
#   "age": "23",
#   "adress": {
#     "Country": "Kosovo",
#     "City": "Prishtine",
#     "ZIP Code": "10000",
#     "Street": "Rruga B"
#   },
#   "Contacts": [
#     {
#       "type": "email",
#       "value": "arianita@gmail.com"
#     },
#     {
#       "type": "phone",
#       "value": "+383111111"
#     },
#     {
#       "type": "Linkedin",
#       "value": "Arianita"
#     }
#   ]
#
#  }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Hello World"}

