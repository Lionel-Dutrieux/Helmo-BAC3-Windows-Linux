200..250 | ForEach-Object {
    $ip = "192.168.190.$_"
    $name = "ip-192-168-190-$_"

    Add-DnsServerResourceRecordA -Name $name -zonename "dutrieux.local" -IPv4Address $ip
    Add-DnsServerResourceRecordPtr -Name "$_" -PtrDomainName "$name.dutrieux.local" -ZoneName "190.168.192.in-addr.arpa"
}