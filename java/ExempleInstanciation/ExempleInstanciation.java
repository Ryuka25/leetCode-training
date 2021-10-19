public class ExempleInstanciation {
    // point d'entree
    public static void main(String[] args) {
        Test t1 = new Test();
        Test t2 = new Test(3);

        t1.doubleNB();
        t2.doubleNB();

        Test.alpha++;

        System.out.println(t1.toString());
        System.out.println(t2.toString());
    }
}