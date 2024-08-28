import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블럭깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 공 클래스 정의
class Ball:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 10
        self.x_speed = 3 * random.choice((1, -1))
        self.y_speed = 3 * random.choice((1, -1))

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        # 화면 가장자리에 닿으면 반사
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.x_speed *= -1
        if self.y - self.radius <= 0:
            self.y_speed *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

# 패들 클래스 정의
class Paddle:
    def __init__(self):
        self.width = 400
        self.height = 10
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - 20
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# 블럭 클래스 정의
class Brick:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.x = x
        self.y = y
        self.hit = False

    def draw(self, screen):
        if not self.hit:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# 블럭 배열 생성
bricks = []
for i in range(6):
    for j in range(5):
        brick = Brick(i * 70 + 35, j * 30 + 30)
        bricks.append(brick)

# 게임 실행 루프
def main():
    clock = pygame.time.Clock()
    ball = Ball()
    paddle = Paddle()
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.move()
        paddle.move()

        # 공과 패들의 충돌 감지
        if ball.y + ball.radius >= paddle.y and paddle.x <= ball.x <= paddle.x + paddle.width:
            ball.y_speed *= -1

        # 공과 블럭의 충돌 감지
        for brick in bricks:
            if not brick.hit and brick.x <= ball.x <= brick.x + brick.width and brick.y <= ball.y <= brick.y + brick.height:
                ball.y_speed *= -1
                brick.hit = True

        # 공이 바닥에 닿으면 게임 종료
        if ball.y + ball.radius > screen_height:
            running = False

        # 화면 그리기
        screen.fill(BLACK)
        ball.draw(screen)
        paddle.draw(screen)
        for brick in bricks:
            brick.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
