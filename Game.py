import pygame
import time
from Test_Script import TestMethods

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 520
WHITE = (255, 255, 255)
GRAY = (145, 145, 145)
BLACK = (0, 0, 0)
BLOCK_SIZE = 40
MAZE_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
MAZE_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
RUNNING = True
BALL_INIT_X = 1 * BLOCK_SIZE
BALL_INIT_Y = MAZE_HEIGHT * BLOCK_SIZE
Test = TestMethods()
Result = []


def draw_maze(screen):
    global maze
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                rect = pygame.Rect(
                    col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                )
                pygame.draw.rect(screen, GRAY, rect)
    return maze


class Ball:
    def __init__(self, x, y, maze):
        self.x = BALL_INIT_X
        self.y = BALL_INIT_Y
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 20
        self.maze = maze
        self.message = ""

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        if (self.x >= BLOCK_SIZE * 11 and self.x < BLOCK_SIZE * 12) and (
            self.y >= BLOCK_SIZE * 1 and self.y < BLOCK_SIZE * 2
        ):
            self.message = "Reached end!"
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
        # Prevent from leaving the screen
        if self.x < 0:
            self.x = 0
        if self.x + self.size > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.size
        if self.y < 0:
            self.y = 0
        if self.y + self.size > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.size
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == 1:
                    wall_rect = pygame.Rect(
                        col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                    )
                    if wall_rect.colliderect(
                        pygame.Rect(self.x, self.y, self.size, self.size)
                    ):
                        # Adjust ball position to be just outside wall
                        if self.x + self.size > wall_rect.x:
                            self.x -= self.velocity_x
                        if self.x < wall_rect.x + wall_rect.width:
                            self.x -= self.velocity_x
                        if self.y + self.size > wall_rect.y:
                            self.y -= self.velocity_y
                        if self.y < wall_rect.y + wall_rect.height:
                            self.y -= self.velocity_y

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.ellipse(screen, WHITE, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    maze = draw_maze(screen)
    ball = Ball(40, 40, maze)

    font = pygame.font.Font(None, 30)

    # Buttons
    up_button = pygame.Rect(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT - 500, 100, 50)
    down_button = pygame.Rect(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT - 300, 100, 50)
    left_button = pygame.Rect(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT - 400, 100, 50)
    right_button = pygame.Rect(SCREEN_WIDTH // 2 + 300, SCREEN_HEIGHT - 400, 100, 50)

    # Draw message
    text = font.render("<- END", True, WHITE)
    rotated_text = pygame.transform.rotate(text, 270)

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(Result)
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if up_button.collidepoint(event.pos):
                    ball.velocity_x, ball.velocity_y = checkSignal("yukari1.txt")
                if down_button.collidepoint(event.pos):
                    ball.velocity_x, ball.velocity_y = checkSignal("asagi1.txt")
                if left_button.collidepoint(event.pos):
                    ball.velocity_x, ball.velocity_y = checkSignal("sol1.txt")
                if right_button.collidepoint(event.pos):
                    ball.velocity_x, ball.velocity_y = checkSignal("sag1.txt")
            if event.type == pygame.MOUSEBUTTONUP:
                ball.velocity_y = 0
                ball.velocity_x = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.velocity_x = -5
                elif event.key == pygame.K_RIGHT:
                    ball.velocity_x = 5
                elif event.key == pygame.K_UP:
                    ball.velocity_y = -5
                elif event.key == pygame.K_DOWN:
                    ball.velocity_y = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ball.velocity_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ball.velocity_y = 0

        ball.update()
        draw_maze(screen)
        ball.draw(screen)
        # pygame.display.flip()
        clock.tick(60)
        pygame.draw.rect(screen, WHITE, up_button)
        screen.blit(
            font.render("UP", True, BLACK),
            (up_button.x + 25, up_button.y + 15),
        )

        pygame.draw.rect(screen, WHITE, down_button)
        screen.blit(
            font.render("DOWN", True, BLACK),
            (down_button.x + 15, down_button.y + 15),
        )

        pygame.draw.rect(screen, WHITE, left_button)
        screen.blit(
            font.render("LEFT", True, BLACK),
            (left_button.x + 25, left_button.y + 15),
        )

        pygame.draw.rect(screen, WHITE, right_button)
        screen.blit(
            font.render("RIGHT", True, BLACK),
            (right_button.x + 15, right_button.y + 15),
        )
        screen.blit(rotated_text, (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT - 430))
        pygame.display.flip()
        screen.fill(BLACK)


def checkSignal(signal):
    move = Test.SVM_with_Wavelets_Features(signal)[0]
    print("Classification Result: ", move)
    Result.append(move)
    if move == "Up":
        return 0, -5
    elif move == "Down":
        return 0, 5
    elif move == "Left":
        return -5, 0
    elif move == "Right":
        return 5, 0
    else:
        return 0, 0


if __name__ == "__main__":
    main()
