import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image,ImageTk



class MovieDatabaseApp:
    def __init__(self, root):

        self.root = root
        self.root.title("Movie Recommendations Based on Genre")
        self.root.geometry("720x720") 

        self.background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
        #photo=ImageTk.PhotoImage(self.background_image)
        #self.photo.pack()

        self.create_gui()
        

    def create_gui(self):
        

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0,relwidth=1, relheight=1)
        
        self.label_title = ttk.Label(self.root, text="Enter Movie Title:",style='Custom.TLabel')
        
        self.label_title.grid(row=2, column=9, padx=200, pady=50)

        self.entry_title = ttk.Entry(self.root, width=60)
        self.entry_title.grid(row=2, column=10, padx=20, pady=10)

        self.button = ttk.Button(self.root, text="Search", command=self.search_movie,style='Custom.TButton')
        self.button.grid(row=2, column=54, padx=20, pady=10)

        self.recommendation_label = ttk.Label(self.root, text="Recommendations:",style='Custom.TButton')
        self.recommendation_label.grid(row=15, column=9, padx=200, pady=10)


        tree_style = ttk.Style()
        tree_style.configure('Pastel.Treeview', background='#ffe4e1')

        self.recommendation_tree = ttk.Treeview(self.root, columns=('Title', 'Year', 'Genre', 'description', 'Language'), show='headings',height=30 ,style='Pastel.Treeview')
        self.recommendation_tree.heading('Title', text='Title')
        self.recommendation_tree.heading('Year', text='Year')
        self.recommendation_tree.heading('Genre', text='Genre')
        self.recommendation_tree.heading('description', text='description')
        self.recommendation_tree.heading('Language', text='Language')
        self.recommendation_tree.grid(row=16, column=7, columnspan=100, padx=200, pady=10)

        self.root.style = ttk.Style()
        self.root.style.configure('Custom.TButton', padding=(10, 5), font=('Times New Roman', 12, 'bold'), foreground='maroon')
        self.root.style.configure('Custom.TLabel', font=('Times New Roman', 15), foreground='maroon')

        self.background_label.lower()

    def search_movie(self):
        title = self.entry_title.get().lower()

        if title:
            movie_info = self.get_movie_info(title)

            if movie_info:
                self.update_tree(self.recommendation_tree, [movie_info])  # Update only the lower box
                recommended_movies = self.get_recommendations(movie_info)
                self.update_tree(self.recommendation_tree, recommended_movies)
            else:
                print("Movie not found.")
                self.update_tree(self.recommendation_tree, [])
        else:
            print("Please enter a movie title.")
    def get_movie_info(self, title):
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_title = row['Title'].lower()

                if title and title in row_title:
                    return {
                        'Title': row['Title'],
                        'Year': row['Year'],
                        'Genre': row['Genre'],
                        'description': row['overview'],
                        'Language': row['Language']
                    }
        return None

    def update_tree(self, tree, data):
        tree.delete(*tree.get_children())
        if isinstance(data, dict):
            tree.insert('', 'end', values=(data['Title'], data['Year'], data['Genre'], data['description'], data['Language']))
        elif isinstance(data, list):
            for movie in data:
                tree.insert('', 'end', values=(movie['Title'], movie['Year'], movie['Genre'], movie['description'], movie['Language']))

    def get_recommendations(self, current_movie):
        recommended_movies = []
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
        
            for row in reader:
                if row['Title'] != current_movie['Title'] and row['Genre'] == current_movie['Genre']:

                    
                    
                    recommended_movies.append({
                        'Title': row['Title'],
                        'Year': row['Year'],
                        'Genre': row['Genre'],
                        'description': row['overview'],
                        'Language': row['Language']
                    })
                    
        return recommended_movies

#if __name__ == "__main__":
root = tk.Toplevel()
#root=trail.tk()
#root.geometry('500x500')
app = MovieDatabaseApp(root)
root.mainloop()
