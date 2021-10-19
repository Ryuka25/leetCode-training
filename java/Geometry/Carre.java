package Geometry;

public class Carre extends Rectangle {
    private static final String type = "Carré";

    /** Constructeur */
    public Carre(int cote) {
        super(cote,cote);
        System.out.println("Constructeur " + type);
    }
}