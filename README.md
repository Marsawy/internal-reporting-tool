# internal-reporting-tool
### Introduction For Log Analysis

This is the third project for the Udacity Full Stack Web Development Nanodegree. Being new to databases this project ,  it create complex SQL queries to access a very large database (> 1000k rows) and extract specific data and print it out. This project is an internal reporting tool by taking log data and calculating statistics from it.
(based on python 2.7)

he database in question is a newspaper company database where we have 3 tables; `articles`, `authors` and `log`.
* `articles` - Contains articles posted in the newspaper so far.
* `authors` - Contains list of authors who have published their articles.
* `log` - Stores log of every request sent to the newspaper server.

### Discover News Database <br>
1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)<br>
2. Download or clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)</br>
3. Now we got newsdata.sql in our vagrant directory and now we are good to go.</br>
4. change directory to vagrant<br>
5. use command **psql -d news -f newsdata.sql** to load database<br>
    -use **\c** to connect to database="news"<br>
    -use **\dt** to see the tables in database<br>
    -use **\dv** to see the views in database<br>
    -use **\q** to quit the database<br>

### Run internal reporting tool 
<h4> IRT Results </h4>
1. What are the most popular three articles of all time?<br>
2. Who are the most popular article authors of all time?<br>
3. On which days did more than 1% of requests lead to errors? <br>

<h4> Run IRT </h4>
* Make sure you have `newsdata.sql`, the SQL script file with all the data. It can be downloaded from the Udacity Repo.
- clone or download IRT Repo. <br>
- move it to vagrant folder on your local machine 
- open vagrant in terminal (linux users) or in bash (windows users) 
- write vagrant up then vagrant ssh
* now you are in vagrant VM server :D
- Change directory to /vagrant and look around with ls.
- with cd command get in /newsdb

- Finally run the script.

```sh
python IRT.py

```
