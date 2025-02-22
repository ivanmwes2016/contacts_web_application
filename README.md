# CONTACTS WEB APPLICATION

# RUNNING LOCALLY

Ensure you have python installed and a virtual environment.

If no virtual enironment is installed, run these
python3 -m venv env
source env/bin/activate

1. Install dependencies all the necessary dependencies
   pip install -r requirements.txt

Command Alias are in the Makefile.
• To run the server -> make run
• Any update to the schema -> make migrate

# THE API

[host = http://127.0.0.1:8000 for development]

Show all contacts -> <host>/api/contacts
Create -> <host>/app/contact/create
ContactByID -> Create -> <host>/app/contact/<int:id>
Update -> <host>/app/contact/<int:id>/update
Delete -> <host>/app/contact/<int:id>/delete

# THE USER INTERFACE

To interact with the User Interaface
use: <host>/app

# DEPLOYING THE APPLICATION
