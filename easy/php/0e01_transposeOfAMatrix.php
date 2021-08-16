<?php
    $a = 1;
    $b = 2;
    $c = 3;
    $d = 4;

    $matrix = array (
        array (1,2),
        array (3,4)
    );

    $transposedMatrix = array (
        # initialization
    );

    $lineMax = count($transposedMatrix);
    $columnMax = count($matrix);

    for ($transposedLineNumber=0; $transposedLineNumber < count($matrix[0]); $transposedLineNumber++) { 
        array_push($transposedMatrix,
                array()
        );
    }

    for ($lineNumber=0; $lineNumber < $lineMax; $lineNumber++) { 
        for ($columnNumber=0; $columnNumber < $columnMax; $columnNumber++) { 
            array_push($transposedMatrix[$lineNumber],
                $matrix[$columnNumber][$lineNumber]
            );
        }   
    }

    for ($i=0; $i < count($matrix); $i++) { 
        for ($j=0; $j < count($matrix[$i]); $j++) { 
            echo $matrix[$i][$j];
        }
        echo "<br/>";
    }

    for ($i=0; $i < $lineMax; $i++) { 
        for ($j=0; $j < $columnMax; $j++) { 
            echo $transposedMatrix[$i][$j];
        }
        echo "<br/>";
    }

    
?>