# Name:Minsun Kim
# SBUID: 115964125
##################### SCORE ######################
#######  Score:  6/10
#################################################
# Remove the ellipses (...) when writing your solutions.
## your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/minsun6711/Homework_1.py"
# The area of the triangle is : 32.0 , its perimeter is : 27.440161448987652-> correct
# The area of the polygon is : 14.530850560107215 --> wrong
# no answer for 1st qs
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   c = (5/9)*(fahrenheit-32)
   return c 

def what_to_wear(celsius):
   if celsius < -10:
       return "puffy jacket"
   elif -10<=celsius<0:
       return "Scarf" 
   elif 0<=celsius<10:
        return "Sweater"
   elif 10<=celsius<20:
       return "Light jacket"
   else:
       return "T-shirt"
    


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs (((x1*y2+x2*y3+x3*y1)-(x1*y3+x2*y1+x3*y2))/2)
    return area 

def euclidean_distance(x1, y1, x2, y2):
    d= ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return d
    

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    perimeter1 = euclidean_distance(x1,y1,x2,y2)
    perimeter2 = euclidean_distance(x2,y2,x3,y3)
    perimeter3 = euclidean_distance(x3,y3,x1,y1)
    return perimeter1+perimeter2+perimeter3
    


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area
import math 

def deg2rad(deg):
    return deg * math.pi/180
    

def apothem(number_sides, length_side):
    a = length_side/2* math.tan(deg2rad(180/number_sides))
    return a 
  

def polygon_area(number_sides, length_side):
    area = (number_sides* length_side * apothem(number_sides, length_side))/2 
    return area 


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

