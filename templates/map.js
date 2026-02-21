export class GameMap {
    constructor() {
        this.image = new Image();
        this.image.src = "./assets/cidade.png";
    }

    draw(ctx, camera) {
        ctx.drawImage(
            this.image,
            camera.x,
            camera.y,
            camera.width,
            camera.height,
            0,
            0,
            camera.width,
            camera.height
        );
    }
}
