const board_border = '#002EFE';
const board_background = "#2A304B";
const snake_col = 'lightblue';
const snake_border = 'darkblue';
    
let snake = [
    {x: 200, y: 200},
    {x: 190, y: 200},
    {x: 180, y: 200},
    {x: 170, y: 200},
    {x: 160, y: 200}
]

let score = 0;
let food_x;
let food_y;
let changing_direction = false;
let dx = 10;
let dy = 0;
const snakeboard = document.getElementById("snakeboard");
const snakeboard_ctx = snakeboard.getContext("2d");

document.addEventListener("keydown", change_direction)

main();
gen_food();
    
function main() {
    if (has_game_ended()) {
        document.getElementById("gameOver").style.color = "red";
        document.getElementById("gameOver").innerHTML = "You Lose! Press R to play again.";
        return;
    }

    changing_direction = false;
    setTimeout(function onTick() {
        clearCanvas();
        move_snake();
        drawSnake();
        drawFood();
        main();
    }, 100)
}
    
function clearCanvas() {
    snakeboard_ctx.fillStyle = board_background;
    snakeboard_ctx.strokestyle = board_border;
    snakeboard_ctx.fillRect(0, 0, snakeboard.width, snakeboard.height);
    snakeboard_ctx.strokeRect(0, 0, snakeboard.width, snakeboard.height);
}
    
function drawSnake() {
    snake.forEach(drawSnakePart)
}
    
function drawSnakePart(snakePart) {
    snakeboard_ctx.fillStyle = snake_col;
    snakeboard_ctx.strokestyle = snake_border;
    snakeboard_ctx.fillRect(snakePart.x, snakePart.y, 10, 10);
    snakeboard_ctx.strokeRect(snakePart.x, snakePart.y, 10, 10);
}

function move_snake() {
    const head = {x: snake[0].x + dx, y: snake[0].y + dy};
    snake.unshift(head);
    const has_eaten_food = snake[0].x === food_x && snake[0].y === food_y;
    if (has_eaten_food) {
        score += 1;
        document.getElementById('score').innerHTML = score;
        gen_food();
    } else {
        snake.pop();
    }
}

function change_direction(event) {
    const A_KEY = 65;
    const D_KEY = 68;
    const W_KEY = 87;
    const S_KEY = 83;
    const R_KEY = 82;
    const UP_KEY = 38;
    const DOWN_KEY = 40;
    const RIGHT_KEY = 39;
    const LEFT_KEY = 37;
 
    const keyPressed = event.keyCode;
    const goingUp = dy === -10;
    const goingDown = dy === 10;
    const goingRight = dx === 10;
    const goingLeft = dx === -10;

    if (keyPressed === A_KEY && !goingRight) {
        dx = -10;
        dy = 0;
    }
    if (keyPressed === D_KEY && !goingLeft) {
        dx = 10;
        dy = 0;
    }
    if (keyPressed === W_KEY && !goingDown) {
        dx = 0;
        dy = -10;
    }
    if (keyPressed === S_KEY && !goingUp) {
        dx = 0;
        dy = 10;
    }
    if (keyPressed === UP_KEY && !goingDown) {
        dx = 0;
        dy = -10;
    }
    if (keyPressed === DOWN_KEY && !goingUp) {
        dx = 0;
        dy = 10;
    }
    if (keyPressed === RIGHT_KEY && !goingLeft) {
        dx = 10;
        dy = 0;
    }
    if (keyPressed === LEFT_KEY && !goingRight) {
        dx = -10;
        dy = 0;
    }
    if (keyPressed === R_KEY) {
        location.reload()
    }
}

function has_game_ended() {
    for (let i = 4; i < snake.length; i++) {
        const has_collded = snake[i].x === snake[0].x && snake[i].y === snake[0].y
        if (has_collded) {
            return true
        }
    }
    const hitLeftWall = snake[0].x < 0;
    const hitRightWall = snake[0].x > snakeboard.width - 10;
    const hitTopWall = snake[0].y < 0;
    const hitBottomWall = snake[0].y > snakeboard.height - 10;

    return hitLeftWall || hitRightWall || hitTopWall || hitBottomWall
}

function random_food(min, max) {
    return Math.round((Math.random() * (max-min) + min) / 10) * 10;
}

function gen_food() {
    food_x = random_food(0, snakeboard.width - 10);
    food_y = random_food(0, snakeboard.height - 10);
    snake.forEach(function has_snake_eaten_food(part) {
        const has_eaten = part.x == food_x && part.y == food_y;
        if (has_eaten) gen_food();
    });
}

function drawFood() {
    snakeboard_ctx.fillStyle = 'lightgreen';
    snakeboard_ctx.strokestyle = 'darkgreen';
    snakeboard_ctx.fillRect(food_x, food_y, 10, 10);
    snakeboard_ctx.strokeRect(food_x, food_y, 10, 10);
}