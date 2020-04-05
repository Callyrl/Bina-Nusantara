package com.company;
import java.util.*;

public class Driver
{
    public static void main(String[] args)
    {
        // Testing Account Class
        Account a1 = new Account(250);
        Account a2 = new Account (500);
        Account a3 = new Account (10000);

        System.out.println(a1.deposit(100));       // True
        System.out.println(a1.withdraw(50));       // True

        System.out.println(a3.deposit(-100));      // False
        System.out.println(a2.withdraw(1000));     // False


        // Testing Customer & Bank Class
        Customer c1 = new Customer("Jeconiah", "Richard");
        Customer c2 = new Customer("Claudia","Rachel");
        Customer c3 = new Customer("Rowin", "Fadhilla");

        c1.setAccount(a1);
        c2.setAccount(a2);
        c3.setAccount(a3);

        System.out.println(c1.toString());        // Jeconiah Richard
        System.out.println(c1.getAccount());      // 300

        // Testing Bank Class
        Bank b1 = new Bank("GANG");
        Bank b2 = new Bank("GENG");

        b1.addCustomer(c1);
        b2.addCustomer(c2);
        b2.addCustomer(c3);

        System.out.println(b1.getNumOfCustomers());      // 1
        System.out.println(b2.getNumOfCustomers());      // 2

        System.out.println(b1.toString());
    }
}
