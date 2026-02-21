import { CONFIG } from "./config.js";
import { GameMap } from "./map.js";
import { Player } from "./player.js";

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

canvas.width = CONFIG.canvasWidth;
canvas.height = CONFIG.canvasHeight;

const map = new GameMap();
const player = new Player();

let keys = {};

window.addEventListener("keydown", e => keys[e.key.toLowerCase()] = true);
window.addEventListener("keyup", e => keys[e.key.toLowerCase()] = false);

let camera = {
    x: 0,
    y: 0,
    width: canvas.width,
    height: canvas.height
};

function update() {
    player.update(keys);

    // Câmera segue o jogador
    camera.x = player.x - camera.width / 2;
    camera.y = player.y - camera.height / 2;

    // Limite do mapa
    camera.x = Math.max(0, Math.min(camera.x, CONFIG.mapWidth - camera.width));
    camera.y = Math.max(0, Math.min(camera.y, CONFIG.mapHeight - camera.height));
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    map.draw(ctx, camera);
    player.draw(ctx, camera);
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

map.image.onload = () => {
    gameLoop();
};
