#!/bin/bash

#deklarasi array compound assignment
distroLinuxDesktop=('Blank0n' 'Ubuntu' 'Debian' 'ArchLinux' 'LinuxMint')
distroLinuxServer=('UbuntuServer' 'Cent0S' 'FedoraSever')

#cara mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}

