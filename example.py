from digilock_remote import Digilock_UI

ip = "192.168.10.3" # example ip address
port = 60001 # Digilock User Interface (DUI) 01

dui = Digilock_UI(ip, port)

# For command syntax look in the offical Digilock RCI manual

switch_state = dui.query_bool('pid2:lock:enable') # get current lock switch state
dui.set_bool('pid2:lock:enable', not switch_state) # toggle it to show that the command is working

setpt = dui.query_numeric('pid2:setpoint') # get current setpoint for pid2
dui.set_numeric('pid2:setpoint', setpt + 1) # increment it to show that the command is working

ch1, ch2 = dui.query_graph('scope:graph') # returns two arrays
print(f"ch1 scope trace type: {type(ch1)}")

# There are also enum and range type commands built into the digilock UI module. Source code is self explanatory.
 


