package Java.Exprement_three;

import java.util.*;

class vehicle {
    void run() {
        System.out.println("Hello JAVA ");

    }
}

class bike extends vehicle {
    void run() {
        System.out.println("Hello JAVA Overriding");

    }
}

class main {
    public static void main(String args[]) {
        vehicle v = new vehicle();
        v.run();
    }
}