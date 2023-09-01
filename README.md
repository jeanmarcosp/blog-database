Jeanmarcos Perez
Xenia Dela Cueva

## Lab 4 
Using a mongodb database cluster, pymongo, and python, we created a blog engine. We used a config.ini file and additional functions that would enable the user to automatically access the database (wusing our Atlas username and password). To run the program, we have the following functions:


## Post
Post takes the following format:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;post blogName userName title postBody tags timestamp
This creates an entry to the blog database, which has the following fields:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"userName" - username of the user inputting,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"title" - title of post in blog,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"postBody"- content of blog post,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "tags" - tags related to the post,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"timestamp"- time the post was created,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"permalink": URL of post,
"comments": an embedded document to hold all the comments for the post (including replies to comments). 

We chose to embed the comments since comments only refer to one post (even if they are comments to comments, ultimately commenting on a post) and are based on timestamps/ permalinks. We also referred to CS61 MongoDB- Schema Notes (which approved that Blog comment can be embedded) and was advised by the Professor to embed.  If the blog database is not already made, it is created.

## Comment
Comment takes the following format:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment blogname permalink userName commentBody timestamp
Using the database with the same name as the blogName, a user can post a comment on a post or a comment's post. Since comments are an embedded document, they have the following subfields:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"userName"-  - username of the user inputting,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"permalink" - timestamp of the user that inputted,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"comment"- commentBody

## Delete
Delete takes the following format:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;post blogName userName title postBody tags timestamp
Delete does not delete the post or the comment from the database, but rather updates the postBody or commentBody in comments field to say " deleted by User", as well as the timestamp it was deleted.

## Show
Show takes the following in the format:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show blogName
This would display all the posts and comments for the corresponding blogName database



