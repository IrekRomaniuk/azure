
https://docs.microsoft.com/en-us/azure/container-instances/container-instances-vnet

```
az account list-locations
az container create --resource-group vmlab --file vnet-deploy-aci.yaml
Virtual network is not supported in location 'eastus' for container group 'appcontaineryaml'. Please use one of the locations 'EastUS2EUAP,CentralUSEUAP,WestUS,WestCentralUS,NorthEurope,WestEurope'.

```

Try vm-simple-linux with publicIP

```
az group create --name containerlab --location "eastus2"
docker@R90HE73F:/mnt/c/Users/irekromaniuk/azure/vm-simple-linux$ az group deployment create \
>   --name vmlabDeployment \
>   --resource-group containerlab \
>   --template-file azuredeploy.json \
>   --parameters @azuredeploy.parameters.json \
>   --parameters adminPassword=''
Deployment failed. Correlation ID: 9854778f-d3d5-4fb4-8f37-bba35d872b99. {
  "error": {
    "code": "InvalidResourceReference",
    "message": "Resource /subscriptions/c7084809-7044-42f7-8d2e-2fb121098957/resourceGroups/cloud-shell-storage-eastus/providers/Microsoft.Network/publicIPAddresses/lin-vmPublicIP referenced by resource /subscriptions/c7084809-7044-42f7-8d2e-2fb121098957/resourceGroups/containerlab/providers/Microsoft.Network/networkInterfaces/vmNIC was not found. Please make sure that the referenced resource exists, and that both resources are in the same region.",
    "details": []
  }
}
```