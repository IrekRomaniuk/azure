# Add service endpoints to a subnet in a Virtual Network and secure a storage account to 

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F201-vnet-2subnets-service-endpoints-storage-integration%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F201-vnet-2subnets-service-endpoints-storage-integration%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

This template creates a new VNet with 2 subnets, a NIC in each subnet. Enables service endpoint to Storage on one of the subnets and secures a new storage account to that subnet.

```
az keyvault secret show --name 'azureuser' --vault-name 'keyniuk'

rg=lab

dir=$(pwd)
template=$dir/azuredeploy.json
parms=$dir/azuredeploy.parameters.json

az group create --name $rg --location eastus

job=job.$(date --utc +"%Y%m%d.%H%M%S")
az group deployment create --parameters "@$parms" --template-file $template --resource-group $rg --name $job --no-wait
or 

az group deployment create --parameters "@$parms" --parameters param1=param1 param2=param2 --template-file $template --resource-group $rg --name $job --no-wait
```