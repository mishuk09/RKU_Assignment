package Java.Exprement_three;

import java.util.*;

class car{
    void spreed() {
        System.out.println("Hello");

    }

}

class maruti extends car {
    void gear() {
        System.out.println("Hello");
    }

}

class maruti800 extends maruti {
    void getmodel() {
        System.out.println("Hasan");
    }

}

class main {
    public static void main(String args[]) {
        car c = new car();
        c.getClass();
    }
}