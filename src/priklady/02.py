import matplotlib.pyplot as plt

def load_signal_from_txt(path):
    values = []
    with open(path, "r") as f:
        for i in f:
            i = i.strip()
            if i != "":
                values.append(float(i))
    return values

def signal_min(values):
    return min(values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return sum(values) / len(values)

def plot_signal(values):
    plt.plot(values)
    plt.title("Signal")
    plt.show()


print("Modul sa nacital")


if __name__ == "__main__":

    data = load_signal_from_txt("ekg_signal.txt")

    print("Minimum:", signal_min(data))
    print("Maximum:", signal_max(data))
    print("Priemer:", signal_avg(data))

    plot_signal(data)