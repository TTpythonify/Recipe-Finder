import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = {"query":"rice"}

headers = {
	"x-rapidapi-key": "1ae4654528msh82cf9d56f299a41p175eb1jsnebd34a46be13",
	"x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())