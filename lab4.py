import pymongo                               #mongodb connector
from pprint import pprint
import datetime
from datetime import date
import shlex
import re
from db_functions import *

server = create_mongo_server()

try:    #initialize server connection
    connection = pymongo.MongoClient(server)

except pymongo.errors.ServerSelectionTimeoutError as err:
    print("Connection failure:")
    print(err)
    
#Connect to my database
db = connection.lab4

inp = input("please enter a command or press \"q\" to quit\n")
inp = shlex.split(inp)

while inp[0].lower() != 'q':

    #post blogName userName title postBody tags timestamp
    if inp[0].lower() == "post":
        blogName = inp[1]
        collection = db[blogName]
        userName = inp[2]
        title = inp[3]
        postBody = inp[4]
        timestamp = inp[6].strip('\"')
        taglist = []
        for tag in inp[5].strip('\"').split(","): taglist.append(tag)
        permalink  = blogName + '.' + re.sub('[^0-9a-zA-Z]+', '_', title)
        
        try:
            blogpost1 ={"userName": userName,
                        "title": title,
                        "postBody": postBody,
                        "tags": taglist,
                        "timestamp": timestamp,
                        "permalink": permalink,
                        "comments": []
                        }
            collection.insert_one(blogpost1)
        
        except Exception as e:
            print("Could not post blog:", type(e), e)


    #comment blogname permalink userName commentBody timestamp
    if inp[0].lower() == "comment":  

        blogName = inp[1]
        collection = db[blogName]
        permalink = inp[2]
        userName = inp[3]
        commentBody = inp[4]
        timestamp = inp[5]

        # check if the permalink is valid: if not, std error
        count1 = collection.count_documents({"permalink": permalink})
        count2 = collection.count_documents({"comments.permalink": permalink})

        if count1 > 0:
            try:
                comment = {"userName": userName,
                           "permalink": timestamp,
                           "comment": commentBody} #permalink based on comment

                collection.update_one({"permalink": permalink},{'$push': {'comments': comment}})

            except Exception as e:
                print("Could not upload comment:", type(e), e)
        
        elif count2 > 0:
            try:
                comment = {"userName": userName,
                            "permalink": timestamp,
                            "comment": commentBody} #permalink based on comment

                collection.update_one({"comments.permalink": permalink},{'$push': {'comments': comment}})

            except Exception as e:
                print("Could not upload comment:", type(e), e)
        else:
            print("unable to upload comment: post/comment does not exist")
        


    #delete blogname permalink userName timestamp
    if inp[0].lower() == "delete":   
        blogName = inp[1]
        collection = db[blogName]
        permalink = inp[2]
        userName = inp[3]
        timestamp = inp[4]

        # check if the permalink is valid: if not, std error
        count1 = collection.count_documents({"permalink": permalink})
        count2 = collection.count_documents({"comments.permalink": permalink})

        if count1 > 0:
            try:
                update_mes = "deleted by " + userName
                query = {"permalink": permalink}
                update = { "$set": { "postBody": update_mes, 
                                    "timestamp": timestamp} }
                collection.update_one(query, update)

            except Exception as e:
                print("Could not delete:", type(e), e)
        
        elif count2 > 0:
            try:
                update_mes = "deleted by " + userName
                #query = {"permalink": permalink}
                #update = { "$set": { "comments.comment": update_mes} }
                #collection.update_one(query, update)

                collection.update_one({"comments.permalink":permalink} , {'$set': {"comments.$.comment": update_mes}})

            except Exception as e:
                print("Could not delete:", type(e), e)
        else:
            print("unable to delete: post/comment does not exist")



    #show blogName
    if inp[0].lower() == "show":   
        blogName = inp[1]
        collection = db[blogName]

        try:
            iter = collection.find({})
            # have to get each post's permalink to get their comments
            for item in iter:
                pprint("- - - -")
                pprint(item)
        except Exception as e:
            print("Error trying to read collection:", type(e), e)

    inp = input("please enter another command or press \"q\" to quit\n")
    inp = shlex.split(inp)

print("Goodbye!")