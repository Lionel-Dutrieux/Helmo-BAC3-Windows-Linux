param ([int] $length = 8, [int] $maxNumber = 2, [int] $maxUpper = 2)

if ($length -le 0) {
    Write-Error "Parameters error (length)"
    exit
}

if ($maxNumber -lt 0 -or $length -lt $maxNumber) {
    Write-Error "Parameters error (maxNumber)"
    exit
}

if ($maxUpper -lt 0 -or $length -lt $maxUpper) {
    Write-Error "Parameters error (maxUpper)"
    exit
}

$maxLower = $($length - $maxNumber - $maxUpper)


if ($length -lt $($maxNumber + $maxUpper)) {
    Write-Error "Parameters error (length < all)"
    exit
}

[array] $chars = "abcdefghijklmnopqrstuvwxyz".ToCharArray()
[array] $charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray()
[array] $password = ""


for ($i = 0; $i -lt $maxNumber; $i++) {
    $password += $(Get-Random -Minimum 0 -Maximum 10)
}

for ($i = 0; $i -lt $maxUpper; $i++) {
    $password += $($charsUpper | Get-Random)
}

for ($i = 0; $i -lt $maxLower; $i++) {
    $password += $($chars | Get-Random)
}

Write-Output $( -join ($password | Sort-Object { Get-Random }))