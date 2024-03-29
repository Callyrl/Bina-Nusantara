package com.company;

public class Customer
{
    private String firstName;
    private String lastName;
    private Account account;

    public Customer(String firstName, String lastName)
    {
        this.firstName = firstName ;
        this.lastName = lastName;
    }

    public String getFirstName()
    {
        return this.firstName;
    }

    public String getLastName()
    {
        return this.lastName;
    }

    public Account getAccount()
    {
        return this.account;
    }

    public void setAccount(Account account)
    {
        this.account = account;
    }

    @Override
    public String toString()
    {
        return "Customer[ " + "First Name: " + firstName + ", Last Name: " + lastName + " ]";
    }
}
