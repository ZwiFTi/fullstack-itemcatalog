# Description

This is a Udacity fullstack nanodegree project. The application demonstrates
a couple of interesting methods of web applications. In its core, its an Item Catalog,
but behind the scenes are these techniques:

- Implementation of Python Flask framework
- Mapping of HTTP methods to CRUD operations
- User registration and authentication system (third-party OAuth authentication)
- RESTful web application with JSON endpoints

Registered users will have the ability to post, edit and delete their own items.

# Installation

**In terminal:**

    git clone https://github.com/ZwiFTi/fullstack-itemcatalog.git
    cd fullstack-itemcatalog/vagrant
    vagrant up && vagrant ssh

    python populate_db.py
    python project.py

    Go to localhost:5000
