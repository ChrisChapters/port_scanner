This is a simple web app for port scanner.

You can use this tool to find the open ports of an IP address. 

To find the IP address of a website, use nslookup, for example: nslookup 'site_name'.

here is the installation steps,


sudo git clone https://github.com/ChrisChapters/port_scanner.git

ls/

cd port_scanner/

sudo python -m venv venv/                   //(create a new environment)

source venv/bin/activate/

pip install -r requirements.txt/

sudo python run.py/
