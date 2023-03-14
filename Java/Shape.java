 
class Shape {
    void area(){

    }
    void perimeter(){

    }
    // Triangle class implementing Shape
class Triangle extends Shape {
    private double base, height, side1, side2, side3;

    public Triangle(double base, double height, double side1, double side2, double side3) {
        this.base = base;
        this.height = height;
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public void area() {
        double area = (base * height) / 2;
        System.out.println("The area of the triangle is: " + area);
    }

    public void perimeter() {
        double perimeter = side1 + side2 + side3;
        System.out.println("The perimeter of the triangle is: " + perimeter);
    }
}

// Circle class implementing Shape
class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public void area() {
        double area = Math.PI * radius * radius;
        System.out.println("The area of the circle is: " + area);
    }

    public void perimeter() {
        double perimeter = 2 * Math.PI * radius;
        System.out.println("The perimeter of the circle is: " + perimeter);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating a Triangle object and calling the area() and perimeter() methods
        Triangle triangle = new Triangle(4, 5, 3, 4, 5);
        triangle.area();
        triangle.perimeter();

        // Creating a Circle object and calling the area() and perimeter() methods
        Circle circle = new Circle(3);
        circle.area();
        circle.perimeter();
    }
}

}

