import pygame
import sys
import random
import time

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 48
MENU_FONT_SIZE = 36
LETTER_FONT_SIZE = 720
SHAPE_SIZE = 500

COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
}
SHAPES = ["square", "rectangle", "triangle", "circle", "star"]
LETTERS = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

KEYS = ["F", "J"]

pygame.init()
pygame.display.set_caption("Learn Colors, Shapes, and Letters")
clock = pygame.time.Clock()

# --- Utility Functions ---
def draw_text(surface, text, font, color, center):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=center)
    surface.blit(rendered, rect)

def draw_shape(surface, shape, center):
    if shape == "square":
        rect = centered_rect(center, SHAPE_SIZE, SHAPE_SIZE)
        pygame.draw.rect(surface, (0, 0, 0), rect, 0)
    elif shape == "rectangle":
        rect = centered_rect(center, SHAPE_SIZE, SHAPE_SIZE // 2)
        pygame.draw.rect(surface, (0, 0, 0), rect, 0)
    elif shape == "triangle":
        points = [
            (center[0], center[1] - SHAPE_SIZE // 2),
            (center[0] - SHAPE_SIZE // 2, center[1] + SHAPE_SIZE // 2),
            (center[0] + SHAPE_SIZE // 2, center[1] + SHAPE_SIZE // 2),
        ]
        pygame.draw.polygon(surface, (0, 0, 0), points)
    elif shape == "circle":
        pygame.draw.circle(surface, (0, 0, 0), center, SHAPE_SIZE // 2)
    elif shape == "star":
        draw_star(surface, center, SHAPE_SIZE // 2, SHAPE_SIZE // 4, 5, (0, 0, 0))

def centered_rect(center, w, h):
    return (center[0] - w // 2, center[1] - h // 2, w, h)

def draw_star(surface, center, outer_radius, inner_radius, points, color):
    angle = 0
    step = 3.14159 / points
    vertices = []
    for i in range(points * 2):
        r = outer_radius if i % 2 == 0 else inner_radius
        x = center[0] + int(r * pygame.math.cos(angle))
        y = center[1] + int(r * pygame.math.sin(angle))
        vertices.append((x, y))
        angle += step
    pygame.draw.polygon(surface, color, vertices)

def wait_for_key(keys):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in keys:
                return event.key

def get_key_name(key):
    if key == pygame.K_f:
        return "F"
    elif key == pygame.K_j:
        return "J"
    elif key == pygame.K_SPACE:
        return "Space"
    elif key == pygame.K_ESCAPE:
        return "Esc"
    return pygame.key.name(key)

# --- Menu Functions ---
def menu_select_category(screen, font):
    categories = ["Colors", "Shapes", "Letters"]
    selected = 0
    while True:
        screen.fill((220, 220, 220))
        draw_text(screen, "Select a Category", font, (0, 0, 0), (SCREEN_WIDTH // 2, 100))
        for i, cat in enumerate(categories):
            color = (0, 0, 255) if i == selected else (0, 0, 0)
            draw_text(screen, cat, font, color, (SCREEN_WIDTH // 2, 200 + i * 80))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(categories)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(categories)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return categories[selected].lower()

def menu_select_items(screen, font, category, options):
    selected = set()
    idx = 0
    while True:
        screen.fill((220, 220, 220))
        draw_text(screen, f"Select 2 {category.title()} (Space to confirm)", font, (0, 0, 0), (SCREEN_WIDTH // 2, 60))
        if category == "letters":
            col_count = 3
            row_count = (len(options) + col_count - 1) // col_count
            col_width = SCREEN_WIDTH // (col_count + 1)
            start_x = SCREEN_WIDTH // 2 - col_width
            for i, opt in enumerate(options):
                col = i // row_count
                row = i % row_count
                x = start_x + col * col_width
                y = 120 + row * 40
                color = (0, 0, 255) if i == idx else (0, 0, 0)
                mark = "[X]" if opt in selected else "[ ]"
                draw_text(screen, f"{mark} {opt.title()}", font, color, (x, y))
        else:
            for i, opt in enumerate(options):
                color = (0, 0, 255) if i == idx else (0, 0, 0)
                mark = "[X]" if opt in selected else "[ ]"
                draw_text(screen, f"{mark} {opt.title()}", font, color, (SCREEN_WIDTH // 2, 120 + i * 40))
        draw_text(screen, f"Selected: {', '.join([o.title() for o in selected])}", font, (0, 128, 0), (SCREEN_WIDTH // 2, 500))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    idx = (idx - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    idx = (idx + 1) % len(options)
                elif event.key == pygame.K_SPACE:
                    if len(selected) == 2:
                        return list(selected)
                elif event.key == pygame.K_RETURN:
                    if options[idx] in selected:
                        selected.remove(options[idx])
                    elif len(selected) < 2:
                        selected.add(options[idx])

def menu_assign_keys(screen, font, items):
    assignments = {KEYS[0]: items[0], KEYS[1]: items[1]}
    while True:
        screen.fill((220, 220, 220))
        draw_text(screen, "Key Assignments", font, (0, 0, 0), (SCREEN_WIDTH // 2, 100))
        draw_text(screen, f"F: {items[0].title()}", font, (0, 0, 0), (SCREEN_WIDTH // 2, 200))
        draw_text(screen, f"J: {items[1].title()}", font, (0, 0, 0), (SCREEN_WIDTH // 2, 280))
        draw_text(screen, "Press Space to start", font, (0, 128, 0), (SCREEN_WIDTH // 2, 400))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return assignments

# --- Gameplay Functions ---
def run_game(screen, category, assignments, font, letter_font):
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.get_surface()
    items = [assignments[KEYS[0]], assignments[KEYS[1]]]
    stats = {
        "correct": 0,
        "wrong": 0,
        "skipped": 0,
        "response_times": [],
        "total": 0,
    }
    running = True
    while running:
        item = random.choice(items)
        start_time = time.time()
        screen.fill((255, 255, 255))
        if category == "colors":
            screen.fill(COLORS[item])
        elif category == "shapes":
            draw_shape(screen, item, (screen.get_width() // 2, screen.get_height() // 2))
        elif category == "letters":
            draw_text(screen, item, letter_font, (0, 0, 0), (screen.get_width() // 2, screen.get_height() // 2))
        pygame.display.flip()
        responded = False
        while not responded:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    return stats
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                        return stats
                    elif event.key == pygame.K_f or event.key == pygame.K_j:
                        guess = assignments[get_key_name(event.key)]
                        stats["total"] += 1
                        if guess == item:
                            stats["correct"] += 1
                        else:
                            stats["wrong"] += 1
                        stats["response_times"].append(time.time() - start_time)
                        responded = True
                    elif event.key == pygame.K_SPACE:
                        stats["skipped"] += 1
                        responded = True
        clock.tick(FPS)

# --- Score Screen ---
def show_score(screen, font, stats):
    screen.fill((220, 220, 220))
    total_guesses = stats["correct"] + stats["wrong"]
    percent = (stats["correct"] / total_guesses * 100) if total_guesses > 0 else 0
    avg_time = (sum(stats["response_times"]) / len(stats["response_times"])) if stats["response_times"] else 0
    draw_text(screen, "Score Summary", font, (0, 0, 0), (SCREEN_WIDTH // 2, 80))
    draw_text(screen, f"Correct: {stats['correct']}", font, (0, 128, 0), (SCREEN_WIDTH // 2, 160))
    draw_text(screen, f"Wrong: {stats['wrong']}", font, (255, 0, 0), (SCREEN_WIDTH // 2, 220))
    draw_text(screen, f"Skipped: {stats['skipped']}", font, (128, 128, 128), (SCREEN_WIDTH // 2, 280))
    draw_text(screen, f"Percent Correct: {percent:.1f}%", font, (0, 0, 255), (SCREEN_WIDTH // 2, 340))
    draw_text(screen, f"Avg Response Time: {avg_time:.2f}s", font, (0, 0, 0), (SCREEN_WIDTH // 2, 400))
    draw_text(screen, "Press Space to return to menu", font, (0, 128, 0), (SCREEN_WIDTH // 2, 500))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

# --- Main Loop ---
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont("arial", MENU_FONT_SIZE)
    letter_font = pygame.font.SysFont("arial", LETTER_FONT_SIZE)
    while True:
        category = menu_select_category(screen, font)
        if category == "colors":
            options = list(COLORS.keys())
        elif category == "shapes":
            options = SHAPES
        elif category == "letters":
            options = LETTERS
        items = menu_select_items(screen, font, category, options)
        assignments = menu_assign_keys(screen, font, items)
        stats = run_game(screen, category, assignments, font, letter_font)
        show_score(screen, font, stats)

if __name__ == "__main__":
    main()