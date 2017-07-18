<?php
header("Content-Type:text/html;charset=utf8");
function encrypt($data,$key)
{
    $key = md5('ISCC');
    $x = 0;
    $len = strlen($data);
    $klen = strlen($key);
    for ($i=0; $i < $len; $i++) { 
        if ($x == $klen)
        {
            $x = 0;
        }
        $char .= $key[$x];
        $x+=1;
    }
    for ($i=0; $i < $len; $i++) {
        $str .= chr((ord($data[$i]) + ord($char[$i])) % 128);
    }
    return base64_encode($str);
}

function decrypt($data, $key) 
{ 
 $key = md5($key); 
    $x = 0; 
    $data = base64_decode($data); 
    $len = strlen($data); 
    $l = strlen($key); 
    for ($i = 0; $i < $len; $i++) 
    { 
        if ($x == $l) 
        { 
         $x = 0; 
        } 
        $char .= substr($key, $x, 1); 
        $x++; 
    } 
    for ($i = 0; $i < $len; $i++) 
    { 
        if (ord(substr($data, $i, 1)) < ord(substr($char, $i, 1))) 
        { 
            $str .= chr((ord(substr($data, $i, 1)) + 128) - ord(substr($char, $i, 1))); 
        } 
        else 
        { 
            $str .= chr(ord(substr($data, $i, 1)) - ord(substr($char, $i, 1))); 
        } 
    } 
    return $str; 
} 
$data = "fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA=";
$key="ISCC";
$decrypt = decrypt($data,$key);
echo $decrypt;

?>
