from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/attack")
def attack(data: dict):
    player_hp = data["player_hp"]
    enemy_hp = data["enemy_hp"]

    # jogador sempre causa 1 de dano
    enemy_hp -= 1

    # goblin sempre causa 20 de dano
    player_hp -= 20

    return {
        "damage": 1,
        "enemy_hp": enemy_hp,
        "critical": False,
        "enemy_damage": 20,
        "player_hp": player_hp
    }
