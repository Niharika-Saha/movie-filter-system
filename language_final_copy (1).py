import tkinter as tk
from tkinter import ttk
import csv
from PIL import Image, ImageTk

class MovieDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendations Based on Language")
        self.root.geometry("720x720") 

        self.background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
        #photo=ImageTk.PhotoImage(self.background_image)

        self.create_gui()

    def create_gui(self):

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0,relwidth=1, relheight=1)
        
  

        self.label_language = ttk.Label(self.root, text="Select Language:",style='Custom.TLabel')
        self.label_language.grid(row=6, column=3, padx=20, pady=20)

        
        self.languages = ['en', 'fr', 'it', 'es','ko','ja']
        self.selected_language = tk.StringVar()
        self.language_dropdown = ttk.Combobox(self.root, textvariable=self.selected_language, values=self.languages,width=50)
        self.language_dropdown.grid(row=6, column=5, padx=20, pady=20)

        self.language_dropdown['postcommand'] = self.update_menu_length


        self.button = ttk.Button(self.root, text="Search", command=self.search_movie,style='Custom.TButton')
        self.button.grid(row=6, column=7, padx=20, pady=10, sticky='e')

        self.recommendation_label = ttk.Label(self.root, text="Recommendations:",style='Custom.TLabel')
        self.recommendation_label.grid(row=8, column=3, padx=20, pady=15)

        tree_style = ttk.Style()
        tree_style.configure('Pastel.Treeview', background='#ffe4e1')
        self.recommendation_tree = ttk.Treeview(self.root, columns=('Title', 'Year', 'Genre', 'Description', 'Language'), show='headings',height=25,style='Pastel.Treeview')
        self.recommendation_tree.heading('Title', text='Title')
        self.recommendation_tree.heading('Year', text='Year')
        self.recommendation_tree.heading('Genre', text='Genre')
        self.recommendation_tree.heading('Description', text='Description')
        self.recommendation_tree.heading('Language', text='Language')
        #self.recommendation_tree.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
        self.recommendation_tree.grid(row=12, column=0, rowspan=40, columnspan=25, padx=150, pady=5)

        self.root.style = ttk.Style()
        self.root.style.configure('Custom.TButton', padding=(10, 5), font=('Times New Roman', 12, 'bold'), foreground='maroon')
        self.root.style.configure('Custom.TLabel', font=('Times New Roman', 15), foreground='maroon')


        self.background_label.lower()

      

       

    def search_movie(self):
        language = self.selected_language.get()

        if language:
            movie_info = self.get_movie_info(language)

            if movie_info:
                #self.update_tree(self.tree, [movie_info])
                recommended_movies = self.get_recommendations(movie_info, language)
                self.update_tree(self.recommendation_tree, recommended_movies)
            else:
                print("Movie not found.")
                #self.update_tree(self.tree, [])
                self.update_tree(self.recommendation_tree, [])
        else:
            print("Please select a language of your choice.")

    def get_movie_info(self, language):
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_language = row['Language']

                if (language and language == row_language):
                    return {
                        'Title': row['Title'],
                        'Year': row['Year'],
                        'Genre': row['Genre'],
                        'Description': row['overview'],
                        'Language': row['Language']
                    }
        return None

    def update_tree(self, tree, data):
        tree.delete(*tree.get_children())
        if isinstance(data, dict):
            tree.insert('', 'end', values=(data['Title'], data['Year'], data['Genre'], data['Description'], data['Language']))
        elif isinstance(data, list):
            for movie in data:
                tree.insert('', 'end', values=(movie['Title'], movie['Year'], movie['Genre'], movie['Description'], movie['Language']))

    def get_recommendations(self, current_movie, language):
        recommended_movies = []
        with open('tmdb_5000_movies.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (not language or row['Language'] == language):
                    recommended_movies.append({
                        'Title': row['Title'],
                        'Year': row['Year'],
                        'Genre': row['Genre'],
                        'Description': row['overview'],
                        'Language': row['Language']
                    })
        return recommended_movies
    def update_menu_length(self):
        self.language_dropdown.configure(height=len(self.languages) + 2)


#if __name__ == "__main__":
root = tk.Toplevel()
    #root=trail.tk()
    #root.geometry('500x500')
app = MovieDatabaseApp(root)
style = ttk.Style()
style.configure('LightBlue.TButton', background='#ADD8E6')
root.mainloop()
