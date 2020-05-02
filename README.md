# CloudflareHttpsOnly
This repository will help you allow https only through Cloudflare on your Linux server.
You must have the Uncomplicated FireWall activated before using it! For activate use `sudo ufw enable` and reboot system.
1. Install `python3.8+`
2. Install requirements:

```
python3.8 -m pip install requests
```
3. Let's add our script to the crontab:
* `nano /etc/crontab`
* Insert the following code:
`0 3 * * 1-7 /usr/bin/python3.8 {path}/set.py &> /dev/null`
* Replace `{path}` with the absolute path to `set.py`
* Save, use ctrl+x
4. Done!

Now at 03:00 on every day-of-week from Monday through Sunday the script will receive current IPv4 Cloudflare addresses and allow them to access HTTPS.
