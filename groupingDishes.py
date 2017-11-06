def groupingDishes(dishes):
    # Given a list of dishes with ingredients, group dishes by ingredient
    # Remove any ingredients with only one dish
    
    groups = {}
    
    for dishName, *ingredients in dishes:
        # loop through dish's ingredients
        for ingredient in ingredients:
            # Append to dishes with that ingredient
            # if ingredient in groups:
            #     dish_list = groups[ingredient]
            #     dish_list.append(dishName)
            #     groups[ingredient] = dish_list
            # else:
            #     groups[ingredient] = [dishName]

            # Cool awesome way to append, return the list, set value
            groups.setdefault(ingredient, []).append(dishName)

    # retList = []
    # sort keys, sort items, remove singletons
    # Note, this can be done with list comprehension

    # for key in sorted(groups):
    #     if len(groups[key]) > 1:
    #         # create the output from the dictionary
    #         retList.append([key] + sorted(groups[key]))

    ret_list = [[key] + sorted(groups[key]) for key in sorted(groups) if len(groups[key]) > 1]
    
    return ret_list

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

print(groupingDishes(dishes))
