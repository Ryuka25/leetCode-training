Write-Host
"
/*******************************************************************/
/*  ____  _____ ____  __  __ _   _ _____  _  _____ ___ ___  _   _  */
/* |  _ \| ____|  _ \|  \/  | | | |_   _|/ \|_   _|_ _/ _ \| \ | | */
/* | |_) |  _| | |_) | |\/| | | | | | | / _ \ | |  | | | | |  \| | */
/* |  __/| |___|  _ <| |  | | |_| | | |/ ___ \| |  | | |_| | |\  | */
/* |_|   |_____|_| \_\_|  |_|\___/  |_/_/   \_\_| |___\___/|_| \_| */
/*                                                                 */
/*******************************************************************/
"
Write-Host 
"
 ===== [ B E G I N of S C R I P T] =====
"

Write-Host "Ce script permute deux nombres donée par l'utilisateur."

$nombre1 = Read-Host("Entrez le nombre numéro 1 ici ")
$nombre2 = Read-Host("Entrez le nombre numéro 2 ici ")

function permutation {
    <#
        permutation [[-nombre1] <Object>] [[-nombre2] <Object>]
    #>
    param (
        $nombre1,
        $nombre2
    )
    Write-Host "
    Start Process ... Permutation
    "
    Write-Host "Voici les nombres avant permutation:"
    Write-Host "    > nombre1 = $nombre1 et nombre2 = $nombre2"

    Write-Host "Processing Permutation"
    Write-Host "Creating new case for temporaly variable"
    $nombreTemp = $nombre1
    Write-Host "Permuting Number"
    $nombre1 = $nombre2
    $nombre2 = $nombreTemp

    Write-Host "Voici les nombres après permutation:"
    Write-Host "    > nombre1 = $nombre1 et nombre2 = $nombre2"

    Write-Host "
    Process Finished with exit(0) ... Permutation
    "
}

# Call permutation function
permutation $nombre1 $nombre2

Write-Host
"
 ===== [ E N D of S C R I P T ] ===== 
"
