import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PicnicDecisionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Задача про пікнік")
        self.root.geometry("800x400")

        # ймовірність дощу 
        self.prob_label = ttk.Label(self.root, text="Ймовірність дощу:")
        self.prob_label.grid(row=0, column=0, padx=10, pady=10)

        self.rain_prob = tk.DoubleVar(value=0.3)
        self.rain_prob_slider = ttk.Scale(self.root, from_=0, to=1, orient="horizontal", variable=self.rain_prob)
        self.rain_prob_slider.grid(row=0, column=1, padx=10, pady=10)

        self.rain_prob_display = ttk.Label(self.root, text="0.30")
        self.rain_prob_display.grid(row=0, column=2, padx=10, pady=10)

        # очікувана користь ліс та дім
        self.expected_forest_label = ttk.Label(self.root, text="Очікувана користь (ліс):")
        self.expected_forest_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.expected_forest_value = ttk.Label(self.root, text="")
        self.expected_forest_value.grid(row=1, column=1, padx=10, pady=5)

        self.expected_home_label = ttk.Label(self.root, text="Очікувана користь (дім):")
        self.expected_home_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.expected_home_value = ttk.Label(self.root, text="")
        self.expected_home_value.grid(row=2, column=1, padx=10, pady=5)

        # таблиця корисності
        self.results_label = ttk.Label(self.root, text="Результат")
        self.results_label.grid(row=3, column=0, padx=10, pady=5)

        self.utility_label = ttk.Label(self.root, text="Корисність")
        self.utility_label.grid(row=3, column=1, padx=10, pady=5)

        self.utility_values = {"вкрай погано": 0, "погано": 2, "посередньо": 5, "чудово": 8}

        self.result_texts = ["вкрай погано", "погано", "посередньо", "чудово"]
        for i, res in enumerate(self.result_texts):
            ttk.Label(self.root, text=res).grid(row=4+i, column=0, padx=10, pady=2)  # Менший pady для зменшення відстані
            ttk.Label(self.root, text=self.utility_values[res]).grid(row=4+i, column=1, padx=10, pady=2)

        # кнопка 
        self.show_graph_button = ttk.Button(self.root, text="Показати графік", command=self.show_graph)
        self.show_graph_button.grid(row=9, column=0, padx=10, pady=10)

        # виведення
        self.decision_label = ttk.Label(self.root, text="Рішення: ")
        self.decision_label.grid(row=8, column=0, padx=10, pady=5)

        self.final_decision = ttk.Label(self.root, text="")
        self.final_decision.grid(row=8, column=1, padx=10, pady=5)

        self.update_decision()

    def update_decision(self):
        prob = self.rain_prob.get()
        self.rain_prob_display.config(text=f"{prob:.2f}")

        # розрахунок корисності
        u_forest = prob * 0 + (1 - prob) * 8  # ліс
        u_home = prob * 2 + (1 - prob) * 5    # дім

        
        self.expected_forest_value.config(text=f"{u_forest:.2f}")
        self.expected_home_value.config(text=f"{u_home:.2f}")

        # рішення
        if u_forest > u_home:
            self.final_decision.config(text="Йти в ліс")
        else:
            self.final_decision.config(text="Залишитись вдома")

    def show_graph(self):
        prob = self.rain_prob.get()

        # вікно
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Графік рішення про пікнік")

        # графік
        figure, ax = plt.subplots(figsize=(5, 4))
        canvas = FigureCanvasTkAgg(figure, master=graph_window)
        canvas.get_tk_widget().pack()

        
        probabilities = [0, 1]
        forest_values = [8, 0]
        home_values = [5, 2]


        ax.plot(probabilities, forest_values, label="Ліс", color="purple")
        ax.plot(probabilities, home_values, label="Дім", color="blue")

        ax.set_title(f"Ймовірність дощу: {prob:.2f}")
        ax.set_xlabel("Ймовірність дощу")
        ax.set_ylabel("Корисність")
        ax.legend()

        canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = PicnicDecisionApp(root)
    
    
    app.rain_prob_slider.config(command=lambda event: app.update_decision())
    
    root.mainloop()
