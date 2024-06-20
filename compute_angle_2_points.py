import math

def compute_angle_2D(p1, p2, p3):
    # Calculate the distances between the points
    a = math.sqrt((p3[0]-p2[0])**2 + (p3[1]-p2[1])**2)
    b = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    c = math.sqrt((p3[0]-p1[0])**2 + (p3[1]-p1[1])**2)
    
    # Apply the law of cosines
    angle = math.acos((b**2 + c**2 - a**2) / ((2*b*c)+1e-6))
    
    # Convert the angle to degrees
    angle = 180 - math.degrees(angle)
    
    return angle