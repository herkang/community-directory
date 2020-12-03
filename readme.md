# Minnesota Community Resource Directory:

Welcome to the Minnesota Community Resource Directory is a platform for users to be able to find local facilities that will allow them to search for their every care needs. A registered user can save and remove resources for their reference. 
# Background:

My name is Kang and I’m a first generation graduate student from the University of Minnesota Twin Cities this Spring 2020. I earned my degree in Mass Communication and Learning Technologies. As an immigrant from a refugee camp, I was motivated by my personal challenges navigating the healthcare and community system in the United States. I wanted to design and develop a platform for users to be able to find local facilities in the Minnesota area. I hope this platform will give others like myself a chance to find resources that will fit their culturally diverse perspectives and give them comfort knowing they are in familiar hands.

# Tech Stack

  - Backend: Flask, Flask_login, Python3, SQLAlchemy, Jinja2
  - Frontend: Boostrap, HTML5, CSS3
  - Database: Pandas, PostgreSQL

# Features

### Sign-up and Login

Users can browse the platform without creating an account. If the user wants to save any resource for future reference, they will need to register an account with a username and password. 

[![Screen-Shot-2020-12-08-at-9-28-34-AM.png](https://i.postimg.cc/Tw6s41J6/Screen-Shot-2020-12-08-at-9-28-34-AM.png)](https://postimg.cc/wtwFt6rf) 

### Resources

Users can browse general resources and community resources in the dropdown navigation. 

[![Screen-Shot-2020-12-08-at-9-28-59-AM.png](https://i.postimg.cc/90GZNXbv/Screen-Shot-2020-12-08-at-9-28-59-AM.png)](https://postimg.cc/Zv5WWS1c)

### Bookmark

Register users can browse resources and save them. 

[![Screen-Shot-2020-12-08-at-9-29-22-AM.png](https://i.postimg.cc/c4BfRHr3/Screen-Shot-2020-12-08-at-9-29-22-AM.png)](https://postimg.cc/SJjXqmLQ)

### Profile

Registered users can look at their saved resources and delete any they don't need.

[![Screen-Shot-2020-12-09-at-8-10-17-AM.png](https://i.postimg.cc/VkT0qwG8/Screen-Shot-2020-12-09-at-8-10-17-AM.png)](https://postimg.cc/0zYNvT1W)

### Installment

Reguirement:

To download this project, please follow the steps below:

Clone repository:

```sh
$ git clone https://github.com/herkang/community-directory.git
```

Create and activate a virtual environment:

```sh
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```

Install dependecies:

```sh
(env) $ pip3 install -r requirements.txt
```

Create database tables:

```sh
(env) $ python3 -i model.py
>>> db.create_all()
```

Start server:
```sh
python3 server.py
```

### Version 2.0

##### Google Api

In the future version, I'd want to provide a map for all facilities. 

##### Search option 

I'd like to implement a search option for easy access.

##### More resources

I'd like to improve on my data gathering skills and provide more resources for each community. 
