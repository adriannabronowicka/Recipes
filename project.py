from functions import *
import tkinter as tk
from tkinter import scrolledtext

list_of_ingredients = []
ingredients = []


# Function for home page
def show_home_page():
    page_1_frame.pack_forget()
    page_2_frame.pack_forget()
    page_3_frame.pack_forget()
    page_4_frame.pack_forget()
    home_page_frame.pack(fill=tk.BOTH, expand=True)


# Function for page of recipes list
def see_all_recipes_page():
    home_page_frame.pack_forget()
    page_1_frame.pack(fill=tk.BOTH, expand=True)
    scroll_text_all_recipes.config(state="normal")
    scroll_text_all_recipes.delete("1.0", tk.END)
    recipes_text = see_all_recipes()
    scroll_text_all_recipes.insert(tk.END, recipes_text)
    scroll_text_all_recipes.config(state="disabled")


# Functions for page of searched recipe
def see_the_recipe_page():
    searched_recipe_entry.delete(0, tk.END)
    recipe_label.config(text="")
    home_page_frame.pack_forget()
    page_2_frame.pack(fill=tk.BOTH, expand=True)


def search_recipe():
    searched_recipe = searched_recipe_entry.get().strip()
    see_the_recipe(searched_recipe, recipe_label)


# Functions for page for adding the recipe
def add_the_recipe_page():
    global ingredients
    ingredients.clear()
    recipe_name_entry.delete(0, tk.END)
    instruction_entry.delete("1.0", tk.END)
    home_page_frame.pack_forget()
    page_3_frame.pack(fill=tk.BOTH, expand=True)


def add_ingredient():
    ingredient = ingredient_entry.get().strip()
    list_of_ingredients.append(ingredient)
    ingredient_entry.delete(0, tk.END)


def finish_input():
    global ingredients
    formatted_list_of_ingredients = " , ".join(list_of_ingredients)
    messagebox.showinfo('Information', f'The ingredients have been saved. List of ingredients:\n'
                                       f' {formatted_list_of_ingredients}')
    copy_list_of_ingredients = list_of_ingredients.copy()
    list_of_ingredients.clear()
    ingredients = copy_list_of_ingredients


def save_the_recipe():
    global ingredients
    name = recipe_name_entry.get().strip()
    instruction = instruction_entry.get("1.0", tk.END).strip()
    if not name or not instruction:
        messagebox.showerror('Error', 'All fields must be filled out.')
        return
    if not ingredients:
        messagebox.showerror('Error', 'If you have added the ingredients, you must save them.')
        return
    recipe = Recipe(name, ingredients, instruction)
    recipe.add_recipe_to_database()
    messagebox.showinfo('Information', 'The recipe has been saved to the database.')
    recipe_name_entry.delete(0, tk.END)
    instruction_entry.delete("1.0", tk.END)
    ingredients.clear()


# Function for recipe deletion page
def delete_the_recipe_page():
    deleted_recipe_entry.delete(0, tk.END)
    home_page_frame.pack_forget()
    page_4_frame.pack(fill=tk.BOTH, expand=True)


def delete_recipe():
    deleted_recipe = deleted_recipe_entry.get().strip()
    delete_recipe_from_database(deleted_recipe)


root = tk.Tk()
root.title('Recipes')
window_width = 600
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)
root.iconbitmap('./cookbook.ico')

background_image_hp = resize_image("background_hp.png")
background_image_p1 = resize_image("background_p1.png")
background_image_p2 = resize_image("background_p2.png")
background_image_p3 = resize_image("background_p3.png")
background_image_p4 = resize_image("background_p4.png")

# Home page
home_page_frame = tk.Frame(root, width=600, height=600)
home_page_frame.pack(fill=tk.BOTH, expand=True)
background_label = tk.Label(home_page_frame, image=background_image_hp)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

welcome = tk.Label(home_page_frame, text='Welcome to the recipe app\nWhat do you want to do?', font=('Arial', 16),
                   foreground='orange', bg='beige')
welcome.pack(pady=20)

button_see_all_recipes = tk.Button(home_page_frame, text='See the list of all recipes', font=('Arial', 12),
                                   bg='beige', command=see_all_recipes_page)
button_see_all_recipes.pack(ipadx=5, ipady=10, pady=10)
button_see_the_recipe = tk.Button(home_page_frame, text='See the recipe', font=('Arial', 12), bg='beige',
                                  command=see_the_recipe_page)
button_see_the_recipe.pack(ipadx=5, ipady=10, pady=10)
button_add_the_recipe = tk.Button(home_page_frame, text='Add the recipe', font=('Arial', 12), bg='beige',
                                  command=add_the_recipe_page)
button_add_the_recipe.pack(ipadx=5, ipady=10, pady=10)
button_delete_the_recipe = tk.Button(home_page_frame, text='Delete the recipe', font=('Arial', 12), bg='beige',
                                     command=delete_the_recipe_page)
button_delete_the_recipe.pack(ipadx=5, ipady=10, pady=10)
button_exit = tk.Button(home_page_frame, text='Exit', font=('Arial', 10), bg='orange', command=home_page_frame.quit)
button_exit.pack(pady=20)

# Page of recipes list
page_1_frame = tk.Frame(root, width=600, height=600)
background_label = tk.Label(page_1_frame, image=background_image_p1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_list_of_recipes = tk.Label(page_1_frame, text='List of recipes', font=('Arial', 14), foreground='orange',
                                 bg='beige')
label_list_of_recipes.pack(pady=(100, 0))
scroll_text_all_recipes = scrolledtext.ScrolledText(page_1_frame, wrap=tk.WORD, width=30, height=20,
                                                    font=('Arial', 12), state="disabled", bg='beige')
scroll_text_all_recipes.pack(pady=(10, 0))

button_go_back = tk.Button(page_1_frame, text='Go to home page', font=('Arial', 10), bg='orange',
                           command=show_home_page)
button_go_back.pack(pady=10)

# Page of searched recipe
page_2_frame = tk.Frame(root, width=600, height=600)
background_label = tk.Label(page_2_frame, image=background_image_p2)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_searched_recipe = tk.Label(page_2_frame, text='Enter the name of the recipe you want to see',
                                 font=('Arial', 14), foreground='orange', bg='beige')
label_searched_recipe.pack(pady=(10, 0))
searched_recipe_entry = tk.Entry(page_2_frame, font=("Arial", 12), bg='beige')
searched_recipe_entry.pack(pady=(10, 0))

button_search_recipe = tk.Button(page_2_frame, text='Search recipe', font=('Arial', 10), bg='orange',
                                 command=search_recipe)
button_search_recipe.pack(pady=(10, 0))
searched_recipe_entry.bind("<Return>", lambda event: button_search_recipe.invoke())

recipe_label = tk.Label(page_2_frame, text="", font=("Arial", 12), wraplength=400, bg='beige')
recipe_label.pack(pady=(10,0))

button_go_back = tk.Button(page_2_frame, text='Go to home page', font=('Arial', 10), bg='orange',
                           command=show_home_page)
button_go_back.pack(pady=10)

# Page for adding the recipe
page_3_frame = tk.Frame(root, width=600, height=600)
background_label = tk.Label(page_3_frame, image=background_image_p3)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_recipe_name = tk.Label(page_3_frame, text='Enter the name of recipe', font=('Arial', 12),
                             foreground='orange', bg='beige')
label_recipe_name.pack(pady=(10, 0))
recipe_name_entry = tk.Entry(page_3_frame, font=("Arial", 12), bg='beige')
recipe_name_entry.pack(pady=(10, 0))

label_ingredient = tk.Label(page_3_frame, text='Enter the ingredient', font=('Arial', 12),
                            foreground='orange', bg='beige')
label_ingredient.pack(pady=(10, 0))
ingredient_entry = tk.Entry(page_3_frame, font=("Arial", 12), bg='beige')
ingredient_entry.pack(pady=(10, 0))
button_add_ingredient_to_list = tk.Button(page_3_frame, text='Add ingredient', font=('Arial', 8),
                                          bg='yellow', command=add_ingredient)
button_add_ingredient_to_list.pack(pady=(10, 0))
button_save_the_ingredients = tk.Button(page_3_frame, text='Save ingredients', font=('Arial', 8),
                                        bg='yellow', command=finish_input)
button_save_the_ingredients.pack(pady=(5, 0))

label_instruction = tk.Label(page_3_frame, text='Describe the recipe', font=('Arial', 12),
                             foreground='orange', bg='beige')
label_instruction.pack(pady=(10, 0))
instruction_entry = tk.Text(page_3_frame, font=("Arial", 12), height=4, width=30, bg='beige')
instruction_entry.pack(ipadx=20, ipady=50, pady=(10, 0))
button_save_recipe = tk.Button(page_3_frame, text='Save the recipe', font=('Arial', 10), bg='orange',
                               command=save_the_recipe)
button_save_recipe.pack(pady=(10, 0))

button_go_back = tk.Button(page_3_frame, text='Go to home page', font=('Arial', 10), bg='orange',
                           command=show_home_page)
button_go_back.pack(pady=10)

# Recipe deletion page
page_4_frame = tk.Frame(root, width=600, height=600)
background_label = tk.Label(page_4_frame, image=background_image_p4)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_deleted_recipe = tk.Label(page_4_frame, text='Enter the name of the recipe you want to delete',
                                font=('Arial', 14), foreground='orange', bg='beige')
label_deleted_recipe.pack(pady=(10, 0))
deleted_recipe_entry = tk.Entry(page_4_frame, font=("Arial", 12), bg='beige')
deleted_recipe_entry.pack(pady=(10, 0))
button_delete_recipe = tk.Button(page_4_frame, text='Delete recipe', font=('Arial', 10), bg='orange',
                                 command=delete_recipe)
button_delete_recipe.pack(pady=(10, 0))
deleted_recipe_entry.bind("<Return>", lambda event: button_delete_recipe.invoke())

button_go_back = tk.Button(page_4_frame, text='Go to home page', font=('Arial', 10), bg='orange',
                           command=show_home_page)
button_go_back.pack(pady=10)

root.mainloop()




