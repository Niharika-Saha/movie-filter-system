import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image,ImageTk

class Movie_Recommendations_Based_on_Description_Keywords:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendations Based on Description/Keywords")
        self.background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
        #photo=ImageTk.PhotoImage(self.background_image)'''
        self.create_gui()

    def create_gui(self):
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0,relwidth=1, relheight=1)
        
        self.label_description = ttk.Label(self.root, text="Enter Description Keywords:",style='Custom.TLabel')
        self.label_description.grid(row=2, column=9, padx=200, pady=50)

        self.entry_description = ttk.Entry(self.root, width=60)
        self.entry_description.grid(row=2, column=10, padx=20, pady=10)

        self.button = ttk.Button(self.root, text="Search", command=self.search_movie,style='Custom.TButton')
        self.button.grid(row=2, column=54, padx=20, pady=10)

        self.recommendation_label = ttk.Label(self.root, text="Recommended Movies:",style='Custom.TButton')
        self.recommendation_label.grid(row=15, column=9, padx=198, pady=10)

        tree_style = ttk.Style()
        tree_style.configure('Pastel.Treeview', background='#ffe4e1')
        self.recommendation_tree = ttk.Treeview(self.root, columns=('Title', 'Year', 'Genre', 'description', 'Language'), show='headings',height=22,style='Pastel.Treeview')
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
        description_keywords = self.entry_description.get().lower()

        if description_keywords:
            recommended_movies = self.get_movies_by_description(description_keywords)

            if recommended_movies:
                # Display the remaining recommended movies
                self.update_tree(self.recommendation_tree, recommended_movies)
            else:
                print("No movies found with the specified description keywords.")
        else:
            print("Please enter description keywords.")

    def get_movies_by_description(self, description_keywords):
        recommended_movies = []
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_description = row['description'].lower()
                if all(keyword in row_description for keyword in description_keywords.split()):
                    recommended_movies.append({
                        'Title': row['Title'],
                        'Year': row['Year'],
                        'Genre': row['Genre'],
                        'description': row['overview'],
                        'Language': row['Language']
                    })
        return recommended_movies

    def update_tree(self, tree, data):
        tree.delete(*tree.get_children())
        if isinstance(data, dict):
            tree.insert('', 'end', values=(data['Title'], data['Year'], data['Genre'], data['description'], data['Language']))
        elif isinstance(data, list):
            for movie in data:
                tree.insert('', 'end', values=(movie['Title'], movie['Year'], movie['Genre'], movie['description'], movie['Language']))


#if __name__ == "__main__":
root = tk.Toplevel()
    #root=trail.tk()
    #root.geometry('500x500')
app = Movie_Recommendations_Based_on_Description_Keywords(root)
root.mainloop()

