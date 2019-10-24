#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:44:25 2019

@author: cally
"""

import pandas as pd

path = "data.csv"
    
with open(path) as file:
    data = pd.read_csv(file, delimiter = ",", index_col = False)
    sort = data.sort_values("Name")

class Staff:

    def __init__(self, ID, name, position, salary):
        self.__ID = ID
        self.__name = name
        self.__position = position
        self.__salary = salary
        
    def newStaff(self):
        self.__userID = input("Input ID [SXXXX]: ")
        if self.__userID[0] != 'n' and len(self.__userID[1:4]) != 4:
            self.__userID = input("Input ID[nXXXX]: ")
        else:
            return self.__userID
        
        self.__userName = input("Input Name [0...20]: ")
        if len(self.__userName) > 0 and len(self.__userName) < 21:
            return self.__userName
        else:
            self.userName = input("Input Name[0...20]: ")
            
        print('Position | Salary Range')
        print('Staff    | 3,500,000 - 7,000,000')
        print('Officer  | 7,000,001 - 10,000,000')
        print('Manager  | >10,000,000')
        
        self.__userPosition = input("Input Position[Staff|Officer|Manager]: ")        
        while True:
            if self.__userPosition == "staff":
                return self.__userPosition
                
                self.__userSalary = int(input("Input Salary: "))
                if self.__userSalary >= 3500000 and self.__userSalary <= 7000000:
                    return self.__userSalary
                else:
                    self.__userSalary = int(input("Input Salary: "))
                    
            elif self.__userPosition == "officer":
                return self.__userPosition
                
                self.__userSalary = int(input("Input Salary: "))
                if self.__userSalary >= 7000001 and self.__userSalary <= 10000000:
                    return self.__userSalary
                else:
                    self.__userSalary = int(input("Input Salary: "))  
                    
            elif self.__userPosition == "manager":
                return self.__userPosition
                
                self.__userSalary = int(input("Input Salary: "))
                if self.__userSalary >10000000:
                    return self.__userSalary
                else:
                    self.__userSalary = int(input("Input Salary: "))
            
            else:
                input("Input Position[Staff|Officer|Manager]: ") 
        
        with open(path) as file:
            data = pd.read_csv(file, delimiter = ",", index_col = False)
            sort = data.sort_values("Name")
            
        dataT = data.T
        dataT[self.__userID, self.__userName, self.__userPosition, self.__userSalary]
        data = dataT.T
        
        print(sort)
        print("You have successfully added a new staff")
        
    def deleteSatff(self):
         if self.__ID in data:
             data.drop(self.__ID , axis = 0, inplace = True)
             print(sort)
             print("You have successfully removed staf from the database.")
         else:
             print("Staff not found in the database.")
         
        
def menu():
    s = Staff(self, ID, name, position, salary)
    
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save and Exit")
    
    choice = (int(input("Input choice: ")))
        
    while True:
        if choice == 1:
            s.newStaff()
            choice = (int(input("Input choice: ")))
            
        elif choice == 2:
            s.deleteStaff()
            choice = (int(input("Input choice: ")))
            
        elif choice == 3:
            s.viewSummary()
            choice = (int(input("Input choice: ")))
    
        elif choice == 4:
            data.to_csv("data.csv", index = False)
            break
        
        elif choice >= 5:
            print("Invalid choice. Enter 1-4.")
            menu()
        
        print("Goodbye!")  
        
