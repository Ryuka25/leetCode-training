<?php 

require_once('config.php');
require_once('init.php');

if (!empty($_GET['page'])) {
    
    $page = $_GET['page'];

    generate($page);

} else {
    
    generate('home');

}