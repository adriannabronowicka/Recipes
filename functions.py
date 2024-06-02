import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk


class Recipe:
    def __init__(self, name, ingredients: list, instruction: str):
        self.name = name
        self.ingredients = ingredients
        self.instruction = instruction

    def add_recipe_to_database(self):
        con = sqlite3.connect('recipes_database.db')
        cur = con.cursor()
        ingredients_str = ", ".join(self.ingredients)
        cur.execute("INSERT INTO Recipes(recipes_name, ingredients, instruction) VALUES(?, ?, ?);",
                    (self.name, ingredients_str, self.instruction))
        con.commit()
        con.close()


def delete_recipe_from_database(deleted_recipe):
    if not deleted_recipe.strip():
        messagebox.showerror("Error", "Please enter the name of recipe to delete.")
        return
    con = sqlite3.connect('recipes_database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM Recipes WHERE LOWER(recipes_name) = LOWER(?)", (deleted_recipe,))
    con.commit()
    if cur.rowcount == 0:
        messagebox.showerror("Error", f"The recipe '{deleted_recipe}' doesn't exist.")
    else:
        messagebox.showinfo("Information", f"The recipe '{deleted_recipe}' has been deleted successfully.")

    con.close()


def see_the_recipe(searched_recipe, recipe_label):
    if not searched_recipe.strip():
        messagebox.showerror("Error", "Please enter the name of recipe to delete.")
        return
    con = sqlite3.connect('recipes_database.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM Recipes WHERE LOWER(recipes_name) = LOWER(?)", (searched_recipe,))
        result = cur.fetchall()
        if result:
            recipe_info = ""
            for row in result:
                recipe_info += f"Recipes name: {row[1]}\n"
                recipe_info += f"Ingredients: {row[2]}\n"
                recipe_info += f"Instruction: {row[3]}\n"
                recipe_label.config(text=recipe_info)
        else:
            raise Exception(f"The recipe '{searched_recipe}' doesn't exist.")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")
    finally:
        con.close()


def see_all_recipes():
    con = sqlite3.connect('recipes_database.db')
    cur = con.cursor()
    cur.execute("SELECT recipes_name FROM Recipes ")
    result = cur.fetchall()
    recipes_text = "\n".join(", ".join(row) for row in result)
    con.close()
    return recipes_text


def resize_image(image):
    original_image = Image.open(image)
    resized_image = original_image.resize((600, 600))
    new_image = ImageTk.PhotoImage(resized_image)
    return new_image




