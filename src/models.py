#Import needed components from the module
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()



# Our models. Remove the demo "Note" and add your own
  

class Recipe(Base): # Wednesday
    __tablename__="recipe"
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    contains = relationship("Contains",back_populates="recipe")

class Ingredients(Base): # Thursday
    __tablename__="ingredients"
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    contains = relationship("Contains",back_populates="ingredients")
     
class Contains(Base):
    __tablename__="contains"
    id = Column(Integer, primary_key=True)
    
    recipe= relationship("Recipe", back_populates="containRecepies")
    ingredients = relationship("Ingredients", back_populates="containIngredients")
      
    containIngredients=Column(Integer, ForeignKey("contains.ingredients"))
    containRecepies=Column(Integer, ForeignKey("contains.recipe"))
  
