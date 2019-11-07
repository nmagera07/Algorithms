#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    arr = []
    arr2 = []
    for x in recipe.values():
        arr.append(x)
    for y in ingredients.values():
        arr2.append(y)

    for i in recipe:
        pass
    for j in ingredients:
        pass

    if i == j and len(i) == len(j) and y >= x:
        res = [j / i for i, j in zip(arr, arr2)]
        print(int(res[0]))
    else:
        print(0)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 51, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))