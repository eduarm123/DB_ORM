#!/usr/bin/env python3
import db
import models

# Make these settings match your Makefile
user="demodb"
password="swordfish"
dbname="demodb"
port="3333"


def menu():
    print("Welcome to the recipe tool")
    print("------------------------")
    print()
    print("1: Initialise Database")
    print("2: List recipes")
    print("3: Add new recipies")
    print("4: View recipies")
    print("5: Add ingredients")
    print("6: View ingredients")
    print("7: Delete recipe")
    print("0: Quit")
    print()
    return int(input("Choose option: "))

if __name__=="__main__":

    session=db.connect(user,password,port,dbname)
    
    userInput=None

    while userInput!=0:
        userInput=menu()
        print()
        if userInput==1:            
            db.create_db(user,password,port,dbname)

        elif userInput==2:            
            recipes=session.query(models.Recipe).all()
            for recipe in recipes:
                print(f"{recipe.id}: {recipe.title}")
                
        elif userInput==3: # Add new recipies
            title=input("Enter new recipe title: ")
            #content=input("Enter new recipe instructions: ")
            newRecipe = models.Recipe(title=title)
            session.add(newRecipe)    
            session.commit()

        elif userInput==4: # View recipies
            recipeNum=int(input("Enter recipe number: "))
            recipe = session.query(models.Recipe).filter_by(id=recipeNum).first()
            if recipe==None:
                print("There is no recipe with that number")
            else:
                print(recipe.title)
                print("-"*len(recipe.title))
                print(recipe.content)
                
        elif userInput==5: # Add ingredients
            ingredientNum=int(input("Enter recipe number: "))
            recipe = session.query(models.Contains).filter_by(id=ingredientNum).first()
            if recipe==None:
                print("There is no recipe with that number")
            else:
                ingredientsCon=input("Enter ingredients ")
                newIngredient = models.Contains(ingredientsCon=ingredientsCon, containRecepies=recipe)
                session.add(newIngredient)    
                session.commit()
            
        elif userInput==6: # View ingredients
            ingredientNum=int(input("Enter recipe number: "))
            recipe = session.query(models.Recipe).filter_by(id=ingredientNum).first()
            if recipe==None:
                print("There is no recipe with that number")
            else:
                print(recipe.title)
                print("-"*len(recipe.title))
                print(recipe.content)
                

        elif userInput==7:
            recipeNum=int(input("Enter recipe number: "))
            recipe = session.query(models.Recipe).filter_by(id=recipeNum)
            if recipe==None:
                print("There is no recipe with that number")
            else:
                recipe.delete()
                session.commit()
        print()
