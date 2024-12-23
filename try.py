import pygame
import numpy as np
import math

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)

# Инициализация Pygame и настройка экрана
def init_pygame(width=800, height=600):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Практическая работа №1")
    return screen


# Общая функция для обработки событий
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def Scale(list, coef):
    l = list.copy()
    for i in range(len(list)):
        l[i] *= coef
    return l

def Move(list, x, y):
    l = list.copy()
    for i in range(len(l)//2):
        l[2*i] += x
        l[2*i+1] += y
    return l

def tt(list, t):
    l = list.copy()
    for i in range(len(list)//2):
        l[2 * i] = t[0]*list[2 * i] + t[1] * list[2 * i + 1]
        l[2 * i + 1] = t[2] * list[2 * i] + t[3]*list[2 * i + 1]
    return l


# Задача 1
def task_1(screen):
    T = np.array([[1, 3], [4, 1]])
    point = np.array([[50], [100]])
    new_point = T @ point

    x, y = point.flatten()
    x_new, y_new = new_point.flatten()

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 5)
    pygame.draw.circle(screen, (255, 0, 0), (x_new, y_new), 5)

    pygame.display.flip()


# Задача 2
def task_2(screen):
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 50)
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (700, 500), 3)

    font = pygame.font.Font(None, 36)
    text = font.render("Привет, Pygame!", True, (0, 0, 0))
    screen.blit(text, (300, 50))

    pygame.display.flip()


# Задача 3
def task_3(screen):
    T = np.array([[1, 3], [4, 1]])
    segment = np.array([[10, 50], [100, 150]])
    new_segment = T @ segment

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, (0, 255, 0), segment[:, 0], segment[:, 1], 3)
    pygame.draw.line(screen, (255, 0, 0), new_segment[:, 0], new_segment[:, 1], 3)

    pygame.display.flip()


# Задача 4
def task_4(screen):
    T = np.array([[1, 2], [3, 1]])
    segment = np.array([[0, 80], [180, 260]])
    new_segment = T @ segment

    midpoint = np.mean(segment, axis=1).astype(int)
    new_midpoint = np.mean(new_segment, axis=1).astype(int)

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, (0, 255, 0), segment[:, 0], segment[:, 1], 3)
    pygame.draw.line(screen, (255, 0, 0), new_segment[:, 0], new_segment[:, 1], 3)
    pygame.draw.circle(screen, (0, 0, 255), midpoint, 5)
    pygame.draw.circle(screen, (0, 0, 255), new_midpoint, 5)
    pygame.draw.line(screen, (0, 0, 0), midpoint, new_midpoint, 2)

    pygame.display.flip()


# Задача 5
def task_5(screen):
    T = np.array([[1, 2], [3, 1]])
    segments = np.array([[25, 75, 25, 175], [225, 175, 225, 275]])
    new_segments = T @ segments

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, (0, 255, 0), segments[:, 0], segments[:, 1], 3)
    pygame.draw.line(screen, (0, 255, 0), segments[:, 2], segments[:, 3], 3)
    pygame.draw.line(screen, (255, 0, 0), new_segments[:, 0], new_segments[:, 1], 3)
    pygame.draw.line(screen, (255, 0, 0), new_segments[:, 2], new_segments[:, 3], 3)

    pygame.display.flip()


# Задача 6
def task_6(screen):
    L = np.array([[-0.5, 3/2], [3, -2], [-1, -1], [3, 5/3]])
    T = np.array([[1, 2],[1, -3]])

    L_scaled = L * 100
    L_transformed = np.dot(L_scaled, T)

    offset = np.array([WIDTH // 2, HEIGHT // 2])
    L_scaled_shifted = L_scaled + offset
    L_transformed_shifted = L_transformed + offset

    def draw_lines(screen, points, color):
        pygame.draw.line(screen, color, points[0], points[1], 2)
        pygame.draw.line(screen, color, points[2], points[3], 2)

    screen.fill(BACKGROUND_COLOR)
    draw_lines(screen, L_scaled_shifted, (255, 0, 0))
    draw_lines(screen, L_transformed_shifted, (0, 0, 255))

    pygame.display.flip()


# Задача 7
def task_7(screen):
    L = np.array([[3, -1], [4, 1], [2, 1]])
    T = np.array([[0, 1], [-1, 0]])

    L_scaled = L * 60
    L_transformed = np.dot(L_scaled, T)

    offset = np.array([WIDTH // 2, HEIGHT // 2])
    L_scaled_shifted = L_scaled + offset
    L_transformed_shifted = L_transformed + offset

    def draw_triangle(screen, points, color):
        pygame.draw.polygon(screen, color, points, 2)

    screen.fill(BACKGROUND_COLOR)
    draw_triangle(screen, L_scaled_shifted, (0, 128, 0))
    draw_triangle(screen, L_transformed_shifted, (0, 0, 128))

    pygame.display.flip()


# Задача 8
def task_8(screen):
    T = np.array([[0, 1], [1, 0]])
    triangle = np.array([[8, 7, 6], [1, 3, 2]]) * 50
    reflected_triangle = T @ triangle

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.polygon(screen, (0, 255, 0), triangle.T, 3)
    pygame.draw.polygon(screen, (255, 0, 0), reflected_triangle.T, 3)
    pygame.display.flip()


# Задача 9
def task_9(screen):
    T = np.array([[2, 0], [0, 2]])
    triangle = np.array([[5, 5, 3], [1, 2, 2]]) * 70
    scaled_triangle = T @ triangle

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.polygon(screen, (0, 255, 0), triangle.T, 3)
    pygame.draw.polygon(screen, (255, 0, 0), scaled_triangle.T, 3)
    pygame.display.flip()


# Задача 10
def task_10(screen):
    screen.fill(BACKGROUND_COLOR)

    b = 10
    a = 5
    points = []
    for theta in np.linspace(0, 4 * np.pi, 1000):
        r = b + 2 * a * math.cos(theta)
        x = r * math.cos(theta) + 400
        y = r * math.sin(theta) + 300
        points.append((x, y))

    pygame.draw.aalines(screen, (0, 0, 255), False, points)
    pygame.display.flip()


# Задача 11
def task_11(screen):
    import math
    x = [2, -2, -2, -2, -2, 2, 2, 2]
    t = [math.cos(math.pi/32),
         math.sin(math.pi/32),
         -math.sin(math.pi/32),
         math.cos(math.pi/32)]


    x = Scale(x, 100)
    for i in range(20):
        line = Move(x, 500, 300)
        pygame.draw.line(screen, (255, 0, 0), (line[0], line[1]), (line[2], line[3]))
        pygame.draw.line(screen, (255, 0, 0), (line[0], line[1]), (line[6], line[7]))
        pygame.draw.line(screen, (255, 0, 0), (line[4], line[5]), (line[2], line[3]))
        pygame.draw.line(screen, (255, 0, 0), (line[4], line[5]), (line[6], line[7]))
        x = tt(x, t)
        x = Scale(x, 0.9)
        pygame.display.flip()


if __name__ == "__main__":
    screen = init_pygame()

    while True:
        handle_events()
        task_11(screen)  # Заменить на вызов нужной задачи