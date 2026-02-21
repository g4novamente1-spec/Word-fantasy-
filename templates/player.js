export class Player {
    constructor() {
        this.x = 1500;
        this.y = 1500;
        this.size = 20;
        this.speed = 5;
    }

    update(keys) {
        if (keys["w"]) this.y -= this.speed;
        if (keys["s"]) this.y += this.speed;
        if (keys["a"]) this.x -= this.speed;
        if (keys["d"]) this.x += this.speed;
    }

    draw(ctx, camera) {
        ctx.fillStyle = "red";
        ctx.beginPath();
        ctx.arc(
            this.x - camera.x,
            this.y - camera.y,
            this.size,
            0,
            Math.PI * 2
        );
        ctx.fill();
    }
}
