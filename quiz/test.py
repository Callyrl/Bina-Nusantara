#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:44:25 2019

@author: cally
"""

import csv

path = "data.csv"
    
with open(path) as file:
    reader = csv.reader(file)
    header = next(reader)
    for column in reader:
         IDs = column[0]
         names = column[1]
         posiotions = column[2]
         
ID = []
name = []
position = []
salary = []
         
class Staff:
    __ID = input("Input ID [SXXXX]: ")
    __name = input("Input Name [0...20]: ")
    __position = input("Input[Position[Stadd|Officer|Manager]: ")
    __salary = input("Salary for ", __position, ": ")
    
    def __init__(self, ID, name, position, salary):
        self.__ID = ID
        self.__name = name
        self.__position = position
        self.__salary = salary
        
    def newStaff(self, newID, newName, newPosition, newSalary):
       return self.self.__ID 
       return self.__name 
       return self.__position 
       return self.__salary 
        
   
    def deleteStaff(self, ID):
        if self.__ID in ID:
            ID.remove(self.__ID)
            print("You have successfully removed staf from the database.")
        else:
            print("Staff not found in the database.")
            
    def viewSummary(self):
        for 
            if position == "Staff"
                minimumS = 
                maximumS =
                averageS =
            
            elif position == "Officer"
                minimumO =
                maximumO = 
                averageO =
                
            elif position == "Manager"
                minimumM =
                maximumM = 
                averageM =
        
        print("1. Salary")
        print("Minimum Salary: ", minimumS)
        print("Maximum Salary: ", maximumS)
        print("Average Salary: ", averageS)
        
        print("2. Officer")
        print("Minimum Salary: ", minimumO)
        print("Maximum Salary: ", maximumO)
        print("Average Salary: ", averageO)
        
        print("3. Manager")
        print("Minimum Salary: ", minimumM)
        print("Maximum Salary: ",maximumM)
        print("Average Salary: ",averageM)
    

    
def menu():
    
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save and Exit")
    
    choice = (int(input("Input choice: ")))

    while True:
        if choice == 1:
            Staff.newStaff(Staff)
            choice = (int(input("Input choice: ")))
            
        elif choice == 2:
            Staff.deleteStaff(Staff)
            choice = (int(input("Input choice: ")))
        
        elif choice == 3:
            Staff.viewSummary()
            choice = (int(input("Input choice: ")))
        
        elif choice >= 5:
            print("Invalid choice. Enter 1-4.")
            menu()
        
        elif choice == 4:
            break
        
    print("Goodbye!")    
