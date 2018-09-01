import matplotlib.pyplot as plt

def plot_traing_accuracy_graph(history):
    plt.figure(figsize=[8, 6])
    plt.plot(history.history['acc'], 'r', linewidth=3.0)
    plt.plot(history.history['val_acc'], 'b', linewidth=3.0)
    plt.legend(["Training Accuracy", "Validation Accuracy"], fontsize=18)
    plt.xlabel("Epochs ", fontsize=16)
    plt.ylabel("Accuracy", fontsize=16)
    plt.title("Accuracy Curves", fontsize=16)