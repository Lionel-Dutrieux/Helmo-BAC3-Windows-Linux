[hashtable] $departementCount = @{}

function addDepartement {
    param([string] $departement)
    $departementCount[$departement] = if ($departementCount.ContainsKey($departement)) { $departementCount[$departement] + 1 } else { 1 }
    return [string] $departementCount[$departement]
}

function getLogin {
    param ([string] $departement)
    [string] $login = "$($departement.Substring(0, 1))$($departement.Substring($departement.Length -1))"
    [string] $departementCount = $(addDepartement($departement))
    return $login + $departementCount.padleft(4, '0')
}


$csv = Import-Csv -Path .\liste-users.csv -Delimiter ';'

foreach ($row in $csv) {
    $login = getLogin($row.Categorie)
    $password = if ($departementCount[$row.Categorie] -eq 50) { "P@ssword" } else { &"./generatePassword.ps1" -length 8 -maxNumber 2 -maxUpper 2 }
    $row | Add-Member -NotePropertyName "Login" -NotePropertyValue $login
    $row | Add-Member -NotePropertyName "Password" -NotePropertyValue $password
}

$csv | Export-Csv -Path .\liste-users-login-pass.csv -NoTypeInformation -Delimiter ';'