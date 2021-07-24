public class MyProgram {

    public static void myCoolMethod() {
        System.out.println("Done")
    }

    public static void myCoolMethod() {
        System.out.println("Done2")
    }

    // entry point!
    public static void main(String[] args) {
        myCoolMethod()
        myCoolMethod2()
    }

    public static typeExample() {
        int x = 10;
        x = 10.5; // ERROR!
        float y = 10.5;
    }

    public static String for_test(String letter, int times) {
        String result = "";
        for(int i = 0; i < times; i++) {}
            result += letter;
        }
        return result;
    }



    public static int if_test(int value, int value2) {
        int rtn = 0; // going to be -1, 0, 1
        if(value < value2) {
            rtn = -1;
        }
        else if(value > value2) {
           rtn = 1;
        }
        return rtn; // else assumed by 0
    }



}


