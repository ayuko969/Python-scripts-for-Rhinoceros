import rhinoscriptsyntax as rs
import random

def assign_random_color():
    objs = rs.GetObjects("Select objects to assign random colours")
    if objs:
        for obj in objs:
            color = [random.randint(0,255),random.randint(0,255),random.randint(0,255),]
            rs.ObjectColor(obj, color)
            
assign_random_color()