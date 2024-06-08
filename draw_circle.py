import rhinoscriptsyntax as rs

def create_circles():
    radius = 1
    spacing = 2
    
    for i in range(10):
        center = (i * spacing, 0,0)
        rs.AddCircle(center, radius)
        
create_circles()

