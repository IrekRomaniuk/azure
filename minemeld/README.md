Broken, Just follow https://live.paloaltonetworks.com/t5/MineMeld-Articles/Manually-install-MineMeld-on-Ubuntu-Server-14-04/ta-p/98454
See also https://live.paloaltonetworks.com/t5/MineMeld-Articles/Running-MineMeld-on-Microsoft-Azure/ta-p/78730

```
az login -u ... -p ...
az group create --name fwlab --location "East US"
az group deployment create \
  --name fwlabDeployment \
  --resource-group fwlab \
  --template-file template.json \
  --parameters @parameters.json \
  --parameters adminPassword=
az vm show \
    --resource-group fwlab \
    --name fwlabDeployment \
    --show-details \
    --query publicIps \
    --output tsv  
az group deployment show --resource-group fwlab --name fwlabDeployment    
az group delete --name fwlab    
```