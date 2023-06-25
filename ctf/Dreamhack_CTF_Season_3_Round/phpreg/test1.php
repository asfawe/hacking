<!DOCTYPE html>
<html>
<body>

<?php
$name = preg_replace("/nyang/i", "", "dnnyangyangnyang0310");
$pw = preg_replace("/\d*\@\d{2,3}(31)+[^0-8]\!/", "d4y0r50ng", "0@0031319!+1+13");

echo $name;
//echo $pw;
if ($name === "dnyang0310" && $pw === "d4y0r50ng+1+13") {
	echo "FLAG";
}
?>

</body>
</html>