<?php
 
$x = 100;
echo "------The prime numbers from 1 to ".$x." are------\n\n";

for ($i = 0; $i < $x; $i++) {
    
     if ($i == 1 || $i == 0)
        continue;
    
    $f = 1;
    
    for ($j = 2; $j < intval($i / 2) + 1; $j++) {
        if ($i % $j == 0) {
            $f = 0;
            break;
        }
    }
    
     if ($f == 1)
        echo $i." ";
}
echo "\n";

?>