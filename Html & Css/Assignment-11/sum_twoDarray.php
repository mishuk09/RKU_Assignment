<?php 
echo "Run by computerpathsala.com <br/>";
$a1=array(array(6,2),array(11,3));
$a2=array(array(5,3),array(4,3));
for($i=0; $i<=1; $i++) 
{
    for($j=0; $j<=1; $j++) 
    {
	$result[$i][$j] = $a1[$i][$j] + $a2[$i][$j];
    }
}
echo "Addtion of 2d Matrices is:<br>";
//for print output 
for($i=0; $i<=1; $i++) 
{
    for($j=0; $j<=1; $j++) 
    {
	echo $result[$i][$j];
	echo "\t";
    }
    echo "<br/>";
}
/* another way to print array
echo "Addtion of 2d array is: ";print_r($result);
*/
?>