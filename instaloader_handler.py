#Instructions: use this to get the photos into the categories folder, 
# from there sort and rename the category1,category2,category3 folders
# to set the category names on the website. The category1 folder name 
# will determine said category name, and the folders inside will be the 
# folder of photos that sort under that
#I would automate it but different who knows what categories futures would want 

#next step is to run the 

import instaloader
import os
import shutil
loader = instaloader.Instaloader()
from Insta_to_Bootstrap import html_editor
import webbrowser

import tkinter as tk


import customtkinter as ctk




def get_instagram(username):
    for post in list(instaloader.Profile.from_username(loader.context,username).get_posts()):
        # post is an instance of instaloader.Post    print( post.shortcode)

        loader.download_post(post, target='instagram.com-p-' +post.shortcode)



def filter_and_copy_folders(root_dir, destination_dir, extensions):
    
    for foldername in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, foldername)
        if os.path.isdir(folder_path) and 'instagram.com-p-' in str(folder_path) :
            print(folder_path)
            destination_path = os.path.join(destination_dir, foldername)
            os.makedirs(destination_path, exist_ok=True)
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path) and filename.lower().endswith(extensions):

                    new_file_path = os.path.join(destination_path, filename)
                    shutil.copy2(file_path, new_file_path)
                    print(f"Copied file '{filename}' to '{new_file_path}'")

                    os.remove(file_path)
                else:
                    os.remove(file_path)
            os.rmdir(folder_path)






#get_instagram('themattiepattie')


ctk.set_appearance_mode("System")

ctk.set_default_color_theme("dark-blue")


appWidth, appHeight = 600, 700

class App(ctk.CTk):
    count = 0
    memory = {}
    
    def make_field(self, title, place_holder, column = 0): #function to make a new field, useful if later you want new default metadata options
        self.title_field = ctk.CTkLabel(self, text=title)
        self.title_field.grid(row=App.count, column=0, padx=20, pady=20, sticky='ew')

        self.title_entry = ctk.CTkEntry(self, placeholder_text=place_holder)
        self.title_entry.grid(row=App.count, column=1, padx=20, pady=20, sticky='ew')
        App.memory[title]=self.title_entry
        App.count = App.count + 1
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("GUI for remediation")
        self.geometry(f"{appWidth}x{appHeight}")
        # Info for presenting the title form field
        self.generateResultsButton = ctk.CTkButton(self, text="Generate Instagram_folders", command=self.get_insta)# gen results button leads to the create Text
        self.generateResultsButton.grid(row=0, column=4, columnspan=2, padx=20, pady=20, sticky="ew")
        self.generateHTMLButton = ctk.CTkButton(self, text="Generate HTML", command=self.gen_html)# gen results button leads to the create Text
        self.generateHTMLButton.grid(row=2, column=4, columnspan=2, padx=20, pady=20, sticky="ew")

        self.display_box = ctk.CTkTextbox(self, width=200, height=100)# makes the display box so you know it worked
        self.display_box.grid(row=1, column=4, columnspan=4, padx=20, pady=20, sticky="nsew")
        
        
    def get_insta(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))

        destination_dir = str(root_dir) + '/Insta_to_Bootstrap/Categories_folder' # The destination directory where 'client' folders will be moved
        extensions_to_move = ('.jpeg', '.jpg', '.mp4')
        text = [key +': ' +App.memory[key].get() for key in App.memory]
        print(text,'texttt')
        print(App.memory['Username'].get(),"TITLEEEE")
        get_instagram(App.memory['Username'].get())
        filter_and_copy_folders(root_dir, destination_dir,extensions_to_move)
        self.display_box.insert("0.0", str(text) +'rerange into category folders before running the next' )
    
    def gen_html(self):
        
        pathway = "Insta_to_Bootstrap\Categories_folder"

        html_editor.category_level_down(pathway)
        webbrowser.open('index.html')


        


    


    # The file will be automatically closed when exiting the 'with' block


 
               


if __name__ == "__main__":
    app = App()
    app.make_field("Username", "Themattiepattie")

    # Used to run the application
    app.mainloop()