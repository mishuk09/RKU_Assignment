
// 1. Program to Print an Integer (Entered by the User)

/*package Java.Exprement_1;

import java.util.Scanner;

public class exprement_01 {

    public static void main(String args[]) {
        System.out.print("Enter number:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        System.out.println(num);

    }

}


*/

// 2.  Write a Program to print the area of triangle. 

/*package Java.Exprement_1;
 

public class exprement_01 {

    public static void main(String args[]) {
      
        double  height=4;
        double width=5;

        double are = 0.5 * height * width;

        System.out.println(are);

    }

}


*/

// 3.Program to Check Whether an Alphabet is Vowel or Consonant

/*  
package Java.Exprement_1;

import java.util.*;

public class exprement_01 {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        char ch= sc.next().charAt(0);

        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            System.out.println("Your char is Voil");

        } else {
            System.out.println("Ypur char is consonent");
        }

    }

}
*/

// 4...Program to Find ASCII Value of a character

/* 

package Java.Exprement_1;

import java.util.*;

public class exprement_01 {

   public static void main(String args[]){
     char ch='A';
     int ASCII=ch;
     System.out.println(ASCII);

   }
    

}


*/

// 5. Java Program to Display Armstrong Number Between Two Intervals

package Java.Exprement_1;

import java.util.*;

public class exprement_01 {

    public static void main(String args[]) {

        int num = 123;
        int arm = 0;

        if (num > 0) {

            arm = (num * num * num) + arm;

            num = num / 10;
        }

    }

}
