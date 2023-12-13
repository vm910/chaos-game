import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from utils import *

LAST_POINT = None
LAST_VERTEX = None
LAST_VERTEX_INDEX = None
SECOND_LAST_VERTEX = None
SECOND_LAST_VERTEX_INDEX = None
PREVIOUS_VERTEX = None
MAIN_VERTICES = None
BATCH_SIZE = 1000

all_points = []


def get_constraints(n):
    if n == 3:
        return lambda last, current: False
    if n == 4:
        return lambda last, current: np.array_equal(last, current)
    if n == 5:
        return lambda last, current: np.array_equal(last, current)


def generate_points(num_points, n):
    global LAST_POINT, LAST_VERTEX, MAIN_VERTICES, all_points, LAST_VERTEX_INDEX
    constraint = get_constraints(n)
    for _ in range(num_points):
        random_main_vertex = np.array(
            MAIN_VERTICES[np.random.randint(0, len(MAIN_VERTICES))]
        )
        vertex_index = MAIN_VERTICES.index(tuple(random_main_vertex))
        while constraint(LAST_VERTEX, random_main_vertex):
            random_main_vertex = np.array(
                MAIN_VERTICES[np.random.randint(0, len(MAIN_VERTICES))]
            )
        LAST_POINT = (random_main_vertex + LAST_POINT) / 2.0
        LAST_VERTEX = random_main_vertex
        LAST_VERTEX_INDEX = MAIN_VERTICES.index(tuple(LAST_VERTEX))
        all_points.append(LAST_POINT)


def animate_chaos_game(i):
    global sc, all_points

    start_index = i * BATCH_SIZE
    end_index = start_index + BATCH_SIZE

    batch_points = all_points[start_index:end_index]
    new_offsets = np.array(batch_points)

    current_offsets = sc.get_offsets()
    updated_offsets = np.vstack([current_offsets, new_offsets])
    sc.set_offsets(updated_offsets)

    return (sc,)


def show_fractal(n):
    global LAST_POINT, LAST_VERTEX, MAIN_VERTICES, all_points, BATCH_SIZE, sc, LAST_VERTEX_INDEX

    x0 = np.random.uniform(0, 100)
    y0 = np.random.uniform(0, 100)

    if n == 3:
        MAIN_VERTICES = equilateral_triangle_vertices(x0, y0)
        LAST_POINT = random_point_in_triangle(*MAIN_VERTICES)
    elif n == 4:
        MAIN_VERTICES = square_vertices(x0, y0)
        LAST_VERTEX_INDEX = 0
        LAST_POINT = random_point_in_square(MAIN_VERTICES[0], MAIN_VERTICES[2])
    elif n == 5:
        MAIN_VERTICES = regular_pentagon_vertices(x0, y0)
        LAST_POINT = random_point_in_pentagon(MAIN_VERTICES)

    fig, ax = plt.subplots(figsize=(6, 6))
    x_values, y_values = zip(*MAIN_VERTICES)
    x_values = list(x_values) + [x_values[0]]
    y_values = list(y_values) + [y_values[0]]

    # ax.plot(x_values, y_values, c="black")
    sc = plt.scatter(*LAST_POINT, c="black", s=0.01)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(min(x_values) - 1, max(x_values) + 1)
    ax.set_ylim(min(y_values) - 1, max(y_values) + 1)

    generate_points(35000, len(MAIN_VERTICES))

    frames_needed = (len(all_points) + BATCH_SIZE - 1) // BATCH_SIZE
    ani = animation.FuncAnimation(
        fig, animate_chaos_game, frames=frames_needed, interval=10
    )
    plt.show()


def main():
    # show_fractal(3)
    show_fractal(4)
    # show_fractal(5)


if __name__ == "__main__":
    main()
