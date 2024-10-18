from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

teste = [
    {
        "id": 1,
        "title": "Spaghetti Carbonara",
        "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.",
        "price": 12.50,
        "category": "Pasta"
    },
    {
        "id": 2,
        "title": "Chicken Tikka Masala",
        "description": "Marinated chicken cooked in a spiced tomato sauce, served with rice.",
        "price": 15.00,
        "category": "Indian"
    },
    {
        "id": 3,
        "title": "Beef Tacos",
        "description": "Soft or hard shell tacos filled with seasoned ground beef, topped with lettuce, cheese, and salsa.",
        "price": 10.00,
        "category": "Mexican"
    },
    {
        "id": 4,
        "title": "Vegetable Stir-Fry",
        "description": "A quick and healthy mix of fresh vegetables sautéed in soy sauce.",
        "price": 9.00,
        "category": "Vegetarian"
    },
    {
        "id": 5,
        "title": "Margherita Pizza",
        "description": "A simple pizza topped with fresh tomatoes, mozzarella cheese, and basil.",
        "price": 11.00,
        "category": "Pizza"
    },
    {
        "id": 6,
        "title": "Lemon Garlic Salmon",
        "description": "Baked salmon fillet marinated in lemon juice, garlic, and herbs.",
        "price": 18.00,
        "category": "Seafood"
    },
    {
        "id": 7,
        "title": "Caprese Salad",
        "description": "Fresh mozzarella, tomatoes, and basil drizzled with balsamic reduction.",
        "price": 8.00,
        "category": "Salad"
    },
    {
        "id": 8,
        "title": "Vegetarian Chili",
        "description": "A hearty stew made with beans, tomatoes, and a variety of spices.",
        "price": 10.00,
        "category": "Vegetarian"
    },
    {
        "id": 9,
        "title": "Beef Stroganoff",
        "description": "Tender beef strips in a creamy mushroom sauce served over egg noodles.",
        "price": 14.00,
        "category": "Beef"
    },
    {
        "id": 10,
        "title": "Shrimp Scampi",
        "description": "Shrimp sautéed in garlic butter and white wine, served over linguine.",
        "price": 17.00,
        "category": "Seafood"
    },
    {
        "id": 11,
        "title": "Pancakes",
        "description": "Fluffy pancakes served with maple syrup and fresh berries.",
        "price": 7.00,
        "category": "Breakfast"
    },
    {
        "id": 12,
        "title": "Falafel Wrap",
        "description": "Crispy falafel balls wrapped in pita with tahini sauce and fresh veggies.",
        "price": 9.50,
        "category": "Mediterranean"
    },
    {
        "id": 13,
        "title": "BBQ Ribs",
        "description": "Tender pork ribs coated in a smoky barbecue sauce.",
        "price": 20.00,
        "category": "Grill"
    },
    {
        "id": 14,
        "title": "Mushroom Risotto",
        "description": "Creamy Arborio rice cooked with mushrooms and Parmesan cheese.",
        "price": 13.00,
        "category": "Italian"
    },
    {
        "id": 15,
        "title": "Stuffed Bell Peppers",
        "description": "Bell peppers filled with a mixture of rice, meat, and spices, baked until tender.",
        "price": 11.50,
        "category": "Comfort Food"
    },
    {
        "id": 16,
        "title": "Spinach and Feta Quiche",
        "description": "A savory pie filled with spinach, feta cheese, and eggs.",
        "price": 10.00,
        "category": "Breakfast"
    },
    {
        "id": 17,
        "title": "Chili Con Carne",
        "description": "A spicy stew made with ground beef, beans, and chili peppers.",
        "price": 12.00,
        "category": "Mexican"
    },
    {
        "id": 18,
        "title": "Pesto Pasta",
        "description": "Pasta tossed with homemade basil pesto and cherry tomatoes.",
        "price": 9.00,
        "category": "Pasta"
    },
    {
        "id": 19,
        "title": "Apple Crisp",
        "description": "Baked apples topped with a crunchy oat topping, served warm.",
        "price": 6.00,
        "category": "Dessert"
    },
    {
        "id": 20,
        "title": "Chocolate Mousse",
        "description": "A rich and creamy dessert made with chocolate and whipped cream.",
        "price": 7.50,
        "category": "Dessert"
    }
]

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(teste)

if __name__ == '__main__':
    app.run(port=5000)  # Run on port 5000




