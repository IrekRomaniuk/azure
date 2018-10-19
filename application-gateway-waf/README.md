# Create Application Gateway with enabled Web Application Firewall

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F101-application-gateway-waf%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F101-application-gateway-waf%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

This template deploys an Application Gateway with Web Application Firewall functionality in a virtual network. 
##### deploy.json and parameters.json downloaded from sucesfull deployment

```
az group create --name AppG --location eastus

az network vnet create \
  --name AGVNet \
  --resource-group AppG \
  --location eastus \
  --address-prefix 10.100.0.0/16 \
  --subnet-name AGBackendSubnet \
  --subnet-prefix 10.100.1.0/24

az network vnet subnet create \
  --name AGSubnet \
  --resource-group AppG \
  --vnet-name AGVNet \
  --address-prefix 10.100.2.0/24

az network public-ip create \
  --resource-group AppG \
  --name AGPublicIPAddress

az network application-gateway create \
  --name AppGateway \
  --location eastus \
  --resource-group AppG \
  --vnet-name AGVNet \
  --subnet AGSubnet \
  --capacity 2 \
  --sku WAF_Medium \
  --http-settings-cookie-based-affinity Disabled \
  --frontend-port 80 \
  --http-settings-port 80 \
  --http-settings-protocol Http \
  --public-ip-address AGPublicIPAddress

az network application-gateway waf-config set \
  --enabled true \
  --gateway-name myAppGateway \
  --resource-group AppG \
  --firewall-mode Detection \
  --rule-set-version 3.0
```
