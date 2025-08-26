import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import Foods as rules
from experta import Fact
import tkinter.font as tkFont
import os

# Create the main window
root = tk.Tk()
root.title("Food Recommendation Expert System")

# Center the main window
window_width = 650
window_height = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#f5f6f5")  # Soft white background

# Define fonts
title_font = tkFont.Font(family="Segoe UI", size=18, weight="bold")
label_font = tkFont.Font(family="Segoe UI", size=12)
button_font = tkFont.Font(family="Segoe UI", size=11, weight="bold")

# Configure ttk styles
style = ttk.Style()
style.theme_use("clam")  # Modern theme
style.configure("TButton", font=button_font, padding=10, background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])
style.configure("TLabel", font=label_font, background="#f5f6f5")
style.configure("TCombobox", font=label_font, padding=5)

# Title label
title_label = tk.Label(root, text="Food Recommendation in restaurants", font=title_font, bg="#f5f6f5", fg="#333")
title_label.pack(pady=20)

# Scrollable input frame
canvas = tk.Canvas(root, bg="#f5f6f5", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
input_frame = tk.Frame(canvas, bg="#f5f6f5")
input_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=input_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
scrollbar.pack(side="right", fill="y")

# Input variables
carnivore = tk.StringVar(value='2')
tension = tk.StringVar(value='0')
diabete = tk.StringVar(value='0')
calorie = tk.StringVar(value='0')
allergie = tk.StringVar(value='0')
qte = tk.StringVar(value='0')
age = tk.StringVar(value='0')
salsuc = tk.StringVar(value='0')
natureplat = tk.StringVar(value='1')  # Set to '1' for Rule 1 (Main)
cuisine = tk.StringVar(value='0')
moment = tk.StringVar(value='1')
occasion = tk.StringVar(value='0')
budget = tk.StringVar(value='0')
naturerepas = tk.StringVar(value='0')

# Input options
carnivore_options = ['0 - Vegan', '1 - Vegetarian', '2 - Carnivore']
health_options = ['0 - No', '1 - Yes']
qte_options = ['0 - Small', '1 - Medium', '2 - Large']
age_options = ['0 - Child', '1 - Adult', '2 - Senior']
salsuc_options = ['0 - Salty', '1 - Sweet']
natureplat_options = ['0 - Starter', '1 - Main', '2 - Dessert']
cuisine_options = ['0 - Tunisian', '1 - French', '2 - Healthy', '3 - Vegetarian']
moment_options = ['0 - Breakfast', '1 - Lunch', '2 - Dinner']
occasion_options = ['0 - Everyday', '1 - Special']
budget_options = ['0 - Low', '1 - Medium', '2 - High']
naturerepas_options = ['0 - Normal', '1 - Organic/Natural']

# Create input fields using ttk.Combobox
inputs = [
    ("Carnivore Preference:", carnivore, carnivore_options),
    ("Hypertension (Tension):", tension, health_options),
    ("Diabetes:", diabete, health_options),
    ("Low Calorie Diet:", calorie, health_options),
    ("Allergies:", allergie, health_options),
    ("Quantity:", qte, qte_options),
    ("Age :", age, age_options),
    ("Salty/Sweet Preference:", salsuc, salsuc_options),
    ("Nature of Plate:", natureplat, natureplat_options),
    ("Kitchen :", cuisine, cuisine_options),
    ("Time of Day:", moment, moment_options),
    ("Occasion:", occasion, occasion_options),
    ("Budget:", budget, budget_options),
    ("Natural/Organic Meal:", naturerepas, naturerepas_options)
]

for i, (label_text, var, options) in enumerate(inputs):
    ttk.Label(input_frame, text=label_text).grid(row=i, column=0, sticky='w', padx=10, pady=5)
    ttk.Combobox(input_frame, textvariable=var, values=options, state="readonly").grid(row=i, column=1, sticky='w', padx=10, pady=5)

# Function to run the expert system and show results in a new window
def Foodrecommandation():
    try:
        # Show loading indicator
        loading_label = tk.Label(root, text="Processing...", font=label_font, bg="#f5f6f5", fg="#666")
        loading_label.pack(pady=10)
        root.update()
        
        expertSystem = rules.Foods()
        expertSystem.reset()
        
        # Extract input values and print for debugging
        inputs = {
            'carnivore': carnivore.get()[0],
            'tension': tension.get()[0],
            'diabete': diabete.get()[0],
            'calorie': calorie.get()[0],
            'allergie': allergie.get()[0],
            'qte': qte.get()[0],
            'age': age.get()[0],
            'salsuc': salsuc.get()[0],
            'natureplat': natureplat.get()[0],
            'cuisine': cuisine.get()[0],
            'moment': moment.get()[0],
            'occasion': occasion.get()[0],
            'budget': budget.get()[0],
            'naturerepas': naturerepas.get()[0]
        }
        print("Inputs:", inputs)
        
        # Declare facts
        for key, value in inputs.items():
            expertSystem.declare(Fact(**{key: value}))
        
        # Run the expert system
        expertSystem.run()
        
        # Debug: Print recommendation
        print(f"Recommendation: {expertSystem.food}, Description: {expertSystem.description}, Photo: {expertSystem.photo}")
        
        # Create new window for results
        result_window = tk.Toplevel(root)
        result_window.title("Your Food Recommendation")
        
        # Center the result window
        result_width = 600
        result_height = 600
        result_x = (screen_width - result_width) // 2
        result_y = (screen_height - result_height) // 2
        result_window.geometry(f"{result_width}x{result_height}+{result_x}+{result_y}")
        result_window.configure(bg="#e8ecef")  # Soft gray background
        
        # Header
        header_frame = tk.Frame(result_window, bg="#4CAF50")
        header_frame.pack(fill='x')
        tk.Label(header_frame, text="Your Recommendation", font=title_font, bg="#4CAF50", fg="white").pack(pady=10)
        
        # Result card
        card_frame = tk.Frame(result_window, bg="white", bd=2, relief="solid")
        card_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Update labels in card
        food_label = tk.Label(card_frame, text=f"Recommended Food: {expertSystem.food}", font=title_font, bg="white", fg="#333")
        food_label.pack(pady=10)
        
        desc_label = tk.Label(card_frame, text=f"Description: {expertSystem.description}", font=label_font, bg="white", fg="#555", wraplength=600)
        desc_label.pack(pady=10)
        
        image_label = tk.Label(card_frame, bg="white", borderwidth=2, relief="solid")
        image_label.pack(pady=10)
        
        # Load and display image
        if expertSystem.photo:
            try:
                # Debug: Check if file exists
                if not os.path.exists(expertSystem.photo):
                    raise FileNotFoundError(f"Image file not found at: {expertSystem.photo}")
                
                img = Image.open(expertSystem.photo)
                img = img.resize((300, 300), Image.LANCZOS)
                photo_img = ImageTk.PhotoImage(img)
                image_label.config(image=photo_img, text="")
                image_label.image = photo_img  # Keep reference
                image_label.update()
                result_window.update()
                print(f"Image loaded successfully: {expertSystem.photo}")
            except Exception as e:
                image_label.config(image='', text=f"Image Error: {str(e)}")
                print(f"Image error: {str(e)}")
        
        # Close button
        close_button = ttk.Button(card_frame, text="Close", command=result_window.destroy)
        close_button.pack(pady=10)
        
        # Remove loading indicator
        loading_label.destroy()
        
    except Exception as e:
        loading_label.destroy()
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        
        # Center the error window
        error_width = 400
        error_height = 200
        error_x = (screen_width - error_width) // 2
        error_y = (screen_height - error_height) // 2
        error_window.geometry(f"{error_width}x{error_height}+{error_x}+{error_y}")
        error_window.configure(bg="#e8ecef")
        
        tk.Label(error_window, text="Error: Could not generate recommendation", font=label_font, bg="#e8ecef", fg="#333").pack(pady=10)
        tk.Label(error_window, text=f"Error: {str(e)}", font=label_font, bg="#e8ecef", fg="#555", wraplength=350).pack(pady=10)
        ttk.Button(error_window, text="Close", command=error_window.destroy).pack(pady=10)
        print(f"Error in Foodrecommandation: {e}")

# Reset form function
def reset_form():
    carnivore.set('2')
    tension.set('0')
    diabete.set('0')
    calorie.set('0')
    allergie.set('0')
    qte.set('0')
    age.set('0')
    salsuc.set('0')
    natureplat.set('1')  # Set to '1' for Rule 1
    cuisine.set('0')
    moment.set('1')
    occasion.set('0')
    budget.set('0')
    naturerepas.set('0')
    print("Form reset")

# Button frame
button_frame = tk.Frame(root, bg="#f5f6f5")
button_frame.pack(pady=20)

# Get Recommendation button
# Parameters you can change
BUTTON_X = 400
BUTTON_Y = 300
BUTTON_SPACING = 50

# Place buttons manually
recommend_button = ttk.Button(root, text="Get Recommendation", command=Foodrecommandation)
recommend_button.place(x=BUTTON_X, y=BUTTON_Y)

reset_button = ttk.Button(root, text="Reset Form", command=reset_form)
reset_button.place(x=BUTTON_X + 20, y=BUTTON_Y + BUTTON_SPACING)


root.mainloop()