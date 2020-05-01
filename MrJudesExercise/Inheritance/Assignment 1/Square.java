package com.company;

public class Square extends Rectangle
{
    public Square()
    {
        super();
    }

    public Square(double side)
    {
        super(side, side);
        //super.setWidth(side);
        //super.setLength(side);
    }

    public Square(double side, String color, boolean filled)
    {
        super(side, side, color, filled);
        //super(.setWidth(side);
        //super.setLength(side);
        //super.setColor(color);
        //super.setFilled(filled);
    }

    public double getSide()
    {
        return super.getLength() == super.getWidth() ? super.getLength() : 0.0;
    }

    public void setSide(double side)
    {
        super.setWidth(side);
        super.setLength(side);
    }

    public void setWidth(double side)
    {
        super.setWidth(side);
        super.setLength(side);
    }

    public void setLength(double side)
    {
        super.setWidth(side);
        super.setLength(side);
    }

    @Override
    public String toString()
    {
        return "A square with side: " + getSide() + ", which is a subclass of " + super.toString();
    }
}