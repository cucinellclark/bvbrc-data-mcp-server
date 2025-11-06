last edit: 10/16/2025
# Getting Started
follow the README instructions in the BV-BRC Data MCP Server
The MCP server should be running. Take note of the port where you are running it
The server.py script must be running your MCP server in order to connect to ChatGTP.

## Connecting your MCP server to ChatGTP
Click the plus next to 'ask my anything'
    Click 'add sources'
Now you should see 'Sources' and 'Add' below your chat box.

Click the down arrow next to 'Add'
    Click 'connect more'
Scroll down to Advanced Settings
    Click the toggle next to Developer Mode. Must be "on"
Click Back

In the upper right hand corner, click "Create"

Icon is optional.
Fill in the Name and Description
The MCP Server URL is relient uppon the port you selected in your config

At present, OAuth will not work. Click the dropdown box and select "No Authentication"

Then click the check box if you Trust this application and click create.

Now you should be able to see "Enabled apps & connectors"
 
Select your server by clicking "Connect"

If you click on the test server, you will see Information and Actions. 

Actions lists the functions defined in the tools/scripts brought in by your sever scritpt.  


Note: For now.... when writing a query mention the action you are testing
