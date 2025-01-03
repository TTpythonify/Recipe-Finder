import webbrowser

def find_recipe():
    results = {}
    data = {'results': [
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/JMQ3ZPPP/kerabu-rice-rice-salad', 'image': 'kerabu-rice-rice-salad-648822.jpg', 'servings': 12, 'id': 648822, 'title': 'Kerabu Rice (Rice Salad)'},
        {'readyInMinutes': 30, 'sourceUrl': 'https://fullbellysisters.blogspot.com/2012/01/cauliflower-fried-rice-more-veggies.html', 'image': 'cauliflower-brown-rice-and-vegetable-fried-rice-716426.jpg', 'servings': 8, 'id': 716426, 'title': 'Cauliflower, Brown Rice, and Vegetable Fried Rice'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/H4TVGTQM/wild-rice-with-bacon-mushrooms-green-onions', 'image': 'Wild-Rice-With-Bacon--Mushrooms---Green-Onions-665344.jpg', 'servings': 6, 'id': 665344, 'title': 'Wild Rice With Bacon, Mushrooms & Green Onions'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/RB57HRNX/tomato-and-bacon-pizza-with-rice-crust', 'image': 'Tomato-and-Bacon-Pizza-With-Rice-Crust-663553.jpg', 'servings': 8, 'id': 663553, 'title': 'Tomato and Bacon Pizza With Rice Crust'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/LTPYSJCV/autumn-fried-rice-with-buffalo-nuts', 'image': 'Autumn-Fried-Rice-with-Buffalo-Nuts-633093.jpg', 'servings': 8, 'id': 633093, 'title': 'Autumn Fried Rice with Buffalo Nuts®'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/TTSVHLSH/chinese-veg-fried-rice', 'image': 'Chinese-Veg-Fried-rice-638729.jpg', 'servings': 4, 'id': 638729, 'title': 'Chinese Veg Fried rice'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/RYNTB4NP/cumin-scented-basmati-rice-pilaf', 'image': 'Cumin-Scented-Basmati-Rice-Pilaf-641034.jpg', 'servings': 6, 'id': 641034, 'title': 'Cumin-Scented Basmati Rice Pilaf'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/L7577Z86/orange-chicken-with-brown-rice-gluten-free', 'image': 'Orange-Chicken-With-Brown-Rice-(Gluten-Free)-653835.jpg', 'servings': 4, 'id': 653835, 'title': 'Orange Chicken With Brown Rice (Gluten-Free)'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/KY4LQ345/healthier-pork-fried-rice', 'image': 'Healthier-Pork-Fried-Rice-646425.jpg', 'servings': 3, 'id': 646425, 'title': 'Healthier Pork Fried Rice'}, 
        {'readyInMinutes': 45, 'sourceUrl': 'https://www.foodista.com/recipe/WZ82F5RR/saffron-infused-rice-pudding-with-sweetened-whole-wheat-pancakes', 'image': 'SAFFRON-INFUSED-RICE-PUDDING-WITH-SWEETENED-WHOLE-WHEAT-PANCAKES-658975.jpg', 'servings': 8, 'id': 658975, 'title': 'SAFFRON INFUSED RICE PUDDING WITH SWEETENED WHOLE WHEAT PANCAKES'}
    ],
    'baseUri': 'https://img.spoonacular.com/recipes/', 
    'offset': 0, 
    'number': 10, 
    'totalResults': 312, 
    'processingTimeMs': 77, 
    'expires': 1735908627550, 
    'isStale': False}

    for recipe in data['results']:
        # Extract the necessary information
        more_info = recipe['sourceUrl']
        info_image = recipe['image']
        info_title = recipe['title']
        
        # Add this information to the results dictionary
        results[recipe["id"]] = {
            "sourceURL": more_info,
            "image": info_image,
            "title": info_title
        }

    print(results)

# Call the function
find_recipe()
