package com.company;

public class Driver
{
    public static void main(String[] args)
    {
        Vehicle[] arrayOfVehicles = new Vehicle[4];

        // Testing Jeep Class
        arrayOfVehicles[0] = new Jeep("Ranger", 5, 300, 4);

        System.out.println(arrayOfVehicles[0].toString());
        Jeep j1 = (Jeep) arrayOfVehicles[0];
        j1.drive();
        j1.soundHorn();

        // Testing Hovercraft Class
        arrayOfVehicles[1] = new Hovercraft("Wings", 1, 100, 0, 1000);

        System.out.println("\n" + arrayOfVehicles[1].toString());
        Hovercraft h1 = (Hovercraft) arrayOfVehicles[1];
        h1.enterSea();
        h1.enterLand();

        // Testing Frigate Class
        arrayOfVehicles[2] = new Frigate("Apache", 500, 300, 100000);

        System.out.println("\n" + arrayOfVehicles[2].toString());
        Frigate f1 = (Frigate) arrayOfVehicles[2];
        f1.launch();
        f1.fireGun();

        // Testing Police Car
        arrayOfVehicles[3] = new PoliceCar("JPD", 4, 500, 4);

        System.out.println("\n" + arrayOfVehicles[3].toString());
        PoliceCar p1 = (PoliceCar) arrayOfVehicles[3];
        p1.drive();
        p1.lights();
        p1.mic();

        IsEmergency e1 = (IsEmergency) arrayOfVehicles[3];
        e1.soundSiren();

        //----------------------------------------------------------------------------------------------------------//
        /* Printing out the common methods only
        for (int i=0; i<arrayOfVehicles.length; i++)
        {
            // Common method for all & Printing each
            System.out.println("\n" + arrayOfVehicles[i].getName());

            // Testing IsLandVehicle Class
            if (arrayOfVehicles[i] instanceof IsLandVehicle)
            {
                IsLandVehicle lv = (IsLandVehicle) arrayOfVehicles[i];
                lv.drive();
            }

            // Testing IsSeaVessel Class
            else
            {
                IsSeaVessel sv = (IsSeaVessel) arrayOfVehicles[i];
                sv.launch();
            }
        }
         */
    }
}
