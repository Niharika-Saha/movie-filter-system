import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image, ImageTk

class MovieDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System (using Content-based filtering)")
        self.root.geometry("720x720") 

        self.background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
        #photo=ImageTk.PhotoImage(self.background_image)
        self.create_gui()

    def create_gui(self):
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0,relwidth=1, relheight=1)

        icon_image = tk.PhotoImage(file='/Users/prakhyasantosh/Downloads/icon.png')
        small_icon = icon_image.subsample(5)
        
        
        self.top_50_button = ttk.Button(self.root, text="Top 50 Movies", command=self.display_top_50_movies, style='Custom.TButton')#,image=small_icon, compound=tk.LEFT)
        self.top_50_button.grid(row=1, column=20, padx=50, pady=50)

        self.top_50_button.image = small_icon
        self.root.style = ttk.Style()
        self.root.style.configure('Custom.TButton', font=('Times New Roman', 12, 'bold'), foreground='maroon', borderwidth=2, relief='solid')


        tree_style = ttk.Style()
        tree_style.configure('Pastel.Treeview', background='#ffe4e1')
        self.tree = ttk.Treeview(self.root, columns=('Title', 'Year', 'Genre', 'description', 'Language'), show='headings', height=25,style='Pastel.Treeview')
        self.tree.heading('Title', text='Title')
        self.tree.heading('Year', text='Year')
        self.tree.heading('Genre', text='Genre')
        self.tree.heading('description', text='description')
        self.tree.heading('Language', text='Language')
        self.tree.grid(row=2, column=8, rowspan=40, columnspan=25, padx=200, pady=5)

        self.background_label.lower()



    def display_top_50_movies(self):
        top_50_movies = self.get_top_50_movies()
        self.update_tree(self.tree, top_50_movies)

    def get_top_50_movies(self):
        movies = []
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            sorted_movies = sorted(reader, key=lambda x: float(x['popularity']), reverse=True)
            top_50_movies = sorted_movies[:50]
            for row in top_50_movies:
                movies.append({
                    'Title': row['Title'],
                    'Year': row['Year'],
                    'Genre': row['Genre'],
                    'description': row['description'],
                    'Language': row['Language']
                })
        return movies

    def update_tree(self, tree, data):
        tree.delete(*tree.get_children())
        if isinstance(data, dict):
            tree.insert('', 'end', values=(data['Title'], data['Year'], data['Genre'], data['description'],data['Language']))
        elif isinstance(data, list):
            for movie in data:
                tree.insert('', 'end', values=(movie['Title'], movie['Year'], movie['Genre'], movie['description'], movie['Language']))


#if __name__ == "__main__":
root = tk.Toplevel()
#root=trail.tk()
#root.geometry('500x500')
app = MovieDatabaseApp(root)
root.mainloop()

