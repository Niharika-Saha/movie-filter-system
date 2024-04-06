import tkinter as tk
from PIL import ImageTk, Image
import csv

from tkinter import ttk

class Some1:
    def __init__(self):
        recommendation_window=tk.Tk()
        background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
        background_label = tk.Label(recommendation_window, image=background_image)
        background_label.place(x=0, y=0,relwidth=1, relheight=1)
        button_tbased = tk.Button(recommendation_window, text="Genre Based Recommendations",command=open_module_window1)
        button_des=tk.Button(recommendation_window,text="Description Based Recommendations",command=open_module_window2)
        button_yb = tk.Button(recommendation_window, text="Year Based Recommendations",command=open_module_window4)
        button_lang = tk.Button(recommendation_window, text="Language Based Recommendations",command=open_module_window3)
        button_runtime = tk.Button(recommendation_window, text="Runtime Based Recommendations",command=open_module_window5)
        button_top50 = tk.Button(recommendation_window, text="Top 50 Movies",command=open_module_window6) 
        button_tbased.grid(row=6, column=1, pady=50)

        button_des.grid(row=8,column=1,pady=50)

        button_yb.grid(row=6, column=5, pady=50)
        button_lang.grid(row=8, column=5, pady=50)
        button_runtime.grid(row=10, column=1, pady=50)
        button_top50.grid(row=10, column=5, pady=50)

        #background_label.lower()
        recommendation_window.mainloop()


def open_module_window1():
    import genre_final_copy
    '''
    module_path = "/Users/prakhyasantosh/Downloads/genre_final_copy.py"
    
    try:
        with open(f"/Users/prakhyasantosh/Downloads/genre_final_copy.py","r") as file:
            code=file.read()
            exec(code)
    except Exception as e:
            print("Module unable to open")
    '''
def open_module_window2():
    import keyword_final_copy

    '''
    keyword_final="/Users/prakhyasantosh/Downloads/keyword_final_copy.py"
    try:
        with open(f"/Users/prakhyasantosh/Downloads/keyword_final_copy.py","r") as file:
            code=file.read()
            exec(code)
    except Exception as e:
        print("Module unable to open")
    '''
def open_module_window3():
    import language_final_copy

    '''
    language_final="/Users/prakhyasantosh/Downloads/language_final-6.py"
    try:
        with open(f"/Users/prakhyasantosh/Downloads/language_final-6.py","r") as file:
            code=file.read()
            exec(code)
    except Exception as e:
        print("Module unable to open")
    '''
    
def open_module_window4():
    import year_final_copy
    '''
    year_final="/Users/prakhyasantosh/Downloads/year_final_copy.py"
    try:
        with open(f"/Users/prakhyasantosh/Downloads/year_final_copy.py","r") as file:
            code=file.read()
            exec(code)
    except Exception as e:
        print("Module unable to open")
    '''

def open_module_window5():
    import runtime_final_copy
    '''
    runtime_final="/Users/prakhyasantosh/Downloads/runtime_final_copy.py"
    try:
        with open(f"/Users/prakhyasantosh/Downloads/runtime_final_copy.py","r") as file:
            code=file.read()
            exec(code)
    except Exception as e:
        print("Module unable to open")
    '''
def open_module_window6():
    import top50_final_copy

    '''
    top50_final="/Users/prakhyasantosh/Downloads/top50_final_copy.py"
    try:
        with open(f"/Users/prakhyasantosh/Downloads/top50_final_copy.py","r") as file:
            code=file.read()
            exec(code)
    except Exception as e:
        print("Module unable to open")
    '''
'''
recommendation_window=tk.Tk()

button_tbased = tk.Button(recommendation_window, text="Genre Based Recommendations",command=open_module_window1)
button_des=tk.Button(recommendation_window,text="Description Based Recommendations",command=open_module_window2)
button_yb = tk.Button(recommendation_window, text="Year Based Recommendations",command=open_module_window4)
button_lang = tk.Button(recommendation_window, text="Language Based Recommendations",command=open_module_window3)
button_runtime = tk.Button(recommendation_window, text="Runtime Based Recommendations",command=open_module_window5)
button_top50 = tk.Button(recommendation_window, text="Top 50 Movies",command=open_module_window6) 
button_tbased.grid(row=6, column=1, pady=50)

button_des.grid(row=8,column=1,pady=50)

button_yb.grid(row=6, column=5, pady=50)
button_lang.grid(row=8, column=5, pady=50)
button_runtime.grid(row=10, column=1, pady=50)
button_top50.grid(row=10, column=5, pady=50)

background_image = tk.PhotoImage(file="/Users/prakhyasantosh/Downloads/cinema1.png")
background_label = tk.Label(recommendation_window, image=background_image)
background_label.place(x=0, y=0,relwidth=1, relheight=1)


background_label.lower()
recommendation_window.mainloop()
'''
