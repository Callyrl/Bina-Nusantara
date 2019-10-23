#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:44:25 2019

@author: cally
"""

class Staff:
    __ID = input("Input ID [SXXXX]: ")
    __name = input("Input Name [0...20]: ")
    __position = input("Input[Position[Stadd|Officer|Manager]: ")
    __salary = input("Salary for Offcier: ")
    
    def __init__(self, ID, name, position, salary):
        self.__ID = ID
        self.__name = name
        self.__position = position
        self.__salary = salary
        
    def name(self):
        return self.__name 
    
    def getPosition(self):
        return self.__position
    
        
    
    def salary(self):
        
        
class Office:
    def __init__(self):
        self.__path = "data.txt"
        with open(self.__path, 'r') as file:
            self.__staff = file.readlines().splitlines()
        
    def newStaff(self, ID, name,position, salary):
       userID = self.__ID
       name = self.__name
       self.__staff.append(
       with open(self.__path, 'w') as newdata:
           for staff in self.__staff:
               newdata.write(
        
    def deleteStaff(self, ID):
        userID = self.__ID
        if userID in self.__data:
            self.__staff.remove(ID)
            with open(self.__data, 'w') as newdata:
                for staff in self.__staff:
                    newdata.write(staff + "\n")
            print("You have successfully removed staff: ", self.__name, " from the database.")
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
    
    office = Office(Staff)
    
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save and Exit")
    
    choice = (int(input("Input choice: ")))

    while True:
        if choice == 1:
            office.newStaff(Staff)
            choice = (int(input("Input choice: ")))
            
        elif choice == 2:
            office.deleteStaff(Staff)
            choice = (int(input("Input choice: ")))
        
        elif choice == 3:
            office.viewSummary()
            choice = (int(input("Input choice: ")))
        
        elif choice >= 5:
            print("Invalid choice. Enter 1-4.")
            adminMenu()
        
        elif choice == 4:
            break
    print("Goodbye!")    

    
