# Very simple deployment of a Linux VM

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FIrekRomaniuk%2Fazure%2Fmaster%2Fvm-simple-linux%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FIrekRomaniuk%2azure%2Fmaster%2Fvm-simple-linux%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>


This template allows you to deploy a simple Linux VM using a few different options for the Ubuntu Linux version, using the latest patched version. This will deploy a A1 size VM in the resource group location and return the FQDN of the VM. It is running two scripts: script1.py and script2.sh (second dependent on first). Referencing static IP 'pan-fwPublicIP' created in different resource group 'cloud-shell-storage-eastus'

https://azure.microsoft.com/en-us/blog/automate-linux-vm-customization-tasks-using-customscript-extension/

azuredeploy.last.json:

```
{"code":"DeploymentFailed","message":"At least one resource deployment operation failed. Please list deployment operations for details. Please see https://aka.ms/arm-debug for usage details.","details":[{"code":"BadRequest","message":"{\r\n \"error\": {\r\n \"code\": \"InvalidScheduleId\",\r\n \"message\": \"The schedule should be created in subscription xxx, resource group vmlab and with name shutdown-computevm-ubuntu-vm.\"\r\n }\r\n}"}]}
```

https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-template-deploy-cli

```
az login -u ... -p ...
az group create --name vmlab --location "East US"
az group deployment create \
  --name vmlabDeployment \
  --resource-group vmlab \
  --template-file azuredeploy.json \
  --parameters @azuredeploy.parameters.json \
  --parameters adminPassword=
az vm show \
    --resource-group vmlab \
    --name vmlabDeployment \
    --show-details \
    --query publicIps \
    --output tsv  
az group destroy --name vmlab    
```