#these are important imports for the flask app and the socketio hosting a web server 
from flask import Flask, render_template, request, session, redirect 
from flask_socketio import join_room, leave_room, send, SocketIO 
import random 
from string import ascii_uppercase 

#this creates a flask app and it also sets a secert key for the flask app using the config function 
app = Flask(__name__)
app.config["SECRET_KEY"] = "kfjsklfjsk"

#this creates a variable referencing  the flask application wrapping it with Socket.IO for real time communication with server and clients 
socketio = SocketIO(app)

#this is the base home root for the flask app and has the methods of POST and GET to allow for retreiving the home page and also sending the data when you interact with the chat 
@app.route("/", methods = ["POST", "GET"])
def home():
    #when the browser talks to a website it uses different methods. The Post is for sending data to the server from the website 
    if request.method == "POST" :
        #These lines pull out the information that the user inputted for the name and the code. 
        name = request.form.get("name")
        code = request.form.get("code")
        #This gets the information from the button pressed to see if it was check and if it was not check it would return false instead of None with the addition of ,False
        join = request.form.get("join", False)
        create = request.form.get("create", False)
        #if the name is not inputted then it will turn it into a web page to send to the user browser with a variable named error to the home.html file
        if not name: 
            return render_template("home.html", error= "Please enter a name ")

    #this is the connection from the backend to the front end to output the HTML/javascript front end of the website. 
    return render_template("home.html")

#this makes sure that the server is starting if you are running it directly in the Python file 
if __name__ == "__main__" :
    socketio.run(app, debug=True)