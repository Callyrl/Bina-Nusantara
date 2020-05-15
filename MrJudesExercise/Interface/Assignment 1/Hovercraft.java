package com.company;

public class Hovercraft implements IsLandVehicle, IsSeaVessel
{
    private String name = "";
    private int maxPassenger = 0;
    private double maxSpeed = 0;
    private int numWheels = 0;
    private int displacement = 0;

    Hovercraft(String name, int maxPassenger, double maxSpeed, int numWheels, int displacement)
    {
        setName(name);
        setMaxPassenger(maxPassenger);
        setMaxSpeed(maxSpeed);
        setNumWheels(numWheels);
        setDisplacement(displacement);
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

    public void enterLand()
    {
        System.out.println("LAND HO");
    }

    public int getDisplacement()
    {
        return this.displacement;
    }

    public void setDisplacement(int displacement)
    {
        this.displacement = displacement;
    }

    public void launch()
    {
        System.out.println("Whoosh");
    }

    public void enterSea()
    {
        System.out.println("Aye Aye Captain");
    }

    @Override
    public String toString()
    {
        return "A vehicle of type Hovercraft with a name " + this.getName() + ", has " + this.getNumWheels() +
                " wheels, a capacity of max " + this.getMaxPassenger() + ", a max speed of " + this.getMaxSpeed()
                + " and a max displacement of" + this.getDisplacement();
    }
}
