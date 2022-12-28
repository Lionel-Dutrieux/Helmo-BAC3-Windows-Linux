
function addUser {

    # e190061 P@ssword Lionel Dutrieux Path(OU)

    param(
        [Parameter(Mandatory = $true)] [string] $name,
        [Parameter(Mandatory = $true)] [string] $password,
        [Parameter(Mandatory = $true)] [string] $givenName,
        [Parameter(Mandatory = $true)] [string] $surname,
        [Parameter(Mandatory = $true)] [string] $path
    )
    
    New-ADUser -Name $name -AccountPassword (ConvertTo-SecureString `
            -AsPlainText $password -Force) -Enabled $true `
        -PasswordNeverExpires $true -CannotChangePassword $true `
        -SamAccountName $name `
        -Path $path -GivenName $givenName `
        -Surname $surname -DisplayName $("$givenName $surname")
}

function createOU {

    param (
        [Parameter(Mandatory = $true)] [string] $path,
        [Parameter(Mandatory = $true)] [string] $name
    )

    if (Get-ADOrganizationalUnit -Filter "Name -like '$name'") {
    }
    else {
        New-ADOrganizationalUnit -Name $name -ProtectedFromAccidentalDeletion $false -Path $path
    }
}

function addSecurityGroup {
    param (
        [Parameter(Mandatory = $true)] [string] $name,
        [Parameter(Mandatory = $true)] [string] $path
    )

    if (Get-ADGroup -Filter "Name -like '$name'") {
    }
    else {
        New-ADGroup -Name $name -samAccountName $name -GroupCategory Security -GroupScope Global -Path $path
    }
}

function addUserToGroup {
    param (
        [Parameter(Mandatory = $true)] [string] $groupPath,
        [Parameter(Mandatory = $true)] [string] $userPath
    )
    
    Add-ADGroupMember $groupPath -Members $userPath
}

function getGroupName {
    param(
        [Parameter(Mandatory = $true)] [string] $name
    )
    return "cat" + $name.substring(0, 1).toupper() + $name.substring(1).tolower()
}

$csv = Import-Csv -Path .\liste-users-login-pass.csv -Delimiter ';'

foreach ($user in $csv) {
    createOU "OU=DomUsers,OU=CGDom,DC=cg24dom,DC=local" $user.Categorie
    addUser $user.Login $user.Password $user.Nom $user.Prenom "OU=$($user.Categorie),OU=DomUsers,OU=CGDom,DC=cg24dom,DC=local"

    $securityGroup = getGroupName $user.Categorie
    addSecurityGroup $securityGroup "OU=DomGroups,OU=CGDom,DC=cg24dom,DC=local"
    addUserToGroup "CN=$securityGroup,OU=DomGroups,OU=CGDom,DC=cg24dom,DC=local" "CN=$($user.Login),OU=$($user.Categorie),OU=DomUsers,OU=CGDom,DC=cg24dom,DC=local"
}