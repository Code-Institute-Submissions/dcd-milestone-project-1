import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb+srv://admin:Arnold21!@recipe-book-ky5u3.mongodb.net/recipes-book?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipes.html', categories=mongo.db.categories.find())

@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipes/<recipes_id>')
def edit_recipes(recipes_id):
    the_recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipes.html', recipes=the_recipes, categories=all_categories)

@app.route('/update_recipes/<recipes_id>', methods=["POST"])
def update_recipes(recipes_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipes_id)},
    {
        'name': request.form.get['name'],
        'category': request.form.get['category'],
        'method': request.form.get['method'],
    })
    return redirect(url_for('get_recipes'))

@app.route('/recipes/<recipes_id>')
def view_recipes(recipes_id):
    the_recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    return render_template('recipes.html', recipes=the_recipes)


@app.route('/delete_recipes/<recipes_id>')
def delete_recipes(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_recipes'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())

@app.route('/add-category')
def add_category():
    return render_template('addcategory.html')

@app.route('/add-category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get['category_name']})
    return redirect(url_for('get_categories'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 8080)),
        debug=True)