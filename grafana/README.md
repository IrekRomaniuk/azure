```
az keyvault secret show --name 'azureuser' --vault-name 'keyniuk'

rg=grafana

dir=$(pwd)
template=$dir/template.json
parms=$dir/parameters.json

az group create --name $rg --location eastus

job=job.$(date --utc +"%Y%m%d.%H%M%S")

az group deployment create --parameters "@$parms" --parameters sshPassword='' grafanaAdminPassword='' --template-file $template --resource-group $rg --name $job --no-wait
Azure Error: InvalidTemplate
Message: Deployment template validation failed: 'The resource 'Microsoft.Storage/storageAccounts/niukgrafanastorage' is not defined in the template. Please see https://aka.ms/arm-template for usage details.'.
```


