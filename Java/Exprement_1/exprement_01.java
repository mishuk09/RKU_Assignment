
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

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {

//         int num = 153;
//         int arm = 0;
//         int temp = num;

//         if (num > 0) {

//             int lastDigit = num % 10;

//             arm = (lastDigit * lastDigit * lastDigit) + arm;

//             num = num / 10;
//         }

//         System.out.println(arm);
//         if (temp == arm) {
//             System.out.println("Armstrong");
//         } else {
//             System.out.println("Not armstrong");
//         }

//     }

// }

// public class exprement_01 {

// public static void main(String args[]) {
// int num = 153;
// int rev = 0;
// int temp = num;

// while (num > 0) {
// int lastDigit = num % 10;
// rev = (lastDigit * lastDigit * lastDigit) + rev;
// num = num / 10;
// }

// if (temp == rev) {
// System.out.println("Armstrong");
// } else {
// System.out.println("Not armstrong");
// }
// }

// }

// Java Program to Make a Simple Calculator Using switch...case

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {

//         Scanner sc = new Scanner(System.in);
//         int num1 = sc.nextInt();
//         int num2 = sc.nextInt();
//         System.out.println("Enter operator:");
//         char ch = sc.next().charAt(0);

//         switch (ch) {
//             case '+':
//                 System.out.println("Sum of two number is" + " " + (num1 + num2));
//             case '-':
//                 System.out.println("Sum of two number is" + " " + (num1 - num2));
//             case '*':
//                 System.out.println("Sum of two number is" + " " + (num1 * num2));
//             case '/':
//                 System.out.println("Sum of two number is" + " " + (num1 / num2));

//         }

//     }

// }

// Write a java Program to check the number is Prime or not

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {

//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter number:");
//         int num = sc.nextInt();
//         boolean isPrime = true;

//         for (int i = 2; i < num - 1; i++) {
//             if (num % i == 0) {
//                 isPrime = false;
//             }

//         }

//         if (isPrime == true) {
//             System.out.println("Prime number");
//         } else {
//             System.out.println("Not prime number");
//         }

//     }

// }

//Java Program to Calculate Average Using Array

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {

//         int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
//         int sum = 0;

//         for (int i = 0; i < arr.length + 1; i++) {
//             sum += i;

//         }
//         System.out.println(sum);

//     }

// }

// Java Program to Find Largest Element of an Array

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {

//         int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
//         int maxEle = arr[0];

//         for (int i = 0; i < arr.length; i++) {
//             if (arr[i] > maxEle) {
//                 maxEle = arr[i];
//             }

//         }
//         System.out.println(maxEle);

//     }

// }

// 10. Java Program to Add Two Matrix Using Multi-dimensional Arrays

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {
//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter Row and Col: ");
//         int row = sc.nextInt();
//         int col = sc.nextInt();

//         int arr[][] = new int[row][col];

//         System.out.println("Enter Element:");

//         for (int i = 0; i < row; i++) {
//             for (int j = 0; j < col; j++) {
//                 arr[i][j] = sc.nextInt();
//             }

//         }

//         System.out.println("Output");
//         for (int i = 0; i < row; i++) {
//             for (int j = 0; j < col; j++) {

//                 System.out.print(arr[i][j] + " ");
//             }
//             System.out.println();
//         }

//     }
// }

// 17...Java Program to convert char type variables to integer.

// import java.util.*;

// public class exprement_01 {

//     public static void main(String args[]) {

//         char ch = '3';
//         int num = ch - '0';
//         System.out.println(num);

//     }
// }
