# luasTracker
 A web app to display the next Luas on a small screen.

 I built this app after seeing my friend do something similar. The app is designed to be run on a raspberry pi with a screen. In my setup I leave the raspberry pi running on a countertop by the front door of my apartment. It shows me the latest times for the Luas (Irish tram service) beside my apartment. I built it through a webapp with Flask / Python to gain some exposure to how Flask works. This is an over engineered solution to a very small problem, but experience is experience.

If you would like to use this and change which stop the info is pulled from edit the 'stop' parameter in the request: 

luas_params = {'action': 'forecast', 'encrypt': 'false', 'stop': 'CHA'}

I have plans to make a request url to request a differnt stop.. 