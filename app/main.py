from fastapi import FastAPI,HTTPException
import redis
from app.datatype.data_type import IDstore
import json
import sys
#note: host has to be the same as the service name in the docker-compose file
r = redis.Redis(host="redis", port=6379)
app = FastAPI()

import debugpy

debugpy.listen(("localhost", 5678))
#print("Waiting for client to attach...")
#debugpy.wait_for_client()

IDs: dict[str, IDstore] = {}

with open("app/data/sampledata.json", encoding="utf8") as file:
    raw_data = json.load(file)
    for ids in raw_data:
        ID = IDstore(**ids)
        IDs[ID.id] = ID


@app.get("/")
def read_root():
    return {"Hello": "World FastAPI"}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}

@app.get("/getid/{id}", response_model=IDstore)
def read_item(id: str) -> IDstore:
    print("sdfdffsdfsdf" ,IDs," ",IDs['one'])
    #sys.exit()

    if id not in IDs:
        raise HTTPException(status_code=404, detail="ID not found")
    return IDs[id]


@app.get("/health")
def health():
    return {"status": "ok"}