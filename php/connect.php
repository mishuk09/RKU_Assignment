<?php

$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$email = $_POST['email'];
$password = $_POST['password'];
$address = $_POST['address'];

//database connection

$conn = new mysqli('localhost','root','','Assignment-06');
if($conn->connect_error){
    die('Connection failed : '.$conn->connect_error);
}
else{
    $stmt = $conn->prepare("insert into resistration(firstName,lastName,email,password,address) value(?,?,?,?,?)");
    $stmt->bind_param("sssss",$firstName,$lastName,$email,$password,$address);
    $stmt->execute();
    echo"resister successfully ....";
    $stmt->close();
    $conn->close();
}



?>