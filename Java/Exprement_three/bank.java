package Java.Exprement-03;

public class bank {
    void getinterestRate() {
        System.out.println("Main Bank");

    }

}

class ICICI extends bank {
    void getinterestRate() {
        System.out.println("icic bank");
    }

}

class SBI extends ICICI {
    void getinterestRate() {
        System.out.println("sbi bank");
    }

}

class BOB extends SBI {
    void getinterestRate() {
        System.out.println("bob bank");
    }

}

class main {
    public static void main(String args[]) {
        bank mainbank = new bank();
        ICICI icicibank = new ICICI();
        SBI sbibank = new SBI();
        BOB bobbank = new BOB();
        mainbank.getinterestRate();
        icicibank.getinterestRate();
        sbibank.getinterestRate();
        bobbank.getinterestRate();
    }
}