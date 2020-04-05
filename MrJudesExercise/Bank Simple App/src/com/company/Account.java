package com.company;

public class Account
{
    private double balance;

    public Account(double balance)
    {
        this.balance = balance;
    }

    public double getBalance()
    {
        return balance;
    }

    public boolean deposit(double amt)
    {
        if (amt > 0)
            return true;
        else
            return false;
    }

    public boolean withdraw(double amt)
    {
        if(this.balance >= amt)
        {
            this.balance -= amt;
            return true;
        }

        else
        {
            return false;
        }
    }

    @Override
    public String toString()
    {
        return "Account[ " + "Balance: " + balance + " ]";
    }
}