import fire
import toml
import os
import subprocess
from datetime import date


def backup(config_file_name):

	# This is function that backs up data from remote MySQL server with its
	# arguments provided by configuration file.

	# Let database name be 'kvant'.

	config = toml.load(config_file_name)

	for servername in config.get('db').keys():
		ip = config.get('db').get(servername).get('ip')
		username = config.get('db').get(servername).get('username')
		password = config.get('db').get(servername).get('password')

		path = config.get('general').get('backup_path')
		sk = config.get('general').get('sk')
		day = str(date.today())
		# category ? server ?
		
		tables_item = config.get('db').get(servername).get("tables")
		if isinstance(tables_item, list):
			for table in tables_item:
				endpath = path + '/' + sk + '/' + day + '/' + table + '.sql'
				# print("mysqldump {} {} > {}".format(
				# 	servername, table, endpath))
				subprocess.run("mysqldump -u{} -p{} {} {} -r{}".format(
					username, password, 'kvant', table, endpath))
		else:
			table = tables_item
			endpath = path + '/' + sk + '/' + day + '/' + table + '.sql'
			# os.makedirs(os.path.dirname(endpath, exist_ok=True)) ??????
			# print("mysqldump -u{} -p{} {} {} -r{}".format(username, 
			# 	password, 'kvant', table, endpath))
			subprocess.run("mysqldump -u{} -p{} {} {} -r{}".format(
				username, password, 'kvant', table, endpath)) ## for windows
			# subprocess.run("mysqldump -u{} -p{} {} {} > {}".format(
			# 	username, password, 'kvant', table, endpath)) ## for linux

if __name__ == '__main__':
	fire.Fire(backup)