package Geometry;

public class Rectangle {
    private static final String type = "Rectangle";
    private int largeur,longeur;

    /** Creates a new instance of Rectangle */
    public Rectangle(int largeur, int longeur) {
        System.out.println("Constructeur " + type);
        this.largeur = largeur;
        this.longeur = longeur;
    }

    public int perimetre() {return (largeur+longeur)*2 ;}
    public int surface() {return (largeur*longeur);}
}