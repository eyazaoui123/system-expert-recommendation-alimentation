from experta import Rule, Fact, KnowledgeEngine, AND, OR, NOT

class Foods(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.food = "No recommendation found"
        self.description = "no description available"
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\default\plat_du_jour.jpg"
    
    # Règle 1: Enfant + Déjeuner
    @Rule(AND(
        Fact(carnivore='2'), 
        Fact(tension='0'),
        Fact(diabete='0'),
        Fact(calorie='0'),
        Fact(allergie='0'),
        Fact(qte='0'),
        Fact(age='0'),
        Fact(cuisine='0'),
        Fact(salsuc='0'),
        Fact(natureplat='1'),
        Fact(moment='1'),
        Fact(occasion='0'),
        Fact(budget='0'),
        Fact(naturerepas='0')
    ))
    def reg1(self):
        self.food = "Tunisian couscous"
        self.description = "Traditional Tunisian dish. Rich in nutrients and easy to digest."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\tunisian\couscous.jpg"
        print("Rule 1 triggered")
    
    # Règle 2: Tension + Déjeuner
    @Rule(AND(
        Fact(carnivore='2'), 
        Fact(tension='1'),
        Fact(diabete='0'),
        Fact(calorie='0'),
        Fact(allergie='0'),
        Fact(qte='0'),
        Fact(age='1'),
        Fact(cuisine='0'),
        Fact(salsuc='0'),
        Fact(natureplat='0'),
        Fact(moment='1'),
        Fact(occasion='0'),
        Fact(budget='0'),
        Fact(naturerepas='0')
    ))
    def reg2(self): 
        self.food = "Tunisian salad Mechouia"
        self.description = "Traditional Tunisian salad, low in salt, perfect for tension problems."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\tunisian\salade_mechouia.jpg"
        print("Rule 2 triggered")
        
    # Rule 10: Diabetic + Low Calorie + Main + Healthy + No Hypertension
    @Rule(AND(
        Fact(diabete='1'),
        Fact(calorie='1'),
        Fact(natureplat='1'),
        Fact(cuisine='2'),
        Fact(tension='0')
    ))
    def reg10(self):
        self.food = "Grilled Fish with Vegetables"
        self.description = "Grilled fish with fresh vegetables, low in calories and carbohydrates for diabetics."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\healthy\poisson_grille.jpg"
        print("Rule 10 triggered")

    # Rule 3: Diabetic + Main + Low Calorie + French or Vegetarian (not Tunisian or Healthy)
    @Rule(AND(
        Fact(diabete='1'),
        Fact(natureplat='1'),
        Fact(calorie='1'),
        NOT(Fact(cuisine='2'))   # Not Healthy (to avoid Rule 10)
    ))
    def reg3(self):
        self.food = "Grilled Chicken with Herbs"
        self.description = "Low carbohydrate protein dish, ideal for diabetic people."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\healthy\poulet_grille.jpg"
        print("Rule 3 triggered")
    
    # Règle 4: Végétarien + Déjeuner
    @Rule(AND(
        Fact(carnivore='1'),
        Fact(moment='1'),
        Fact(age='0'),
        Fact(calorie='0')
    ))
    def reg4(self):
        self.food = "Mediterranean Full Salad"
        self.description = "Balanced salad with fresh vegetables, cheese and nuts, perfect for lunch."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\vegetarian\salade_mediterraneenne.jpg"
        print("Rule 4 triggered")
    
    # Règle 5: Personne âgée + Faible en calories
    @Rule(AND(
        Fact(age='2'),
        Fact(calorie='1'),
        Fact(tension='0'),
        Fact(diabete='0')
    ))
    def reg5(self):
        self.food = "Homemade Vegetable Soup"
        self.description = "Light and nutritious soup, easy to digest for the elderly."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\senior\soupe_legumes.jpg"
        print("Rule 5 triggered")
    
    # Règle 6: Occasion spéciale + Cuisine française
    @Rule(AND(
        Fact(occasion='1'),
        Fact(cuisine='1'),
        Fact(budget='2'),
        Fact(salsuc='0')
    ))
    

        
    def reg6(self):
        self.food = "Coq with wine"
        self.description = "Refined traditional French dish, perfect for special occasions."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\french\coq_au_vin.jpg"
        print("Rule 6 triggered")
    
    # Règle 7: Budget économique + Repas rapide
    @Rule(AND(
        Fact(budget='0'),
        Fact(naturerepas='1'),
        Fact(moment='1')
    ))
    def reg7(self):
        self.food = "Tunisian Tuna sandwich"
        self.description = "Quick, economical and tasty meal, typical of Tunisian cuisine."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\tunisian\sandwich_thon.png"
        print("Rule 7 triggered")
    
    # Règle 8: Dessert + Sucré
    @Rule(AND(
        Fact(natureplat='2'),
        Fact(salsuc='1'),
        Fact(diabete='0'),
        Fact(age='1')
    ))
    def reg8(self):
        self.food = "Tunisian Baklawa"
        self.description = "Sweet oriental dessert with almonds and honey, delicious and authentic."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\tunisian\baklawa.jpg"
        print("Rule 8 triggered")
    
    # Règle 9: Vegan + Breakfast + Starter
    @Rule(AND(
        Fact(carnivore='0'),
        Fact(moment='0'),
        Fact(natureplat='0'),
        Fact(calorie='0'),
        Fact(allergie='0'),
        Fact(cuisine='3')
    ))
    def reg9(self):
        self.food = "Avocado Toast"
        self.description = "Fresh avocado toast, vegan and energizing for breakfast."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\vegetarian\avocado_toast.jpg"
        print("Rule 9 triggered")
    
    
    # Rule 11: Allergic + Vegetarian + Lunch + Medium Budget + Main + Not Child
    @Rule(AND(
        Fact(allergie='1'),
        Fact(carnivore='1'),
        Fact(moment='1'),
        Fact(budget='1'),
        Fact(natureplat='1'),
        NOT(Fact(age='0'))
    ))
    def reg11(self):
        self.food = "Quinoa Salad"
        self.description = "Quinoa salad with vegetables, without common allergens, vegetarian and healthy."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\vegetarian\quinoa_salad.jpg"
        print("Rule 11 triggered")
    
    # Règle 12: Senior + Dinner + Low Salt + No Diabetes
    @Rule(AND(
        Fact(age='2'),
        Fact(moment='2'),
        Fact(tension='1'),
        Fact(diabete='0'),
        Fact(natureplat='1')
    ))
    def reg12(self):
        self.food = "Steamed Vegetables with Whitefish"
        self.description = "Steamed vegetables and white fish, low in salt for seniors with hypertension."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\senior\legumes_poisson.jpg"
        print("Rule 12 triggered")
    
    # Règle 13: Child + Sweet Dessert + No Health Issues
    @Rule(AND(
        Fact(age='0'),
        Fact(natureplat='2'),
        Fact(salsuc='1'),
        Fact(diabete='0'),
        Fact(allergie='0')
    ))
    def reg13(self):
        self.food = "Fruit Yogurt"
        self.description = "Natural yoghurt with fresh fruit, sweet and fun for children."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\child\yaourt_fruits.jpg"
        print("Rule 13 triggered")
    
    # Règle 14: Special Occasion + High Budget + French Dessert
    @Rule(AND(
        Fact(occasion='1'),
        Fact(budget='2'),
        Fact(cuisine='1'),
        Fact(natureplat='2'),
        Fact(salsuc='1'),
        Fact(diabete='0'),
        Fact(age='2')
    ))
    def reg14(self):
        self.food = "Crème Brûlée"
        self.description = "Classic French dessert, creamy and caramelized, for special occasions."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\french\creme_brulee.jpg"
        print("Rule 14 triggered")
    
    # Règle 15: Vegan + Organic + Main + Dinner
    @Rule(AND(
        Fact(carnivore='0'),
        Fact(naturerepas='1'),
        Fact(natureplat='1'),
        Fact(moment='2'),
        Fact(calorie='0'),
        Fact(salsuc='0')
    ))
    def reg15(self):
        self.food = "Stir-Fry of Organic Vegetables"
        self.description = "Vegan, nutritious stir-fried organic vegetables for dinner."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\vegetarian\stir_fry.jpg"
        print("Rule 15 triggered")
    
    # Règle 16: Carnivore + Tunisian + Starter + Breakfast
    @Rule(AND(
        Fact(carnivore='2'),
        Fact(cuisine='0'),
        Fact(natureplat='0'),
        Fact(moment='0'),
        Fact(occasion='0')
    ))
    def reg16(self):
        self.food = "Tunisian Ojja"
        self.description = "Eggs with tomatoes and peppers, Tunisian starter for carnivorous breakfast."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\tunisian\ojja.jpg"
        print("Rule 16 triggered")
    
    # Règle 17: Low Calorie + Healthy + Large Quantity + Adult
    @Rule(AND(
        Fact(calorie='1'),
        Fact(cuisine='2'),
        Fact(qte='2'),
        Fact(age='1'),
        Fact(natureplat='1')
    ))
    def reg17(self):
        self.food = "Grilled Chicken Salad"
        self.description = "Large portion of salad with grilled chicken, low calorie for adults."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\healthy\salade_poulet.jpg"
        print("Rule 17 triggered")
    
    # Règle 18: Diabetes + Tension + Vegetarian + Starter
    @Rule(AND(
        Fact(diabete='1'),
        Fact(tension='1'),
        Fact(carnivore='1'),
        Fact(natureplat='0'),
        Fact(allergie='0')
    ))
    def reg18(self):
        self.food = "Fresh Tomato Soup"
        self.description = "Soup low in salt and sugar, vegetarian for starter with diabetes and tension."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\vegetarian\soupe_tomates.jpg"
        print("Rule 18 triggered")
    
    # Règle 19: Special + High Budget + Carnivore + Main + French
    @Rule(AND(
        Fact(occasion='1'),
        Fact(budget='1'),
        Fact(carnivore='2'),
        Fact(natureplat='1'),
        Fact(cuisine='1')
    ))
    def reg19(self):
        self.food = "Boeuf Bourguignon"
        self.description = "French dish rich in flavors, for special occasions with a high budget."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\french\boeuf_bourguignon.png"
        print("Rule 19 triggered")
    
    # Règle 20: Allergic + Child + Small Quantity + Breakfast
    @Rule(AND(
        Fact(allergie='1'),
        Fact(age='0'),
        Fact(qte='0'),
        Fact(moment='0'),
        Fact(natureplat='0')
    ))
    def reg20(self):
        self.food = "Fruit Smoothie"
        self.description = "Simple fruit smoothie, without common allergens, small portion for children."
        self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\child\smoothie.jpg"
        print("Rule 20 triggered")
    
    # Default rule: Only trigger if no other rule has set food
    @Rule(Fact())
    def default_rule(self):
        if self.food == "No recommendation found":
            self.food = "Dish of the Day"
            self.description = "Our special suggestion from the chef, tailored to your general preferences."
            self.photo = r"C:\Users\MEGA PC\Desktop\food-recommendation-system\photo\default\plat_du_jour.jpg"
            print("Default rule triggered")