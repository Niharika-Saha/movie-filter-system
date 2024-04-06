import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image,ImageTk

class Movie_Recommendations_based_on_Runtime:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendations based on Runtime")
        self.root.geometry("720x720") 

        self.background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
        #photo=ImageTk.PhotoImage(self.background_image)'''
        self.create_gui()

    def create_gui(self):

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Adding three filter buttons
        self.filter_button_1 = ttk.Button(self.root, text="Movies (Runtime < 90 mins)", command=lambda: self.display_filtered_movies(0, 90))
        self.filter_button_1.grid(row=7, column=25, padx=100, pady=40)

        self.filter_button_2 = ttk.Button(self.root, text="Movies (Runtime between 90 and 120 mins)", command=lambda: self.display_filtered_movies(90, 120))
        self.filter_button_2.grid(row=7, column=30, padx=100, pady=40)

        self.filter_button_3 = ttk.Button(self.root, text="Movies (Runtime > 120 mins)", command=lambda: self.display_filtered_movies(120))
        self.filter_button_3.grid(row=7, column=35, padx=100, pady=40)

        self.tree = ttk.Treeview(self.root, columns=('Title', 'Year', 'Genre', 'description', 'Language', 'Runtime'), show='headings', height=25)
        self.tree.heading('Title', text='Title')
        self.tree.heading('Year', text='Year')
        self.tree.heading('Genre', text='Genre')
        self.tree.heading('description', text='Description')
        self.tree.heading('Language', text='Language')
        self.tree.heading('Runtime', text='Runtime')
        self.tree.grid(row=30, column=6, rowspan=40, columnspan=75, padx=100, pady=50)

    def display_filtered_movies(self, min_runtime, max_runtime=float('inf')):
        filtered_movies = self.get_filtered_movies(min_runtime, max_runtime)
        self.update_tree(self.tree, filtered_movies)

    def get_filtered_movies(self, min_runtime, max_runtime=float('inf')):
        movies = []
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Filter movies with runtime in the specified range
            filtered_movies = [row for row in reader if row['runtime'].strip() and min_runtime < float(row['runtime']) <= max_runtime]
            for row in filtered_movies:
                movies.append({
                    'Title': row['title'],
                    'Year': row['Year'][:4],
                    'Genre': row['Genre'],
                    'description': row['overview'],
                    'Language': row['Language'],
                    'Runtime': row['runtime']
                })
        return movies

    def update_tree(self, tree, data):
        tree.delete(*tree.get_children())
        if isinstance(data, dict):
            tree.insert('', 'end', values=(data['Title'], data['Year'], data['Genre'], data['description'], data['Language'], data['Runtime']))
        elif isinstance(data, list):
            for movie in data:
                tree.insert('', 'end', values=(movie['Title'], movie['Year'], movie['Genre'], movie['description'], movie['Language'], movie['Runtime']))


#if __name__ == "__main__":
root = tk.Toplevel()
#root=trail.tk()
#root.geometry('500x500')
app = Movie_Recommendations_based_on_Runtime(root)
root.mainloop()
