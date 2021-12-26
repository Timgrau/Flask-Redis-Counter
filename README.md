This approach automatically connects the database (redis) container with the
application (flask) container. A Network gets created and the redis container and
application container get attached to it.
# Needed
Make sure you have ```make``` and ```sed``` installed on your system to first run the 
container and second to extract the ip address of the running redis container with a 
bash script and insert it into the flask python script that's running on the application side.
Of course docker and docker-compose is needed.
# Reproduce
1. Clone the repository
2. Navigate into the ```database``` folder

   * hit ```make``` to run the redis container
3. Open a new Terminal, navigate into the ```flask``` folder

   * hit ```make``` to run the flask container
4. Open the url in your browser
---
If you decide to destroy the running flask thread by pressing ```Ctrl+c```, you can use the command
```make clean``` in the ```flask``` directory to stop redis and remove the created container, network, images and
also the ip address that got written into to flask script on line 7.  