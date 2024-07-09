import os
from fastapi import FastAPI, HTTPException
import aiofiles
import json

app = FastAPI()


@app.get("/api/links")
async def links():
    async with aiofiles.open(
        os.path.dirname(os.path.abspath(__file__)) + "/.tempdata/monster-url.json", "r"
    ) as f:
        data = await f.read()
    links = json.loads(data)
    return links


@app.get("/api/monsters")
async def monsters():
    async with aiofiles.open(
        os.path.dirname(os.path.abspath(__file__)) + "/.tempdata/monsters-details.json",
        "r",
    ) as f:
        data = await f.read()
    monsters = json.loads(data)
    return monsters


@app.get("/api/monster/{item_id}")
async def get_monster(item_id):
    async with aiofiles.open(
        os.path.dirname(os.path.abspath(__file__)) + "/.tempdata/monsters-details.json",
        "r",
    ) as f:
        data = await f.read()
    monsters = json.loads(data)
    try:
        monster = monsters[int(item_id)]
        return monster
    except IndexError:
        raise HTTPException(status_code=404, detail=f"No monster with id {item_id}")
