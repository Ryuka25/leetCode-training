public class Test {
    // Attribut de classe
    private int nb=5;
    public static int alpha = 10;

    // Constructeur
    public Test() {
        System.out.println("Constructeur  1");
        System.out.println("number = " + nb);   
    }

    public Test(int initial_nb) {
        System.out.println("Constructeur 2");
        System.out.println("number = " + nb);
        this.nb= initial_nb;
        System.out.println("number = " + nb);
    }

    // methodes
    public void augmenteNB(){nb++;}
    public void augmenteNB(int newNb){nb+=newNb;}
    public void doubleNB(){nb<<=1;}
    public String toString() {return "number = "+ nb +", alpha = "+ alpha;}
}