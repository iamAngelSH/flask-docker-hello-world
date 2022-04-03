# Fun Flask App on a Docker container

This is a very simple and generic Flask App that uses GET and Post methods. It also uses a fun API. 

<hr>

## How to use:



1. Clone this [repository](https://github.com/iamAngelSH/flask-docker-hello-world) to a directory of your choice on your terminal.
  - Command to clone:
  ```git
  git clone https://github.com/iamAngelSH/flask-docker-hello-world
  ```
2. Step in the repository directory
  - Change Direcotry
  ```terminal
  cd flask-docker-hello-world
  ```
3. Here you should have all the contents you need.
4. Having Docker running already on your computer, we can get started with the FLask App.
5. Let's build the image
  - Run docker-compose up in the same directory you are in
  ```docker
  docker-compose up
  ```
  
**THESE NEXT STEPS IS TO USE THE FLASK APP ON THE WEB 🕸️**
   - If you want to skip the web browser part, [SKIP TO THIS SECTION](#running-a-program-to-hit-each-of-our-flask-app-routes-without-looking-at-the-web-browser)
6. Open a web browser
  - Once the image is the done building you should get the following link:
    - http://172.24.0.2:5000
  - However, we will not be using that!
    - Since port 5000 is for the server running on the docker container, we need to use the port running on our local machine.
    - Use the following:
      - http://localhost:5555
7. Congrats 🥳 Flask App is up and running. You will see a menu on your web browser with what you can on this Flask App.

<hr>

## Running a program to hit each of our flask app routes without looking at the web browser
Although we do have our flask app running, it is always good to test our routes and make sure they work appropriately.

1. Having your flask docker container still running, open a new terminal.
  - Change into the directory that you have the repository (Flask Project) stored in.
    - Change into the repository directory
  ```terminal
  cd ~Path_to_repo
  ```
2. Once you are in the reposiotry directory, we run another docker-compose command
  - This command will let us execute a python script to test the routes in our flask app and should return values via the terminal.
  ```terminal
  docker-compose exec web python make-requests.py
  ```
3. Once you run this command, you should see 3 different results.
```terminal
pong!  --- STATUS CODE 200
EDIFNOC  --- STATUS CODE 200
4  --- STATUS CODE 200
```
- We can see the output that should be shown in our flask app and also the status code to make sure everything is running ok.

<hr>

