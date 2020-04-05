package com.company;
import java.util.*;

public class Bank
{
    private Customer[] customers = new Customer[10];
    private int numberOfCustomer = 0;
    private String bankName;

    public Bank(String bankName)
    {
        this.bankName = bankName;
    }

    public void addCustomer(Customer customer)
    {
        this.customers = Arrays.copyOf(this.customers, this.customers.length + 1);
        this.customers[this.customers.length-1] = customer;
        this.numberOfCustomer +=1 ;
    }

    public int getNumOfCustomers()
    {
        return this.numberOfCustomer;
    }

    public Customer getCustomer(int index)
    {
        return this.customers[index+1];
    }

    public void printCustomers()
    {
        System.out.println("\nList of Customers: ");
        for (int i=1; i<=getNumOfCustomers(); i++)
        {
            System.out.println("- " + this.customers[i].getFirstName() + " " + this.customers[i].getLastName());
        }
    }

    @Override
    public String toString()
    {
        return "Bank[ " +
                "\nBank Name: " + bankName + '\'' +
                "\nNumber of Customers: " + numberOfCustomer + " ]";
    }
}