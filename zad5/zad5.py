import json
import requests
import unittest


class FreeMeal:
    def search_meal_by_name(self, name):
        if isinstance(name, str):
            data = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={name}")
            if data.json()['meals'] == None:
                raise ValueError("Nie ma posiłku o takiej nazwie")
            else:
                return data.json()['meals'][0]['strMeal']
        else:
            raise ValueError("name musi byc typu string")
    def list_all_meals_by_first_letter(self, l):
        if isinstance(l, str) and len(l) == 1:
            data = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?f={l}")
            result = []
            for i in data.json()['meals']:
                result.append(i['strMeal'])
            return result
        else:
            raise ValueError("Nie string i nie litera")
    def get_meal_by_id(self, id):
        if isinstance(id, int):
            data = requests.get(f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
            if  data.json()['meals'] == None:
                raise ValueError("Nie ma posiłku o takim id")
            else:
                return data.json()['meals'][0]['strMeal']
        else:
            raise ValueError("id musi być typu int")
    def list_all_meal_categories(self):
        data = requests.get(f"https://www.themealdb.com/api/json/v1/1/categories.php")
        result = []
        for i in data.json()['categories']:
            result.append(i['strCategory'])
        return result
    def list_all_categories(self):
        data = requests.get("http://themealdb.com/api/json/v1/1/list.php?c=list")
        result = []
        for i in data.json()['meals']:
            result.append(i['strCategory'])
        return result
    def list_all_area(self):
        data = requests.get(f"http://themealdb.com/api/json/v1/1/list.php?a=list")
        result = []
        for i in data.json()['meals']:
            result.append(i['strArea'])
        return result
    def list_all_ingredients(self):
        data = requests.get("http://themealdb.com/api/json/v1/1/list.php?i=list")
        result = []
        for i in data.json()['meals']:
            result.append(i['strIngredient'])
        return result
    def filter_by_main_ingredient(self, ingredient):
        if isinstance(ingredient, str):
            data = requests.get(f"http://themealdb.com/api/json/v1/1/filter.php?i={ingredient}")
            result = []
            if data.json()['meals'] == None:
                raise ValueError
            for i in data.json()['meals']:
                result.append(i['strMeal'])
            return result
        else:
            raise ValueError

    def get_recipe_by_id(self, id):
        if isinstance(id, int):
            data = requests.get(f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
            if data.json()['meals'] == None:
                raise ValueError("Nie ma posiłku o pdanym id")
            else:
                return data.json()['meals'][0]['strInstructions']
        else:
            raise ValueError("id musi byc typu int")


class TestFreeMeal(unittest.TestCase):
    def setUp(self):
        self.temp = FreeMeal()
    def test_search_meal_by_name(self):
        self.assertEqual("Spicy Arrabiata Penne",self.temp.search_meal_by_name('Arrabiata'))
    def test_search_meal_by_name_int(self):
        self.assertRaises(ValueError, self.temp.search_meal_by_name, 2)

    def test_search_meal_by_name_array(self):
        self.assertRaises(ValueError, self.temp.search_meal_by_name, [])

    def test_search_meal_by_name_object(self):
        self.assertRaises(ValueError, self.temp.search_meal_by_name, {})

    def test_search_meal_by_name_none(self):
        self.assertRaises(ValueError, self.temp.search_meal_by_name, None)

    def test_list_meals_by_first_letter(self):
        self.assertEqual(
            ['Fish pie', 'French Lentils With Garlic and Thyme', 'Fettucine alfredo', 'Full English Breakfast', 'French Onion Soup', 'Flamiche', 'French Omelette', 'Fish Stew with Rouille', 'Fennel Dauphinoise', 'Fruit and Cream Cheese Breakfast Pastries', 'French Onion Chicken with Roasted Carrots & Mashed Potatoes', 'Ful Medames', 'Feteer Meshaltet', 'Fish fofos', 'Fresh sardines'],
            self.temp.list_all_meals_by_first_letter('f'))

    def test_list_meals_by_first_letter_string(self):
        self.assertRaises(ValueError, self.temp.list_all_meals_by_first_letter, 'xddd')

    def test_list_meals_by_first_letter_number(self):
        self.assertRaises(TypeError, self.temp.list_all_meals_by_first_letter, '0')

    def test_list_meals_by_first_letter_empty_string(self):
        self.assertRaises(ValueError, self.temp.list_all_meals_by_first_letter, '')
    def test_list_meals_by_first_letter_int(self):
        self.assertRaises(ValueError, self.temp.list_all_meals_by_first_letter, 21)
    def test_get_meal_by_id(self):
        self.assertEqual('Teriyaki Chicken Casserole', self.temp.get_meal_by_id(52772))

    def test_get_meal_by_id_wrong_id(self):
        self.assertRaises(ValueError, self.temp.get_meal_by_id, 1337)

    def test_get_meal_by_id_arr(self):
        self.assertRaises(ValueError, self.temp.get_meal_by_id, [])

    def test_get_meal_by_id_obj(self):
        self.assertRaises(ValueError, self.temp.get_meal_by_id, {})

    def test_get_meal_by_id_none(self):
        self.assertRaises(ValueError, self.temp.get_meal_by_id, None)
    def test_list_all_meal_categories(self):
        self.assertEqual(['Beef', 'Chicken', 'Dessert', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side', 'Starter',
             'Vegan', 'Vegetarian', 'Breakfast', 'Goat'], self.temp.list_all_meal_categories())

    def test_list_all_categories(self):
        self.assertEqual(
            ['Beef', 'Breakfast', 'Chicken', 'Dessert', 'Goat', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood',
             'Side', 'Starter', 'Vegan', 'Vegetarian']
            , self.temp.list_all_categories())

    def test_list_all_area(self):
        self.assertEqual(
            ['American', 'British', 'Canadian', 'Chinese', 'Croatian', 'Dutch', 'Egyptian', 'French', 'Greek', 'Indian',
             'Irish', 'Italian', 'Jamaican', 'Japanese', 'Kenyan', 'Malaysian', 'Mexican', 'Moroccan', 'Polish',
             'Portuguese', 'Russian', 'Spanish', 'Thai', 'Tunisian', 'Turkish', 'Unknown', 'Vietnamese']
            , self.temp.list_all_area())
    def test_list_all_ingredients(self):
        self.assertEqual(
            ['Chicken', 'Salmon', 'Beef', 'Pork', 'Avocado', 'Apple Cider Vinegar', 'Asparagus', 'Aubergine',
             'Baby Plum Tomatoes', 'Bacon', 'Baking Powder', 'Balsamic Vinegar', 'Basil', 'Basil Leaves',
             'Basmati Rice', 'Bay Leaf', 'Bay Leaves', 'Beef Brisket', 'Beef Fillet', 'Beef Gravy', 'Beef Stock',
             'Bicarbonate Of Soda', 'Biryani Masala', 'Black Pepper', 'Black Treacle', 'Borlotti Beans', 'Bowtie Pasta',
             'Bramley Apples', 'Brandy', 'Bread', 'Breadcrumbs', 'Broccoli', 'Brown Lentils', 'Brown Rice',
             'Brown Sugar', 'Butter', 'Cacao', 'Cajun', 'Canned Tomatoes', 'Cannellini Beans', 'Cardamom', 'Carrots',
             'Cashew Nuts', 'Cashews', 'Caster Sugar', 'Cayenne Pepper', 'Celeriac', 'Celery', 'Celery Salt',
             'Challots', 'Charlotte Potatoes', 'Cheddar Cheese', 'Cheese', 'Cheese Curds', 'Cherry Tomatoes',
             'Chestnut Mushroom', 'Chicken Breast', 'Chicken Breasts', 'Chicken Legs', 'Chicken Stock',
             'Chicken Thighs', 'Chickpeas', 'Chili Powder', 'Chilled Butter', 'Chilli', 'Chilli Powder',
             'Chinese Broccoli', 'Chocolate Chips', 'Chopped Onion', 'Chopped Parsley', 'Chopped Tomatoes', 'Chorizo',
             'Christmas Pudding', 'Cilantro', 'Cinnamon', 'Cinnamon Stick', 'Cloves', 'Coco Sugar', 'Cocoa',
             'Coconut Cream', 'Coconut Milk', 'Colby Jack Cheese', 'Cold Water', 'Condensed Milk', 'Coriander',
             'Coriander Leaves', 'Coriander Seeds', 'Corn Tortillas', 'Cornstarch', 'Cream', 'Creme Fraiche',
             'Cubed Feta Cheese', 'Cucumber', 'Cumin', 'Cumin Seeds', 'Curry Powder', 'Dark Brown Sugar',
             'Dark Soft Brown Sugar', 'Dark Soy Sauce', 'Demerara Sugar', 'Diced Tomatoes', 'Digestive Biscuits',
             'Dill', 'Doner Meat', 'Double Cream', 'Dried Oregano', 'Dry White Wine', 'Egg Plants', 'Egg Rolls',
             'Egg White', 'Egg Yolks', 'Eggs', 'Enchilada Sauce', 'English Mustard', 'Extra Virgin Olive Oil',
             'Fajita Seasoning', 'Farfalle', 'Fennel Bulb', 'Fennel Seeds', 'Fenugreek', 'Feta', 'Fish Sauce',
             'Flaked Almonds', 'Flax Eggs', 'Flour', 'Flour Tortilla', 'Floury Potatoes', 'Free-range Egg, Beaten',
             'Free-range Eggs, Beaten', 'French Lentils', 'Fresh Basil', 'Fresh Thyme', 'Freshly Chopped Parsley',
             'Fries', 'Full Fat Yogurt', 'Garam Masala', 'Garlic', 'Garlic Clove', 'Garlic Powder', 'Garlic Sauce',
             'Ghee', 'Ginger', 'Ginger Cordial', 'Ginger Garlic Paste', 'Ginger Paste', 'Golden Syrup', 'Gouda Cheese',
             'Granulated Sugar', 'Grape Tomatoes', 'Greek Yogurt', 'Green Beans', 'Green Chilli', 'Green Olives',
             'Green Red Lentils', 'Green Salsa', 'Ground Almonds', 'Ground Cumin', 'Ground Ginger', 'Gruyère',
             'Hard Taco Shells', 'Harissa Spice', 'Heavy Cream', 'Honey', 'Horseradish', 'Hot Beef Stock', 'Hotsauce',
             'Ice Cream', 'Italian Fennel Sausages', 'Italian Seasoning', 'Jalapeno', 'Jasmine Rice',
             'Jerusalem Artichokes', 'Kale', 'Khus Khus', 'King Prawns', 'Kosher Salt', 'Lamb', 'Lamb Loin Chops',
             'Lamb Mince', 'Lasagne Sheets', 'Lean Minced Beef', 'Leek', 'Lemon', 'Lemon Juice', 'Lemon Zest', 'Lemons',
             'Lettuce', 'Lime', 'Little Gem Lettuce', 'Macaroni', 'Mackerel', 'Madras Paste', 'Marjoram',
             'Massaman Curry Paste', 'Medjool Dates', 'Meringue Nests', 'Milk', 'Minced Garlic',
             'Miniature Marshmallows', 'Mint', 'Monterey Jack Cheese', 'Mozzarella Balls', 'Muscovado Sugar',
             'Mushrooms', 'Mustard', 'Mustard Powder', 'Mustard Seeds', 'Nutmeg', 'Oil', 'Olive Oil', 'Onion Salt',
             'Onions', 'Orange', 'Orange Zest', 'Oregano', 'Oyster Sauce', 'Paprika', 'Parma Ham', 'Parmesan',
             'Parmesan Cheese', 'Parmigiano-reggiano', 'Parsley', 'Peanut Butter', 'Peanut Oil', 'Peanuts', 'Peas',
             'Pecorino', 'Penne Rigate', 'Pepper', 'Pine Nuts', 'Pitted Black Olives', 'Plain Chocolate', 'Plain Flour',
             'Plum Tomatoes', 'Potato Starch', 'Potatoes', 'Prawns', 'Puff Pastry', 'Raspberry Jam', 'Raw King Prawns',
             'Red Chile Flakes', 'Red Chilli', 'Red Chilli Powder', 'Red Onions', 'Red Pepper', 'Red Pepper Flakes',
             'Red Wine', 'Refried Beans', 'Rice', 'Rice Noodles', 'Rice Stick Noodles', 'Rice Vermicelli', 'Rigatoni',
             'Rocket', 'Rolled Oats', 'Saffron', 'Sage', 'Sake', 'Salsa', 'Salt', 'Salted Butter', 'Sausages',
             'Sea Salt', 'Self-raising Flour', 'Semi-skimmed Milk', 'Sesame Seed', 'Shallots',
             'Shredded Mexican Cheese', 'Shredded Monterey Jack Cheese', 'Small Potatoes', 'Smoked Paprika',
             'Smoky Paprika', 'Sour Cream', 'Soy Sauce', 'Soya Milk', 'Spaghetti', 'Spinach', 'Spring Onions', 'Squash',
             'Stir-fry Vegetables', 'Strawberries', 'Sugar', 'Sultanas', 'Sunflower Oil', 'Tamarind Ball',
             'Tamarind Paste', 'Thai Fish Sauce', 'Thai Green Curry Paste', 'Thai Red Curry Paste', 'Thyme',
             'Tomato Ketchup', 'Tomato Puree', 'Tomatoes', 'Toor Dal', 'Tuna', 'Turmeric', 'Turmeric Powder', 'Turnips',
             'Vanilla', 'Vanilla Extract', 'Veal', 'Vegan Butter', 'Vegetable Oil', 'Vegetable Stock',
             'Vegetable Stock Cube', 'Vinaigrette Dressing', 'Vine Leaves', 'Vinegar', 'Water', 'White Chocolate Chips',
             'White Fish', 'White Fish Fillets', 'White Vinegar', 'White Wine', 'Whole Milk', 'Whole Wheat',
             'Wholegrain Bread', 'Worcestershire Sauce', 'Yogurt', 'Zucchini', 'Pretzels', 'Cream Cheese',
             'Icing Sugar', 'Toffee Popcorn', 'Caramel', 'Caramel Sauce', 'Tagliatelle', 'Fettuccine', 'Clotted Cream',
             'Corn Flour', 'Mussels', 'Fideo', 'Monkfish', 'Vermicelli Pasta', 'Baby Squid', 'Squid', 'Fish Stock',
             'Pilchards', 'Black Olives', 'Onion', 'Tomato', 'Duck', 'Duck Legs', 'Chicken Stock Cube',
             'Pappardelle Pasta', 'Paccheri Pasta', 'Linguine Pasta', 'Sugar Snap Peas', 'Crusty Bread',
             'Fromage Frais', 'Clams', 'Passata', 'Rapeseed Oil', 'Stilton Cheese', 'Lamb Leg', 'Lamb Shoulder',
             'Apricot', 'Butternut Squash', 'Couscous', 'Minced Beef', 'Turkey Mince', 'Barbeque Sauce', 'Sweetcorn',
             'Goose Fat', 'Duck Fat', 'Fennel', 'Red Wine Vinegar', 'Haricot Beans', 'Rosemary', 'Butter Beans',
             'Pinto Beans', 'Tomato Sauce', 'Mascarpone', 'Mozzarella', 'Ricotta', 'Dried Apricots', 'Capers', 'Banana',
             'Raspberries', 'Blueberries', 'Walnuts', 'Pecan Nuts', 'Maple Syrup', 'Light Brown Soft Sugar',
             'Dark Brown Soft Sugar', 'Dark Chocolate Chips', 'Milk Chocolate', 'Dark Chocolate', 'Pumpkin',
             'Shortcrust Pastry', 'Peanut Cookies', 'Gelatine Leafs', 'Peanut Brittle', 'Peaches', 'Yellow Pepper',
             'Green Pepper', 'Courgettes', 'Tinned Tomatos', 'Chestnuts', 'Wild Mushrooms', 'Truffle Oil', 'Paneer',
             'Naan Bread', 'Lentils', 'Roasted Vegetables', 'Kidney Beans', 'Mixed Grain', 'Tahini', 'Tortillas',
             'Udon Noodles', 'Cabbage', 'Shiitake Mushrooms', 'Mirin', 'Sesame Seed Oil', 'Baguette', 'Vine Tomatoes',
             'Suet', 'Swede', 'Ham', 'Oysters', 'Stout', 'Lard', 'Lamb Kidney', 'Beef Kidney', 'Haddock',
             'Smoked Haddock', 'Brussels Sprouts', 'Raisins', 'Currants', 'Custard', 'Mixed Peel', 'Redcurrants',
             'Blackberries', 'Hazlenuts', 'Braeburn Apples', 'Red Food Colouring', 'Pink Food Colouring',
             'Blue Food Colouring', 'Yellow Food Colouring', 'Apricot Jam', 'Marzipan', 'Almonds', 'Black Pudding',
             'Baked Beans', 'White Flour', 'Yeast', 'Fruit Mix', 'Dried Fruit', 'Cherry', 'Glace Cherry', 'Treacle',
             'Oatmeal', 'Oats', 'Egg', 'Beef Shin', 'Bouquet Garni', 'Single Cream', 'Red Wine Jelly', 'Apples',
             'Goats Cheese', 'Prosciutto', 'Unsalted Butter', 'Brie', 'Tarragon Leaves', 'Chives', 'Pears',
             'White Chocolate', 'Star Anise', 'Tiger Prawns', 'Custard Powder', 'Desiccated Coconut', 'Frozen Peas',
             'Minced Pork', 'Creamed Corn', 'Sun-Dried Tomatoes', 'Dijon Mustard', 'Tabasco Sauce', 'Canola Oil', 'Cod',
             'Salt Cod', 'Ackee', 'Jerk', 'Ground Beef', 'Baby Aubergine', 'Paella Rice', 'Scotch Bonnet', 'Oxtail',
             'Broad Beans', 'Red Snapper', 'Malt Vinegar', 'Rice Vinegar', 'Water Chestnut', 'Tofu', 'Doubanjiang',
             'Fermented Black Beans', 'Scallions', 'Sichuan Pepper', 'Wonton Skin', 'Starch', 'Rice wine',
             'Cooking wine', 'Duck Sauce', 'Gochujang', 'Bean Sprouts', 'Noodles', 'Wood Ear Mushrooms', 'Dark Rum',
             'Light Rum', 'Rum', 'English Muffins', 'Muffins', 'White Wine Vinegar', 'Smoked Salmon', 'Mars Bar',
             'Rice Krispies', 'Ancho Chillies', 'Almond Milk', 'Allspice', 'Almond Extract', 'Tripe', 'Goat Meat',
             'Black Beans', 'Anchovy Fillet', 'Ras el hanout', 'Filo Pastry', 'Orange Blossom Water', 'Candied Peel',
             'Grand Marnier', 'Sherry', 'Rose water', 'Mixed Spice', 'Mincemeat', 'Sweet Potatoes', 'Bread Rolls',
             'Bun', 'Potatoe Buns', 'Ground Pork', 'Pork Chops', 'Yukon Gold Potatoes', 'Yellow Onion',
             'Beef Stock Concentrate', 'Chicken Stock Concentrate', 'Persian Cucumber', 'Mayonnaise', 'Sriracha',
             'Rhubarb', 'Pita Bread', 'Bulgur Wheat', 'Quinoa', 'Dill Pickles', 'Sesame Seed Burger Buns', 'Buns',
             'Iceberg Lettuce', 'Gherkin Relish', 'Cheese Slices', 'Shortening', 'Warm Water', 'Boiling Water',
             'Pickle Juice', 'Powdered Sugar', 'Kielbasa', 'Polish Sausage', 'Sauerkraut', 'Caraway Seed', 'Herring',
             'Jam', 'Mulukhiyah', 'Sushi Rice', 'Figs', 'Cider', 'Beetroot', 'Sardines', 'Ciabatta', 'Buckwheat']
            , self.temp.list_all_ingredients())
    def test_filter_by_main_ingredient(self):
        self.assertEqual(['Keleya Zaara', 'Lancashire hotpot', 'Stuffed Lamb Tomatoes'], self.temp.filter_by_main_ingredient('Lamb'))

    def test_filter_by_main_ingredient_wrong_ingredient(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, 'sand')

    def test_filter_by_main_ingredient_array(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, [])


    def test_filter_by_main_ingredient_object(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, {})


    def test_filter_by_main_ingredient_none(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, None)


    def test_filter_by_main_ingredient_true(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, True)


    def test_filter_by_main_ingredient_False(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, False)


    def test_filter_by_main_ingredient_int(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, 23)


    def test_filter_by_main_ingredient_float(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, 2.1233)


    def test_filter_by_main_ingredient_negative_int(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, -21)


    def test_filter_by_main_ingredient_negative_float(self):
        self.assertRaises(ValueError, self.temp.filter_by_main_ingredient, -2.451)
    def test_get_recipe_by_id(self):
        self.assertEqual("Preheat oven to 350\u00b0 F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, \u00bd cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!", self.temp.get_recipe_by_id(52772))

if __name__ == '__main__':
    unittest.main()