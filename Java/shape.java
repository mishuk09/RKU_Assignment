package Java;

public class shape {

    void area() 
    {
         
    }

    void  perimeter()
    {

    }

    public class triangle extends shape{
        
        void result(){
            int re=area();  
            
        }

    }
    public class circle{

    }
    public class rectangle extends shape {

        void draw() {

        }
    }

    public static void main(String[] args) {

        shape s = new shape();
        s.draw();
    }
}
