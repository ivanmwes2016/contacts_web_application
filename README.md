# CONTACTS WEB APPLICATION
Using python django, ajax for front-end interactions.

## Getting Started

Ensure you have python installed and a virtual environment.

If no virtual enironment is installed, run these
python3 -m venv env
source env/bin/activate

In `/contacts` folder:

1. Install dependencies all the necessary dependencies from `requirements.txt`
   pip install -r requirements.txt

Command Alias are in the Makefile.
- Any update to the schema -> `make migrate`
- To run the server -> `make run`


## The Api endpoints

[host = http://127.0.0.1:8000 for development]

- Show all contacts -> `/api/contacts`
- Create -> `/app/contact/create`
- ContactByID `/app/contact/<int:id>`
- Update -> `/app/contact/<int:id>/update`
- Delete -> `/app/contact/<int:id>/delete`

## Accessing the client/front-end
To interact with the User Interaface
use: `/app` will render the contacts page.


## DEPLOYING THE APPLICATION
For this application we will use AWS-EC2 + gunicon + Nginx + Github actions for deployment automation.
1. 
