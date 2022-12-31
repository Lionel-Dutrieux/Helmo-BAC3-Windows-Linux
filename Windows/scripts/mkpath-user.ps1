function createUserFolders {
    param(
        [Parameter(Mandatory = $true)] [string] $departement,
        [Parameter(Mandatory = $true)] [string] $login
    )

    createFolder "C:\CGData\$departement"
    createFolder "C:\CGData\$departement\$login"
    createFolder "C:\CGData\$departement\$login\netprofile.V6"

    $acl = Get-ACL -Path "C:\CGData\$departement"
    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("CG24DOM\cat$departement", "Read", "None", "None", "Allow")
    $acl.SetAccessRule($rule)
    Set-Acl -Path "C:\CGData\$departement" $acl

    $acl2 = Get-ACL -Path "C:\CGData\$departement\$login"
    $rule2 = New-Object System.Security.AccessControl.FileSystemAccessRule("CG24DOM\$login", "Modify", "ContainerInherit,ObjectInherit", "None", "Allow")
    $acl2.SetAccessRule($rule2)
    Set-Acl -Path "C:\CGData\$departement\$login" $acl2

    Set-AdUser -Identity $login -ProfilePath "\\WIN22-AD-REVISI\CGData\$departement\$login\netprofile" -HomeDirectory "\\WIN22-AD-REVISI\CGData\$departement\$login" -HomeDrive "P:"
}

function createFolder {
    param (
        [Parameter(Mandatory = $true)] [string] $path
    )

    if (Test-Path -Path $path) {
    }
    else {
        $null = New-Item -ItemType "directory" -Path $path
    }
    
}

$csv = Import-Csv -Path .\liste-users-login-pass.csv -Delimiter ';'

foreach ($user in $csv) {
    createUserFolders $user.Categorie $user.Login
}