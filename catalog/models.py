from django.db import models

# Create your models here.

# Create Square Model
class Square(models.Model):
    # X or O or Empty

# Create Board 9x9
class Board(models.Model):
    # array of []
    #is full/finished?

# Create BIG Board of Boards 9x9
class BigBoard(models.Model):
    #array of boards?