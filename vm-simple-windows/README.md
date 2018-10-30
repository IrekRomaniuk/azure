# Very simple deployment of a Windows VM

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F101-vm-simple-windows%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F101-vm-simple-windows%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

This template allows you to deploy a simple Windows VM using a few different options for the Windows version, using the latest patched version. This will deploy a A2 size VM in the resource group location and return the fully qualified domain name of the VM.

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
