<?php

abstract class Pet {

    protected $_name;
    protected $_sound;

    public function __construct($data) {
        $this->setName($data['name']);
        $this->_sound = $data['sound'];
    }

    public function getSound() {
        return $this->_sound;
    }

    public function setName($name) {
        $this->_name = $name;
    }
    
    public function getName() {
        return $this->_name;
    }

    public function myMethod(){
        echo "\n".$this->getName().' : '.$this->getSound()." !";
    }
}

class Dog extends Pet {

    public function hug() {
        echo "\nHugging ".$this->getName()." <3";
        return 1;
    }
}

class Cat extends Pet {

    public function give($food) {
        echo "\nGiving $food to ".$this->_name." <3";
        return 1;
    }
}

$dog_1_data = 

$dog_1 = new Dog([
    'name'=>'Pitou',
    'sound'=>'Waouff'
]);
$cat_1 = new Cat([
    'name'=>"Minouchka",
    'sound'=>"Miaouww"
]);

$dog_1->myMethod();
$dog_1->hug();
$cat_1->myMethod();
$cat_1->give("fish");