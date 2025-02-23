# CONTACTS WEB APPLICATION
Using python django, ajax for front-end interactions.

## Getting Started

### Step 1: Clone the repo
1. Navigate to the director where you want to clone the repo
`cd /path/your-folder`
2. use git clone: You can use the `https` or `SSH`
- `git clone https://github.com/ivanmwes2016/contacts_web_application.git` and `cd /contacts`
  

### Step 2: Installing Dependencies
Ensure you have python installed and a virtual environment.

If no virtual enironment is installed, run these
python3 -m venv env
source env/bin/activate

1. In `/contacts` folder:
Install dependencies all the necessary dependencies from `requirements.txt` run: 
- `pip install -r requirements.txt`

Command Alias are in the Makefile.
- Any update to the schema → `make migrate`
- To run the server → `make run`


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


## 🌍 Deploying the app
For this application we will use AWS-EC2 + gunicon + Nginx + Github actions for deployment automation.
`gunicon` for WSGI server processes and `Ngnix` for proxy and static-file server.

### Steps for deployment: Login into you IAM account 
1️⃣ Launch an EC2 Instance
- Go to AWS Console → EC2 → Launch Instance
- Choose Ubuntu 22.04 (or Amazon Linux 2)
- Set security group to allow:
   - SSH (port 22)
   - HTTP (port 80)
   - HTTPS (port 443)
   - Custom TCP (port 8000)
- Select Key Pair to access the instance

2️⃣ Connect to the Instance
- ssh -i `your-key.pem` ubuntu@`your-ec2-public-ip`
- `sudo apt update && sudo apt upgrade -y`

3️⃣ Install Dependencies on EC2
-`sudo apt install python3-pip python3-venv -y`
- Install PostgresSQL: `sudo apt install postgresql postgresql-contrib libpq-dev -y`
  
```
Note: In our file we used, an onfile sqlite.db file for data persistence.

   ⚠️ However: Using an on-file SQLite database on AWS is not recommended for production, because:
   
    - Data Loss Risk – If the EC2 instance restarts or gets replaced, the SQLite file can be lost.
    - Concurrency Issues – SQLite does not handle multiple users well, which can cause database locks.
    - Scaling Problems – If you add more EC2 instances later, they won’t share the same SQLite file.

```

4️⃣ Set Up the Django Project
- clone the repo: ``git clone https://github.com/ivanmwes2016/contacts_web_application.git` and `cd /contacts`
- Create virtual Enviroment: `python3 -m venv venv` then `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Make migrations: `make migrate` or `python manage.py migrate`
- Collect static files: `python manage.py collectstatic --noinput`

5️⃣ Configure Gunicorn & Nginx
1. `pip install gunicorn` and test using `gunicorn --bind 0.0.0.0:8000 contacts.wsgi`
2. Install & Configure Nginx
   - `sudo apt install nginx -y`
   - `sudo nano /etc/nginx/sites-available/django`
   - in the nginx file configure as below:

```
nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Enable the config.
`sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled
sudo systemctl restart nginx`

### Automate Deployment with GitHub Actions
Inside the git repo create a file: .github/workflows/deploy.yml

```
name: Deploy Django to AWS EC2
on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: SSH into EC2 and Deploy
        env:
          PRIVATE_KEY: ${{ secrets.EC2_SSH_KEY }}
          HOST: ${{ secrets.EC2_HOST }}
          USER: ubuntu

        run: |
          echo "$PRIVATE_KEY" > deploy_key.pem
          chmod 600 deploy_key.pem
          ssh -o StrictHostKeyChecking=no -i deploy_key.pem $USER@$HOST << 'EOF'
            cd your-django-app
            git pull origin main
            source venv/bin/activate
            pip install -r requirements.txt
            python manage.py migrate
            python manage.py collectstatic --noinput
            sudo systemctl restart gunicorn
            sudo systemctl restart nginx
          EOF

```

🔑 ### Set up GitHub Secrets
- Go to GitHub → Repo → Settings → Secrets
- Add these secrets:
  
`EC2_SSH_KEY` → Your EC2 private key

`EC2_HOST` → Your EC2 public IP

🚀  # Done! It's advised to create branches from  the main branch. When you merge the changes to main an automatic depolyment will trigger.





