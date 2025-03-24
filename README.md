# HomeWizard-Battery-plugin
A Python plugin for Domoticz that creates several devices for the HomeWizard Battery.  

The plugin configuration requires the ip of the battery and a token.  
A token is created on the battery using the `activate_user.py` script. 
The script initiates the token generation protocol as described in https://api-documentation.homewizard.com/docs/v2/authorization.  
To run it provide the ip of the battery and an username as an argument.  
It asks the user to press enter after the battery has been put in token generation mode, by touching the button above the LED array on the battery.
When a token is acquired the script prints the token returned as well as device and user information.

The ip of the battery (and p1) device can be found by running the `detect.py` script. 
It should print all HomeWizard devices which comply to the V2 API, as well as their ip address.

![Devices](devices.png)

Thanks to gettevan for https://github.com/gettevan/HomeWizard-Wifi-p1-plugin which served as the basis for this plugin.
