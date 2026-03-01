import math
import matplotlib.pyplot as plt


def draw_branch(ax, x, y, angle, length, depth):
    if depth == 0 or length < 1e-3:
        return

    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)
    ax.plot([x, x2], [y, y2])

    # draw two branches of tree
    new_len = length * 0.7
    draw_branch(ax, x2, y2, angle + math.radians(30), new_len, depth - 1)
    draw_branch(ax, x2, y2, angle - math.radians(30), new_len, depth - 1)


def pif_tree(depth: int):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    draw_branch(ax, x=0.0, y=0.0, angle=math.radians(90), length=1.0, depth=depth)
    plt.show()


if __name__ == "__main__":
    depth = int(input("Input Please Level Of recursion (e.g. 8-12): ").strip())
    pif_tree(depth)