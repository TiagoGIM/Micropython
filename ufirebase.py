#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este script implementa metodos put, get e delete para atualizar dados no google firebase diretamente do dispositivo IoT (nodeMcu8266)
"""
import urequests
import json

class uFirebase:
    kind = 'put, get, delete, path'         
    def __init__(self, firebase, auth = None):
        """
        my_app = your app's name in firebase
        firebase = https://my_app.firebaseio.com/
        auth =  Token_access or Secret database
        """
        self.firebase = firebase
        self.auth = auth 

    def put(self,path,myData):
        """
        this method put in a branch a Mydata. if a branch not exist, 
        it will be creat.        
        myData = {key :value}
        path  = 'branch/'
        """
        if self.auth is None:
            try:
                response = urequests.put(self.firebase+path+'.json', data = json.dumps(myData))
                print("try send")
            except:
                print("put sem auth bugou")
        else:
            try:
                url = self.firebase+path+'.json?auth='+self.auth
                print (url, type(url))
                print (myData)
                response = urequests.put(url, data = json.dumps(myData))
                print("try send")
            except:
                print("put com auth bugou")

        try:
            response.close()
        except:
            print("close bugou")

    def patch(self,path,myData):
        """
        this method put in a branch a Mydata just if a branch exist.
        myData = {key :value}
        path  = 'branch/'
        """
        if self.auth is None:
            try:
                response = urequests.patch(self.firebase+path+'.json', data = json.dumps(myData))
            except:
                print("erro")
        else:
            try:
                url = self.firebase+path+'.json?auth='+self.auth
                response = urequests.patch(url, data = json.dumps(myData))
            except:
                print("erro")
        try:
            response.close()
        except:
            print("erro")

    def get(self,path):
        if self.auth is None:
            try:
                url = self.firebase+path+'.json?print=pretty'
                response = urequests.get(url).json()
                return response
            except:
                print("erro")
        else:
            try:
                url =self.firebase+path+'.json?auth='+self.auth
                response = urequests.get(url).json()
                return response
            except:
                print("erro")

    def delete(self,path):
        if self.auth is None:
            try:
                url = self.firebase+path+'.json?print=pretty'
                response = urequests.delete(url).json()
                return response
            except:
                print("erro")
        else:
            try:
                url =self.firebase+path+'.json?auth='+self.auth
                response = urequests.delete(url)
                return response
            except:
                print("erro")
        




