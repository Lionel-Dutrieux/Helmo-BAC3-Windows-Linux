$quotas1 = @("Administratif", "Social", "Comptabilite", "direction")
$quotas2 = @("Elearning", "Etudiant", "Juridique", "Travaux")
$quotas3 = @("Informatique", "Communication", "Personnel")

foreach ($categorie in $quotas1) {
    $quota = 400 * 1048576 # 400 Mo
    $quotaAlert = 390 * 1048576 # 390 Mo
    &"fsutil" "quota" "modify" "C:" $quotaAlert $quota $("cat$categorie")
    New-FSRMQuota -Path "C:\CGData\$categorie" -Template "Limit400Mo"
}

foreach ($categorie in $quotas2) {
    $quota = 300 * 1048576 # 300 Mo
    $quotaAlert = 290 * 1048576 # 290 Mo
    &"fsutil" "quota" "modify" "C:" $quotaAlert $quota $("cat$categorie")
    New-FSRMQuota -Path "C:\CGData\$categorie" -Template "Limit300Mo"
}

foreach ($categorie in $quotas3) {
    $quota = 800 * 1048576 # 800 Mo
    $quotaAlert = 750 * 1048576 # 750 Mo
    &"fsutil" "quota" "modify" "C:" $quotaAlert $quota $("cat$categorie")
    New-FSRMQuota -Path "C:\CGData\$categorie" -Template "Limit800Mo"
}