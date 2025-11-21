"""
PONG — Single-file Python implementation with clear decomposition & comments.

Requirements:
    pip install pygame

Run:
    python pong.py

Controls:
    Player Left  : W (up), S (down)
    Player Right : Up Arrow (up), Down Arrow (down)
    Pause        : P
    Quit         : ESC or window close button

Design overview (decomposition):
    - Constants: All configurable numbers/colors in one place.
    - Data classes / Entities:
        * Paddle: position, movement, rendering, boundary clamping.
        * Ball  : position, velocity, movement, collision response, reset.
    - Systems:
        * InputSystem: reads keyboard state and produces paddle movement.
        * PhysicsSystem: updates positions and resolves collisions.
        * RenderSystem : draws everything to the screen.
        * ScoreSystem  : tracks and displays score, handles round reset.
    - Game loop: orchestrates input → update → render at a fixed timestep.

This structure mirrors how you would decompose a small arcade game into
independent, testable parts while keeping it approachable for students.
"""
from __future__ import annotations
import math
import random
import sys
from dataclasses import dataclass
import pygame

# =============================
# === 1) GLOBAL CONFIGURATION ===
# =============================
WIDTH, HEIGHT = 960, 540          # Window size (16:9 friendly)
FPS = 60                          # Target frames per second

# Gameplay tuning constants (tweak these to rebalance feel)
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 200
PADDLE_SPEED = 420                # pixels per second
BALL_SIZE = 12                    # Ball is a square for simple AABB collisions
BALL_SPEED_START = 360            # Initial speed after serve
BALL_SPEED_MAX = 940              # Cap to avoid tunneling / impossible speeds
BALL_ACCEL = 1.04                 # Multiply speed after every paddle hit
MAX_BOUNCE_ANGLE = math.radians(60)  # Max deflection based on contact point
SCORE_TO_WIN = 7

# Colors (RGB)
WHITE = (250, 250, 250)
GREY  = (35, 35, 40)
ACCENT= (90, 200, 250)

FONT_NAME = "freesansbold.ttf"   # Pygame built-in font


# ==================================
# === 2) DATA CLASSES / ENTITIES ===
# ==================================
@dataclass
class Paddle:
    """Player-controlled or AI paddle.

    Attributes:
        x, y   : Top-left position (floats for smooth motion).
        w, h   : Dimensions.
        vy     : Vertical velocity (pixels/sec), set by InputSystem or AI.
    """
    x: float
    y: float
    w: int = PADDLE_WIDTH
    h: int = PADDLE_HEIGHT
    vy: float = 0.0

    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)

    def update(self, dt: float):
        """Integrate vertical velocity and clamp to screen bounds."""
        self.y += self.vy * dt
        self.y = max(0, min(HEIGHT - self.h, self.y))

    def draw(self, surf: pygame.Surface):
        pygame.draw.rect(surf, WHITE, self.rect(), border_radius=3)


@dataclass
class Ball:
    """Game ball state and behavior."""
    x: float
    y: float
    size: int = BALL_SIZE
    vx: float = 0.0
    vy: float = 0.0

    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)

    def center(self) -> pygame.Vector2:
        return pygame.Vector2(self.x + self.size / 2, self.y + self.size / 2)

    def draw(self, surf: pygame.Surface):
        pygame.draw.rect(surf, WHITE, self.rect(), border_radius=3)

    def serve(self, direction: int):
        """Start the ball moving either left (-1) or right (+1).
        A little random vertical angle makes each serve unique.
        """
        speed = BALL_SPEED_START
        angle = random.uniform(-MAX_BOUNCE_ANGLE * 0.6, MAX_BOUNCE_ANGLE * 0.6)
        self.vx = direction * speed * math.cos(angle)
        self.vy = speed * math.sin(angle)

    def reset_to_center(self):
        self.x = WIDTH / 2 - self.size / 2
        self.y = HEIGHT / 2 - self.size / 2
        self.vx = self.vy = 0.0


# =========================
# === 3) GAME SUBSYSTEMS ===
# =========================
class InputSystem:
    """Reads keyboard and sets paddles' velocities.

    Decoupling input lets us later plug in AI or other control schemes.
    """
    def update(self, keys, left: Paddle, right: Paddle):
        # Reset velocities each frame; then apply based on key state
        left.vy = 0
        right.vy = 0

        if keys[pygame.K_w]:
            left.vy -= PADDLE_SPEED
        if keys[pygame.K_s]:
            left.vy += PADDLE_SPEED

        if keys[pygame.K_UP]:
            right.vy -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            right.vy += PADDLE_SPEED


class SimpleAI:
    """Optional: tracks the ball with a capped response speed.

    Use for single-player by replacing InputSystem control for `right`.
    """
    def __init__(self, reaction_speed: float = 0.85):
        self.reaction = reaction_speed  # 0..1 fraction of paddle speed

    def update(self, ball: Ball, paddle: Paddle):
        target_y = ball.y + ball.size / 2 - paddle.h / 2
        # Move towards target with capped speed
        dy = target_y - paddle.y
        max_step = PADDLE_SPEED * self.reaction / FPS
        step = max(-max_step, min(max_step, dy))
        paddle.vy = step * FPS  # convert per-frame step back to velocity


class PhysicsSystem:
    """Moves entities and resolves collisions and scoring."""
    def __init__(self, left: Paddle, right: Paddle, ball: Ball):
        self.left = left
        self.right = right
        self.ball = ball

    def update(self, dt: float) -> tuple[int, int]:
        """Return (score_left, score_right) deltas for this frame."""
        score_l = score_r = 0

        # 1) Integrate motion
        self.left.update(dt)
        self.right.update(dt)
        self.ball.x += self.ball.vx * dt
        self.ball.y += self.ball.vy * dt

        # 2) Wall collisions (top/bottom)
        if self.ball.y <= 0:
            self.ball.y = 0
            self.ball.vy = abs(self.ball.vy)
        elif self.ball.y + self.ball.size >= HEIGHT:
            self.ball.y = HEIGHT - self.ball.size
            self.ball.vy = -abs(self.ball.vy)

        # 3) Paddle collisions
        self._maybe_collide_with_paddle(self.left, is_left=True)
        self._maybe_collide_with_paddle(self.right, is_left=False)

        # 4) Scoring (ball leaves left/right)
        if self.ball.x + self.ball.size < 0:  # right player scores
            score_r = 1
            self.ball.reset_to_center()
        elif self.ball.x > WIDTH:             # left player scores
            score_l = 1
            self.ball.reset_to_center()

        return score_l, score_r

    def _maybe_collide_with_paddle(self, paddle: Paddle, *, is_left: bool):
        if self.ball.rect().colliderect(paddle.rect()):
            # Place ball outside the paddle to prevent sticking
            if is_left:
                self.ball.x = paddle.x + paddle.w
            else:
                self.ball.x = paddle.x - self.ball.size

            # Compute contact point relative to paddle center (-1..+1)
            paddle_center = paddle.y + paddle.h / 2
            rel = (self.ball.y + self.ball.size / 2 - paddle_center) / (paddle.h / 2)
            rel = max(-1.0, min(1.0, rel))

            # Convert relative contact to bounce angle
            angle = rel * MAX_BOUNCE_ANGLE
            speed = min(BALL_SPEED_MAX, math.hypot(self.ball.vx, self.ball.vy) * BALL_ACCEL)

            # New velocity aims away from the paddle
            dir_x = 1 if is_left else -1
            self.ball.vx = dir_x * speed * math.cos(angle)
            self.ball.vy = speed * math.sin(angle)


class ScoreSystem:
    """Tracks scores and win condition; handles serving after points."""
    def __init__(self, ball: Ball):
        self.left = 0
        self.right = 0
        self.ball = ball
        self.next_serve_dir = random.choice([-1, 1])

    def add(self, dl: int, dr: int):
        self.left += dl
        self.right += dr
        if dl or dr:
            # After a point, serve again from center
            self.ball.reset_to_center()
            self.ball.serve(self.next_serve_dir if dr else -self.next_serve_dir)
            # Alternate who serves next time to keep variety
            self.next_serve_dir *= -1

    def someone_won(self) -> bool:
        return self.left >= SCORE_TO_WIN or self.right >= SCORE_TO_WIN


class RenderSystem:
    """All drawing code lives here to keep logic clean."""
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font

    def draw(self, left: Paddle, right: Paddle, ball: Ball, score: ScoreSystem):
        # Clear
        self.screen.fill(GREY)

        # Center line (dashed)
        dash_h = 18
        gap = 12
        x = WIDTH // 2
        y = 0
        while y < HEIGHT:
            pygame.draw.rect(self.screen, (60, 60, 68), pygame.Rect(x - 2, y, 4, dash_h), border_radius=2)
            y += dash_h + gap

        # Entities
        left.draw(self.screen)
        right.draw(self.screen)
        ball.draw(self.screen)

        # Score text
        sl = self.font.render(str(score.left), True, ACCENT)
        sr = self.font.render(str(score.right), True, ACCENT)
        self.screen.blit(sl, (WIDTH * 0.25 - sl.get_width() / 2, 24))
        self.screen.blit(sr, (WIDTH * 0.75 - sr.get_width() / 2, 24))

        pygame.display.flip()


# ==================
# === 4) THE GAME ===
# ==================
class Game:
    """Main game that wires subsystems together and runs the loop."""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong — Decomposed & Commented")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_NAME, 64)

        # Entities
        margin = 24
        self.left = Paddle(x=margin, y=HEIGHT/2 - PADDLE_HEIGHT/2)
        self.right = Paddle(x=WIDTH - margin - PADDLE_WIDTH, y=HEIGHT/2 - PADDLE_HEIGHT/2)
        self.ball = Ball(x=WIDTH/2 - BALL_SIZE/2, y=HEIGHT/2 - BALL_SIZE/2)

        # Systems
        self.input_sys = InputSystem()
        # self.ai = SimpleAI(reaction_speed=0.9)  # Uncomment to enable AI for right paddle
        self.physics = PhysicsSystem(self.left, self.right, self.ball)
        self.score = ScoreSystem(self.ball)
        self.render = RenderSystem(self.screen, self.font)

        # Serve the first ball
        self.ball.serve(direction=random.choice([-1, 1]))

        self.running = True
        self.paused = False

    def run(self):
        """Canonical game loop: input → update → render."""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Convert ms to seconds
            self._handle_events()

            if not self.paused:
                # Input
                keys = pygame.key.get_pressed()
                self.input_sys.update(keys, self.left, self.right)
                # If you want AI on the right paddle, comment the line above and uncomment below:
                # self.input_sys.update(keys, self.left, self.right)  # still controls left
                # self.ai.update(self.ball, self.right)

                # Update (physics + scoring)
                dl, dr = self.physics.update(dt)
                self.score.add(dl, dr)

            # Render (always draw, even when paused)
            self.render.draw(self.left, self.right, self.ball, self.score)

            if self.score.someone_won():
                self._show_winner_and_reset()

        pygame.quit()

    def _show_winner_and_reset(self):
        """Display winner screen briefly, then reset the match."""
        winner = "Left" if self.score.left >= SCORE_TO_WIN else "Right"
        text = self.font.render(f"{winner} Wins!", True, WHITE)
        subfont = pygame.font.Font(FONT_NAME, 24)
        sub = subfont.render("Press SPACE to play again or ESC to quit", True, WHITE)
        # Simple overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - 60))
        self.screen.blit(sub, (WIDTH/2 - sub.get_width()/2, HEIGHT/2 + 10))
        pygame.display.flip()

        # Wait for user decision
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        waiting = False

        # Reset match
        self.left.y = HEIGHT/2 - PADDLE_HEIGHT/2
        self.right.y = HEIGHT/2 - PADDLE_HEIGHT/2
        self.score.left = self.score.right = 0
        self.ball.reset_to_center()
        self.ball.serve(direction=random.choice([-1, 1]))

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused


# Entry point guard keeps this import-safe
if __name__ == "__main__":
    try:
        Game().run()
    except Exception as e:
        # Fail gracefully with a helpful message instead of a stack trace wall
        print("An error occurred:", e)
        print("• Make sure pygame is installed (pip install pygame)")
        print("• Some environments (like headless servers) cannot open a window.")
