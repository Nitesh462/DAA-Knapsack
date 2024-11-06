import tkinter as tk
from tkinter import messagebox

# Function to calculate max profit and items used
def calculate_profit():
    try:
        k = int(entry_items.get())
        profits = list(map(int, entry_profits.get().split()))
        weights = list(map(int, entry_weights.get().split()))
        capacity = int(entry_capacity.get())
        
        # Ensure input validation for the correct number of items
        if len(profits) != k or len(weights) != k:
            raise ValueError("Mismatch in item count, profits, and weights.")
        
        # Calculate profit-to-weight ratio
        items = [[profits[i], weights[i], profits[i] / weights[i]] for i in range(k)]
        items.sort(key=lambda x: x[2], reverse=True)
        
        max_profit = 0
        items_used = []  # Track items or fractions of items used
        
        for profit, weight, ratio in items:
            if capacity >= weight:
                max_profit += profit
                capacity -= weight
                items_used.append(f"Full item with profit {profit} and weight {weight}")
            else:
                max_profit += capacity * ratio
                items_used.append(f"Fractional item with profit {capacity * ratio:.2f} and weight {capacity}")
                break

        # Display the maximum profit in the result entry box
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{max_profit:.2f}")
        
        # Display the items used in the items_used_label
        items_used_label.config(text="Items Used:\n" + "\n".join(items_used))
        
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Please enter valid inputs.")

# Tkinter UI setup
root = tk.Tk()
root.title("Fractional Knapsack Calculator")
root.geometry("400x350")  # Set window size
root.resizable(False, False)

# UI elements for input
tk.Label(root, text="Number of Items:").grid(row=0, column=0, pady=5, sticky="e")
entry_items = tk.Entry(root, width=20)
entry_items.grid(row=0, column=1, pady=5)

tk.Label(root, text="Profits (space-separated):").grid(row=1, column=0, pady=5, sticky="e")
entry_profits = tk.Entry(root, width=20)
entry_profits.grid(row=1, column=1, pady=5)

tk.Label(root, text="Weights (space-separated):").grid(row=2, column=0, pady=5, sticky="e")
entry_weights = tk.Entry(root, width=20)
entry_weights.grid(row=2, column=1, pady=5)

tk.Label(root, text="Max Capacity:").grid(row=3, column=0, pady=5, sticky="e")
entry_capacity = tk.Entry(root, width=20)
entry_capacity.grid(row=3, column=1, pady=5)

# Button to calculate profit
calculate_button = tk.Button(root, text="Calculate Profit", command=calculate_profit)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Entry box to display result
tk.Label(root, text="Maximum Profit:").grid(row=5, column=0, pady=5, sticky="e")
entry_result = tk.Entry(root, width=20)
entry_result.grid(row=5, column=1, pady=5)

# Label to display items used
items_used_label = tk.Label(root, text="Items Used:", justify="left")
items_used_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
