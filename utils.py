import numpy as np


def equilateral_triangle_vertices(x0, y0, side_len=500):
    Ax, Ay = x0, y0
    Bx, By = Ax + side_len, Ay
    Cx, Cy = Ax + side_len / 2.0, Ay + side_len * np.sqrt(3) / 2
    return [(Ax, Ay), (Bx, By), (Cx, Cy)]


def square_vertices(x0, y0, side_len=500):
    Ax, Ay = x0, y0
    Bx, By = Ax + side_len, Ay
    Cx, Cy = Ax + side_len, Ay + side_len
    Dx, Dy = Ax, Ay + side_len
    return [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]


def regular_pentagon_vertices(x0, y0, side_len=500):
    r = side_len / (2 * np.sin(np.pi / 5))
    angles = [2 * np.pi * i / 5 for i in range(5)]
    return [(x0 + r * np.sin(angle), y0 + r * np.cos(angle)) for angle in angles]


def random_point_in_pentagon(vertices):
    center_x = sum(v[0] for v in vertices) / 5
    center_y = sum(v[1] for v in vertices) / 5
    center = (center_x, center_y)

    triangle_idx = np.random.randint(5)
    A = vertices[triangle_idx]
    B = vertices[(triangle_idx + 1) % 5]

    s, t = np.random.rand(2)
    if s + t > 1:
        s, t = 1 - s, 1 - t

    x = center[0] + s * (A[0] - center[0]) + t * (B[0] - center[0])
    y = center[1] + s * (A[1] - center[1]) + t * (B[1] - center[1])

    return x, y


def random_point_in_triangle(A, B, C):
    s, t = np.random.rand(2)
    if s + t > 1:
        s, t = 1 - s, 1 - t
    x = A[0] + s * (B[0] - A[0]) + t * (C[0] - A[0])
    y = A[1] + s * (B[1] - A[1]) + t * (C[1] - A[1])
    return x, y


def random_point_in_square(A, C):
    Ax, Ay = A
    Cx, Cy = C
    return np.random.uniform(Ax, Cx), np.random.uniform(Ay, Cy)
