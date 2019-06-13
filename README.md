# Project: Logs_Analysis
## By Archana Elisala

Logs Analysis Project, Part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## What it is and does:

A Reporting page that prints out reports in a plain text format based on the data in the database. This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Technologies
1. PostgreSQL
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

## Project Requirements
Reporting tool should answer the following questions:
1. WHAT ARE THE TOP THREE ARTICLES OF ALL THE TIME ?
2. WHO ARE THE MOST POPULAR ARTICLE AUTHORS OF ALL THE TIME ?
3. ON WHICH DAY MORE THAN ONE PERCENTAGE OF ERRORS OCCURED?

* Project follows good SQL coding practices: Each question should be answered with a single database query.  
* The code is error free and conforms to the PEP8 style recommendations.
* The code presents its output in clearly formatted plain text.

## System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip** (not provided here though)) and **newsdata.py** files from the respository and move them to your **vagrant** directory within your VM.

## Run Following commands From the Gitbash terminal where Vagrant is installed in: 
1. vagrant up ---> This command is Used to start up the VirtualMachine.
2. vagrant ssh ---> This Command is Used to log into the VirtuaalMachine.
3. cd /vagrant ---> For Taking you to Vagrant Directory.
4. cd Logs_Anaylasis-Archana ---> Directing to folder
4. psql -d news -f newsdata.sql ---> To load The Data From the DataBase and for Creating tables.
5. python Archananews.py ---> To Run the Reporting tool.

## Resources
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)kgjhv