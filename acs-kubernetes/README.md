# Azure Container Service

See https://docs.microsoft.com/en-us/azure/container-service/container-service-kubernetes-walkthrough. 

[<img src="http://azuredeploy.net/deploybutton.png"/>](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FIrekRomaniuk%2Fazure%2Fmaster%2Facs-kubernetes%2Fazuredeploy.json)

```
{"code":"DeploymentFailed","message":"At least one resource deployment operation failed. Please list deployment operations for details. 
Please see https://aka.ms/arm-debug for usage details.","details":[{"code":"BadRequest","message":"{\r\n \"error\": {\r\n \"code\": \"BadRequest\",\r\n 
\"message\": \"The Service Principal in ServicePrincipalProfile could not be validated. Please see https://aka.ms/acs-sp-help for more details. 
(The client '' with object id '' does not have authorization to perform action 'Microsoft.Authorization/roleAssignments/read' over scope
 '/subscriptions/c7084809-7044-42f7-8d2e-2fb121098957/resourceGroups/kube-lab/providers/Microsoft.Authorization'.)\"\r\n }\r\n}"}]}
```
##### deploy.json and parameters.json downloaded from sucesfull deployment. ssh key and clientID to be moved to parameters

```
az group create -n kube-lab -l eastus
az aks create -g kube-lab -n aks-cluster -l eastus --node-count 1 --node-vm-size Standard_D8s_v3 --verbose --generate-ssh-keys --service-principal xxx --client-secret xxx
```

##### acrniuk.azurecr.io