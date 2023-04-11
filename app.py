import os
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    # search bar
    query = request.form.get("query")
    # recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    recipes = list(mongo.db.recipes.find({"recipe_name": {"$regex": query, "$options": "ig"}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        # checks if email is in use
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("E-mail already in use!")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

    # put new user into session cookies
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # checks if hashed password matches input password
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello, {}. Welcome Back!".format(
                        request.form.get("username")))
                    return redirect(url_for("get_recipes"))
            else:
                # wrong password
                flash("Incorrect Username and/or Password. Please try again.")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # logs user out
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# @app.route("/add_recipe", methods=["GET", "POST"])
# def add_recipe():
#     # adds recipe to database
#     if request.method == "POST":

#         recipes = {
#             "recipe_ingredients": request.form.get("recipe_ingredients"),
#             "recipe_name": request.form.get("recipe_name"),
#             "recipe_description": request.form.get("recipe_description"),
#             "recipe_steps": request.form.get("recipe_steps"),
#             "recipe_allergens": request.form.getlist("recipe_allergens"),
#             "recipe_category": request.form.getlist("recipe_category"),
#             "recipe_image": request.form.get("recipe_image"),
#             "created_by": session["user"]
#         }

#         mongo.db.recipes.insert_one(recipes)
#         flash("Recipe Added")
#         return redirect(url_for("get_recipes"))

#         allergens = mongo.db.allergens.find().sort("recipe_allergens", 1)
#         category = mongo.db.recipe_category.find().sort("recipe_category", 1)
#         return render_template(
#             "add_recipe.html", allergens=allergens,
#             recipe_category=recipe_category)

#     return render_template(
#         "add_recipe.html")

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # adds recipe to database
    if request.method == "POST":

        recipes = {
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_steps": request.form.get("recipe_steps"),
            "recipe_allergens": request.form.getlist("recipe_allergens"),
            "recipe_category": request.form.getlist("recipe_category"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipes)
        flash("Recipe Added")
        return redirect(url_for("get_recipes"))

    allergens = mongo.db.allergens.find().sort("recipe_allergens", 1)
    categories = mongo.db.categories.find().sort("recipe_category", 1)
    return render_template(
        "add_recipe.html", allergens=allergens,
        categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # updates recipe in database
    if request.method == "POST":

        submit = {
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_steps": request.form.get("recipe_steps"),
            "recipe_allergens": request.form.getlist("recipe_allergens"),
            "recipe_category": request.form.getlist("recipe_category"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }

        mongo.db.recipes.replace_one({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    allergens = mongo.db.allergens.find().sort("recipe_allergens", 1)
    categories = mongo.db.categories.find().sort("recipe_category", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe,
        allergens=allergens, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if recipe["created_by"] != session["user"]:
        flash("You are unable to delete this recipe")
        return redirect(url_for("get_recipes"))

    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/show_recipe/<recipe_id>", methods=["GET", "POST"])
def show_recipe(recipe_id):
    # directs user to full recipe page
    if request.method == "POST":
        recipe_method = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_category": request.form.getlist("recipe_category"),
            "recipe_allergens": request.form.getlist("recipe_allergens"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_steps": request.form.get("recipe_steps"),
            "created_by": session["user"]
        }
        mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)}, recipe_method)

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("show_recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
