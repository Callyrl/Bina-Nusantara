package com.company;

public class Frigate implements IsSeaVessel
{
    private String name = "";
    private int maxPassenger = 0;
    private double maxSpeed = 0;
    private int displacement = 0;

    Frigate(String name, int maxPassenger, double maxSpeed, int displacement)
    {
        setName(name);
        setMaxPassenger(maxPassenger);
        setMaxSpeed(maxSpeed);
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

    public void fireGun()
    {
        System.out.println("PEW PEW GO DIE :<");
    }

    @Override
    public String toString()
    {
        return "A vehicle of type Frigate with a name " + this.getName() + ", a capacity of max " + this.getMaxPassenger()
                + ", a max speed of " + this.getMaxSpeed() + " and a max displacement of" + this.getDisplacement();
    }
}
