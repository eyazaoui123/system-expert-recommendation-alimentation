# 🍽️ Food Recommendation Expert System

A Python-based expert system using **Tkinter** and **Experta** to recommend restaurant dishes based on customer preferences, health conditions, and context (e.g., diet, time of day, budget).

---

## 📌 Features

- **Graphical Interface (Tkinter)**: User-friendly dropdown menus for input selection.
- **Rule-Based Expert System (Experta)**: Matches user inputs to dishes using predefined rules.
- **Personalized Recommendations**: Considers:
  - Diet: Vegan, Vegetarian, Carnivore
  - Health: Hypertension, Diabetes, Low Calorie, Allergies
  - Age: Child, Adult, Senior
  - Meal Type: Starter, Main, Dessert
  - Cuisine: Tunisian, French, Healthy, Vegetarian
  - Context: Time of Day, Occasion, Budget, Organic Preference
- **Dish Details**: Displays recommended dish, description, and image.
- **Error Handling**: Shows messages for missing images or unmatched rules.
- **Reset Option**: Clears inputs to default values.

---
## 📷 Screenshots

Below are screenshots of the Food Recommendation Expert System:

- **Main Input Window**: Select your preferences for diet, health, meal type, and more.

- **Result Window**: View the recommended dish, description, and image (e.g., Yaourt aux Fruits).
  ![Result Window](screenshots/result_window.png)

---

## 🏗️ Project Structure

```
project/
├── main.py                # GUI and system runner
├── Foods.py               # Expert system rules
├── photo/                 # Dish images
│   ├── tunisian/
│   ├── french/
│   ├── healthy/
│   ├── vegetarian/
│   ├── senior/
│   ├── child/
│   ├── default/
├── screenshots/
│   ├── main_window.png
│   ├── result_window.png
├── requirements.txt        # Dependencies
├── README.md              # Documentation
```

---

## 🚀 Installation

1. **Clone the Repository** (replace with your actual repo URL):

   ```
   git clone https://github.com/eya-zaoui/food-expert-system.git
   cd food-expert-system
   ```

2. **Create a Virtual Environment**:

   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Requirements**:

   - Python 3.11.9
   - Libraries: `experta==1.9.4`, `frozendict==1.2`, `pillow`

5. **Set Up Images** (optional):

   - Place `.png` images in the `photo/` subfolders (e.g., `photo/tunisian/couscous.png`).
   - If images are missing, the system displays "Image not found."

---

## ▶️ Usage

1. Run the GUI:

   ```
   python main.py
   ```

2. Select preferences (e.g., diet, health, meal type).

3. Click **Get Recommendation** to see:

   - Recommended dish
   - Description
   - Image (if available)

4. Click **Reset Form** to clear inputs.

---

## 📖 Example

**Input**:

- Carnivore Preference: Carnivore
- Age Group: Child
- Cuisine Type: Tunisian
- Time of Day: Lunch
- Nature of Plate: Main
- Others: No health issues, Low budget

**Output**:

- ✅ Recommended Food: Couscous Tunisien
- 📝 Description: Plat traditionnel tunisien parfait pour les enfants.
- 🖼️ Image: photo/tunisian/couscous.png

---

## 🧠 Rules Overview

The system uses if-then rules to match inputs to dishes. Examples:

- Child + Lunch + Main → Couscous Tunisien
- Hypertension + Lunch + Starter → Salade Mechouia
- Diabetic + Main + Low Calorie → Poulet Grillé aux Herbes
- Vegetarian + Lunch → Salade Méditerranéenne
- Senior + Low Calorie → Soupe de Légumes Maison
- Special Occasion + French + High Budget → Coq au Vin
- Dessert + Sweet + No Diabetes → Baklawa Tunisienne
- Default (no match) → Plat du Jour

See `Foods.py` for all 20+ rules.

---

## ⚡ Future Improvements

- Store rules in JSON or a database.
- Add multi-language support (e.g., English, French).
- Include nutritional information (calories, protein).
- Develop a web version using Flask/Django + React.
- Deploy on tablets for restaurant use.

---

## 📌 Author

👩‍💻 **Eya Zaoui**\
AI & Software Engineer | Passionate about Machine Learning and Expert Systems

---
