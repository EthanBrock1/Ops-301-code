# Script: Ops 201 Class 09 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 16FEB2023
# Purpose: add user 

# This is all i could get tonight useing the resource linked 
# will work more in the mornin

New-ADUser -Name "Franz Ferdinand" -OtherAttributes @{'title'="TSP Reporting Lead";'company'="Globex USA";'office'="Springfield, OR";'department'="TPS Department";'mail'="ferdi@GlobeXpower.com"}

