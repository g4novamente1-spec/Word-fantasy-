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
    player_atk = data["player_atk"]
    player_luck = data["player_luck"]

    enemy_hp = data["enemy_hp"]
    enemy_atk = 6
    enemy_def = 3

    # ---- ATAQUE DO JOGADOR ----
    crit = random.randint(1, 100) <= player_luck * 5
    base_damage = random.randint(1, player_atk)
    damage = base_damage * 2 if crit else base_damage
    damage = max(0, damage - enemy_def)
    enemy_hp -= damage

    enemy_damage = 0

    # ---- SE INIMIGO SOBREVIVE, ELE ATACA ----
    if enemy_hp > 0:
        enemy_damage = random.randint(1, enemy_atk)
        player_hp -= enemy_damage

    return JSONResponse({
        "damage": damage,
        "enemy_hp": enemy_hp,
        "critical": crit,
        "enemy_damage": enemy_damage,
        "player_hp": player_hp
    }){
        "damage": damage,
        "enemy_hp": enemy_hp,
        "critical": crit
    })
