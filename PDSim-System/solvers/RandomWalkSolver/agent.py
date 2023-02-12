import numpy as np
import random as r

# AGENT CLASS
class Agent:
    def __init__(self, id, pos):

        self.id = id
        self.pos = pos

    def __str__(self) -> str:
        return f"{self.pos}"

    def move(self, boardChoices):
        newPos = r.choice(boardChoices)
        return id, newPos
        
