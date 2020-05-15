package com.company;

public class Jeep implements IsLandVehicle
{
    private String name = "";
    private int maxPassenger = 0;
    private double maxSpeed = 0;
    private int numWheels = 0;

    Jeep(String name, int maxPassenger, double maxSpeed, int numWheels)
    {
        setName(name);
        setMaxPassenger(maxPassenger);
        setMaxSpeed(maxSpeed);
        setNumWheels(numWheels);
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return this.name;
    }

    public int getMaxPassenger()
    {
        return this.maxPassenger;
    }

    public void setMaxPassenger(int maxPassenger)
    {
        this.maxPassenger = maxPassenger;
    }

    public void setMaxSpeed(double maxSpeed)
    {
        this.maxSpeed = maxSpeed;
    }

    public double getMaxSpeed()
    {
        return this.maxSpeed;
    }

    public int getNumWheels()
    {
        return this.numWheels;
    }

    public void setNumWheels(int n)
    {
        this.numWheels = n;
    }

    public void drive()
    {
        System.out.println("We ride at dawn");
    }

    public void soundHorn()
    {
        System.out.println("BEEP BEEP");
    }

    @Override
    public String toString()
    {
        return "A vehicle of type Jeep with a name " + this.getName() + ", has " + this.getNumWheels() +
                " wheels, a capacity of max " + this.getMaxPassenger() + ", and a max speed of " + this.getMaxSpeed();
    }

}