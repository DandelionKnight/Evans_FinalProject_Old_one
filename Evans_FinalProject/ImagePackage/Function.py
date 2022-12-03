'''
Name: Team Evans
email: laupi@mail.uc.edu 
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project

'''
from PIL import Image

def load_image(filename):
    myimage = Image.open(filename)
    myimage.load()
    return myimage


