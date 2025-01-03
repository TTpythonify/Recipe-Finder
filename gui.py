import customtkinter as ctk
import webbrowser
import requests

class FoodSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Search App")
        self.root.geometry("600x400")  
        
        self.top_frame = ctk.CTkFrame(self.root)
        self.top_frame.pack(fill="x", pady=10)

        self.label = ctk.CTkLabel(self.top_frame, text="Enter food item:", font=("Arial", 14)) 
        self.label.pack(pady=5)
        
        self.food_entry = ctk.CTkEntry(self.top_frame, width=250, font=("Arial", 14)) 
        self.food_entry.pack(pady=5)
        
        self.search_button = ctk.CTkButton(self.top_frame, text="Search", font=("Arial", 14), 
                                           command=self.search_food)
        self.search_button.pack(pady=5)

        self.bottom_frame = ctk.CTkFrame(self.root)
        self.bottom_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create the scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.bottom_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = ctk.CTkFrame(self.bottom_frame)
        self.scrollable_frame.pack(side="left", fill="both", expand=True)

        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.scrollbar.configure(command=self.scrollable_frame.yview)
        )

        self.scrollable_frame.grid_rowconfigure(0, weight=1, minsize=200)

    def search_food(self):
        # Get the food item entered by the user
        food_item = self.food_entry.get()

        if food_item:
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

            querystring = {"query": food_item}

            headers = {
                "x-rapidapi-key": "1ae4654528msh82cf9d56f299a41p175eb1jsnebd34a46be13",
                "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            data = response.json()

            # Clear previous results
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Filter results based on the food item entered
            filtered_results = [food for food in data['results'] if food_item.lower() in food["title"].lower()]

            if filtered_results:
                for food in filtered_results:
                    # Create the frame for each food result
                    food_frame = ctk.CTkFrame(self.scrollable_frame)
                    food_frame.pack(pady=10, fill="x")

                    # Food title with smaller font size
                    food_title_label = ctk.CTkLabel(food_frame, text=food['title'], font=("Arial", 16), anchor="w")
                    food_title_label.pack(side="left", padx=10, expand=True)

                    # "More" button with smaller font size
                    more_button = ctk.CTkButton(food_frame, text="More", font=("Arial", 14), 
                                                command=lambda url=food['sourceUrl']: self.open_url(url))
                    more_button.pack(side="right", padx=10)

                 
                    separator = ctk.CTkLabel(self.scrollable_frame, text="-" * 50, font=("Arial", 12)) 
                    separator.pack(fill="x", pady=5)
            else:
                no_results_label = ctk.CTkLabel(self.scrollable_frame, text="No results found.", font=("Arial", 16))
                no_results_label.pack(pady=10)
        else:
            print("Please enter a food item.")

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    root = ctk.CTk()
    app = FoodSearchApp(root)
    root.mainloop()
