# HomeWizard-Battery-plugin
A Python plugin for Domoticz that creates several devices for the HomeWizard Battery.  

The plugin configuration requires the ip of the battery and a token.  
A token is created on the battery using the `activate_user.py` script. 
The script initiates the token generation protocol as described in https://api-documentation.homewizard.com/docs/v2/authorization.  
To run it provide the ip of the battery and an username as an argument.  
It asks the user to press enter after the battery has been put in token generation mode, by touching the button above the LED array on the battery.
When a token is acquired successfully the script prints the token returned as well as some device and user information.

The ip of the battery (and p1) device can be found by running the `detect.py` script with no command line options.
It should print the type of all HomeWizard devices on your network, along with their ip address. 
Press the enter key to stop the program.

You may want to test the connection. Edit the ip and token in `test.py` and run it, also without command line options.
It should be active for about 2 minutes, while printing the changed state of the battery devices every 10 seconds.

Make sure to run 'pip install -r requirements' before running the above python scripts.

![Devices](devices.png)

Thanks to Eraser3 for https://github.com/Eraser3/HomeWizard-Wifi-p1-plugin which served as the basis for this plugin.
