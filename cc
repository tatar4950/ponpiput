<?php

$c = 0;

echo "แปลงค่า C เป็น F <br>";
while ($c <= 100) {
    $f = ($c * 1.8) + 32;
    echo $c . " °C = " . $f . " °F<br>";
    $c += 10;
}

echo "<br>เลขคู่ตั้งแต่ 2 ถึง 20 <br>";


$num = 2;

do {
    echo $num . "<br>";
    $num += 2;
} while ($num <= 20);
?>
