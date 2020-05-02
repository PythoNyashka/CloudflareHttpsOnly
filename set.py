# -*- coding: utf-8 -*-
import subprocess
import requests
import datetime

cmds = {
	'get_rules_ids': "ufw status numbered | grep '%s'|awk -F'[][]' '{print $2}'",
	'del_rule': "sudo ufw --force delete %s",
	'add_rule': 'sudo ufw allow from %s to any port %s'
}

cloudflare_ips_v4_url = 'https://www.cloudflare.com/ips-v4'

def get_rules_ids_func(port):
	return [int(b) for i in subprocess.check_output(
				cmds['get_rules_ids'] % port,
				shell=True,
				executable='/bin/bash'
			).decode("utf-8").split('\n') \
			if (b := i.replace(' ', '')) not in ['', ' ', '\n']]

def del_all_rules(port):
	rules = get_rules_ids_func(port)

	for index in range(rules.__len__()):
		subprocess.check_output(
			cmds['del_rule'] % rules[0],
			shell=True,
			executable='/bin/bash'
		)
		rules = get_rules_ids_func(port)

def get_cf():
	return [i for i in requests.get(cloudflare_ips_v4_url).text.split('\n') \
			if i  not in ['', ' ', '\n']]

def set_rules(rules, port):
	for rule_ip in rules:
		subprocess.check_output(
			cmds['add_rule'] % (rule_ip, port),
			shell=True,
			executable='/bin/bash'
		)


def main():
	print('- ' * 20)
	print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
	print('Deleting all rules ...')
	del_all_rules(443)
	print('Setting rules ...')
	set_rules(get_cf(), 443)
	print('Done.')

if __name__ == '__main__':
	main()
