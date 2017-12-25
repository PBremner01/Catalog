    Purpose: Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

    Notes: This project was build off the UD330 files.
Used Libraries: 
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash 
from sqlalchemy import create_engine, asc 
from sqlalchemy.orm import sessionmaker 
from cdatabase_setup import Base, Catalog, CItem, User 
from flask import session as login_session 
import random 
import string 
from oauth2client.client import flow_from_clientsecrets 
from oauth2client.client import FlowExchangeError 
import httplib2 
import json 
from flask import make_response 
import requests

To run: 
1. Place file in choosen directory. 
2. In the Vagrant vitual box ( running ) run : python catalogload2.py - creates and loads the Catalog.db 
3. execute python application:8000 
4. in browser enter url localhost:8000

Notes: 
1. On inital startup you can view the files 
2. Login and you can only view the previously created records 
3. Select the “Create Catalog” button to create a new Category 
4. Click on your newly created Category and select the “Edit Catalog” or “Add Item” buttons on botton. 
5. To Edit an Item or Delete an Item, click on it. Button options are supplied in the new page. 
6. JSON presentation options are presented with: 
localhost:8000/Catalogs/JSON 
localhost:8000/Catalog/[Catalog ID/item/JSON

