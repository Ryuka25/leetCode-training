<?php 

class Membre {
    
    // Propriétés de la class Membre:

    private $_pseudo;
    private $_email;
    private $_signature;
    private $_status = "actif";

    // Méthodes de la class Membre:

    /* Les getters servent à récuper des variables */
    public function getPseudo() {
        return $this->_pseudo;
    }

    /* Les setters servent à mettre à jours les valeurs des variables */
    public function setPseudo($newPseudo) {
        if (!empty($newPseudo) AND strlen($newPseudo)<15) {
            $this->_pseudo = $newPseudo;
        }
    }

    public function sendMail($mail) {
        $title = $mail['title'];
        $message = $mail['message'];

        print("\nEmail envoyer");
        // mail($this->_email, $title, $message);
    }

    public function ban() {
        
        $mail = [
            'title'=>"You have been kicked",
            'message'=>"You have been kicked from the server!" 
        ];

        if ($this->_status) {
            $this->_status = "banned";
        }
        print("\nStatus changée");
        $this->sendMail($mail);
    }

    public function getStatus() {
        $status =  "\nStatus : ".$this->_status;
        return $status;
    }
}

function main(){

    $membre = new Membre();

    $membre->setPseudo("RYUKA");
    
    print($membre->getPseudo());
    
    print($membre->getStatus());
    
    $membre->ban();
    
    print($membre->getStatus());

    return 0;

}

main();
