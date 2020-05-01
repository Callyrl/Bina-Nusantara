package com.company;

public class Driver
{
    public static void main(String[] args)
    {
        // Testing Circle Class
        Circle c1 = new Circle();

        System.out.println(c1.toString());


        // Testing Rectangle Class
        Rectangle r1 = new Rectangle(3.0, 5.0, "purple", true);

        System.out.println("\n" + r1.toString());
        System.out.println("Area: " + r1.getArea());
        System.out.println("Perimeter: " + r1.getPerimeter());


        // Testing Square Class
        Square s1 = new Square(5.0, "red", false);

        System.out.println("\n" + s1.toString());

        System.out.println("Area: " + s1.getArea());
        System.out.println("Perimeter:" + s1.getPerimeter());
    }
}
