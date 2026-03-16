import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):

    fig, ax = plt.subplots()

    c1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"], fill=False, color="blue")
    c2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"], fill=False, color="red")

    ax.add_patch(c1)
    ax.add_patch(c2)

    ax.set_aspect("equal")
    plt.title("Kruznice")
    plt.show()