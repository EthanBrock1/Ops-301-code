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
# This is all i could get tonight useing the resource linked 
# will work more in the mornin

    # New-ADUser -Name "Franz Ferdinand" -OtherAttributes @{'title'="TSP Reporting Lead";'company'="Globex USA";'office'="Springfield, OR";'department'="TPS Department";'mail'="ferdi@GlobeXpower.com"}

New-ADUser -Company:"GlobeX USA" -Department:"TPS" -DisplayName:"Rita Morgan" -GivenName:"Rita" -Name:"Rita Morgan" -Path:"DC=corp,DC=globexpower,DC=com" -SamAccountName:"rita" -Server:"WIN-VJKN82JHIKH.corp.globexpower.com" -Surname:"Morgan" -Title:"CFO" -Type:"user" -UserPrincipalName:$null
    # End Code
