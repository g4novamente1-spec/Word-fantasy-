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


@app.post("/combat")
def combat(data: dict):

    player = data["player"]
    enemy = data["enemy"]
    action = data["action"]

    log = []

    # ======================
    # AÇÃO DO JOGADOR
    # ======================

    if action == "attack":

        crit_chance = player["luck"] * 5
        crit = random.randint(1, 100) <= crit_chance

        base_damage = random.randint(player["min_atk"], player["max_atk"])
        damage = base_damage * 2 if crit else base_damage
        damage = max(0, damage - enemy["def"])

        enemy["hp"] -= damage

        msg = f"Você causou {damage} de dano."
        if crit:
            msg += " 💥 CRÍTICO!"
        log.append(msg)

    elif action == "potion":

        if player["potions"] > 0:
            heal = random.randint(15, 25)
            player["hp"] += heal
            player["potions"] -= 1
            log.append(f"Você usou poção e recuperou {heal} HP.")
        else:
            log.append("Você não tem poções!")

    # ======================
    # TURNO DO INIMIGO
    # ======================

    if enemy["hp"] > 0:


        enemy_damage = random.randint(enemy["min_atk"], enemy["max_atk"])
        enemy_damage = max(0, enemy_damage - player["def"])

        player["hp"] -= enemy_damage
        log.append(f"O inimigo causou {enemy_damage} de dano.")

    # ======================
    # VERIFICAÇÕES FINAIS
    # ======================

    if player["hp"] <= 0:
        log.append("☠️ Você morreu!")

    if enemy["hp"] <= 0:
        log.append("🏆 Você venceu o combate!")

    return JSONResponse({
        "player": player,
        "enemy": enemy,
        "log": log
    })

from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
