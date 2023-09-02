# Blog Database Documentation

Authors:
- Jeanmarcos Perez
- Xenia Dela Cueva

## Lab 4

In this lab, we created a blog engine using a MongoDB database cluster, PyMongo, and Python. We also utilized a `config.ini` file and additional functions that enable users to access the database automatically using our Atlas username and password. To run the program, we provide the following functions:

### Post

The `Post` function takes the following format: `post blogName userName title postBody tags timestamp`

The `Post` function creates an entry in the blog database with the following fields:

- "userName" - Username of the user inputting.
- "title" - Title of the post in the blog.
- "postBody" - Content of the blog post.
- "tags" - Tags related to the post.
- "timestamp" - Time the post was created.
- "permalink" - URL of the post.
- "comments" - An embedded document to hold all the comments for the post (including replies to comments).

We chose to embed comments since comments only refer to one post and are based on timestamps/permakinks. We also referred to CS61 MongoDB Schema Notes, which approved that blog comments can be embedded, and we were advised by the Professor to embed them. If the blog database is not already created, it will be created.

### Comment

The `Comment` function takes the following format: `comment blogname permalink userName commentBody timestamp`

Using the database with the same name as the `blogName`, a user can post a comment on a post or a comment's post. Since comments are embedded documents, they have the following subfields:

- "userName" - Username of the user inputting.
- "permalink" - Timestamp of the user that inputted.
- "comment" - Comment body.

### Delete

The `Delete` function takes the following format: `post blogName userName title postBody tags timestamp`

The `Delete` function does not remove the post or comment from the database. Instead, it updates the `postBody` or `commentBody` to say "deleted by User," along with the timestamp it was deleted.

### Show

The `Show` function takes the following format: `show blogName`

This function displays all the posts and comments for the corresponding `blogName` database.




