'''
- loop dictionary comparing values
- 
'''

def recipe_batches(recipe, ingredients):
  batches = 9999

  for i in recipe:
      if ingredients[i] // recipe[i] < batches:
        batches = ingredients[i] // recipe[i]
  
  return batches

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))

'''
#!/usr/bin/python
import math

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
'''