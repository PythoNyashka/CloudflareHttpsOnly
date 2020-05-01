# CloudflareHttpsOnly
This repository will help you allow https only through Cloudflare on your Linux server.
You must have the Uncomplicated FireWall activated before using it! For activate use `sudo ufw enable` and reboot system.
1. Install `python3.8+`reboot
2. Install requirements:

```
python3.8 -m pip install requests
python3.8 -m pip install apscheduler
```
3. Let's add our script to the startup:
* `nano /etc/systemd/system/cloudflarehttpsonly.service`
* Insert the following code:
```
[Unit]
Description=socket_mailing socket daemon
After=syslog.target network.target mysql.service

[Service]
Type=simple
User=root
WorkingDirectory={path}
ExecStart=/usr/bin/python3.8 {path}/set.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```
* Replace `{path}` with the absolute path to `set.py`
* Save, use ctrl+x
* `systemctl enable cloudflarehttpsonly`
* `systemctl start cloudflarehttpsonly`
4. Done!

Now every 12 hours the script will receive current IPv4 Cloudflare addresses and allow them to access HTTPS.
