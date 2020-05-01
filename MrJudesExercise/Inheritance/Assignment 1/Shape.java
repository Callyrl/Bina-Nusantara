package com.company;

public class Shape
{
    private String color;
    private boolean filled;

    public Shape()
    {
        super();
        this.color = "red";
        this.filled = true;
    }

    public Shape(String color, boolean filled)
    {
        super();
        this.color = color;
        this.filled = filled;
    }

    public String getColor()
    {
        return this.color;
    }

    public void setColor(String color)
    {
        this.color = color;
    }

    public boolean isFilled()
    {
        return this.filled;
    }

    public void setFilled(boolean filled)
    {
        this.filled = filled;
    }

    @Override
    public String toString()
    {
        if (!isFilled())
        {
            return "A shape with a colour of " + this.getColor() + " and Not filled";
        }

        else
        {
            return "A shape with a colour of " + this.getColor() + " and filled";
        }
    }
}
