import web
import shelve
import os
import sys
import customport
import requests as r
import re
from requests.auth import HTTPBasicAuth
import base64

urls = (
    '/register', 'newuser',
    '/', 'login'
)
class login:
    def GET(self):
        print("Entered auth")
        try:
            auth = web.ctx.env.get('HTTP_AUTHORIZATION')
            auth = re.sub('^Basic','',auth)
            print("reached auth")
            (name,passwrd) = base64.decodestring(auth.encode()).decode().split(':')
            print("name: ",name)
            adb = shelve.open('auth_db')
            pass1 = adb[name]
        except KeyError as err:
            error = "Cannot find the user. Please check username"
            return error
        finally:
            adb.close()
        if pass1 == passwrd:
            return "login success"
        else:
            return "Username or Password is wrong"

class newuser:
    def GET(self):
        username = input("Enter the username: ")
        password1 = input("Enter the password: ")
        password2 = input("please reenter the password: ")
        if (password1==password2):
            try:
                adb = shelve.open('auth_db')
                adb[username] = password1
            finally:
                adb.close()
            return "New user registered!"
        else:
            print ("Please enter correct password!!")


if __name__ == "__main__":
    app = customport.customport(urls, globals())
    app.run(port=8184)
