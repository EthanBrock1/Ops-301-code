# Script: Ops 301 Class  Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 
# Purpose: 

    #REQUIREMENTS
# Write a Powershell script that adds the below person to AD.
# Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz's email is ferdi@GlobeXpower.com.

    #DEMO
    # New-ADUser -Name "ChewDavid" -OtherAttributes @{'title'="director";'mail'="chewdavid@fabrikam.com"}


    # Start Code


    # New-ADUser -Name "Franz Ferdinand" -OtherAttributes @{'title'="TSP Reporting Lead";'company'="Globex USA";'office'="Springfield, OR";'department'="TPS Department";'mail'="ferdi@GlobeXpower.com"}
# add new user with information
New-ADUser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Fredinand" -SamAccountName "Franz.F" -UserPrincipalName "fredi@GlobeXpower.com" -AccountPassword (Read-Host -AsSecureString "Input Password") -Enabled $true


  # End Code
