
# **Deploy a two-tiered application environment secured by the VM-Series firewall (VPN added)**

This ARM template deploys a VM-Series next generation firewall VM in an Azure resource group along with a web and db server similar to a typical two tier architecture. It also adds the relevant User-Defined Route (UDR) tables to send all traffic through the VM-Series firewall.

![alt_text](azure-topology.png?raw=true)

# <a href="https://github.com/PaloAltoNetworks/azure/blob/master/two-tier-sample/Azure_ARM_template_deployment_guide.pdf">Deployment Guide</a> 



[<img src="http://azuredeploy.net/deploybutton.png"/>](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FIrekRomaniuk%2Fazure%2Fmaster%2Ftwo-tier-sample%2FazureDeploy.json)

[<img src="https://camo.githubusercontent.com/536ab4f9bc823c2e0ce72fb610aafda57d8c6c12/687474703a2f2f61726d76697a2e696f2f76697375616c697a65627574746f6e2e706e67" data-canonical-src="http://armviz.io/visualizebutton.png" style="max-width:100%;">](https://raw.githubusercontent.com/IrekRomaniuk/azure/master/two-tier-sample/azureDeploy.json)

<br/>

### Addresses

- webserver-vm 10.x.3.5
- database-vm  10.x.4.5
