import string
import os
import crypt
import fileinput
#from shutil import copyfile
import shutil
from random import *

def generate_ran_pass():
	characters = string.ascii_letters + "-+=_!@$#*%<>{}[]" + string.digits
	password = "".join(choice(characters) for x in range(randint(8,12)))
	return password

def validate_uname(uname):
	print(uname)
	return True

def validate_home_dir(dir):
	#print(dir)
	return True

def create_user(uname,uhome,ubs,password):
	print(password)
	encPass = crypt.crypt(password,"22")

	ubash=""
#	uname = raw_input("Please insert username: ")
#	uhome = raw_input("Please insert user home directory name: ")
#	ubs = raw_input("Do you want to give shell access to user? ")

	if ubs.lower()=="y" or ubs.lower()=='yes':
		ubash="/bin/bash"
	else:
		ubash="/bin/false"

	if validate_uname(uname) and validate_home_dir(uhome):
		return os.system("useradd -p "+encPass+ " -s "+ ubash + " -d /home/" +uhome+ " " + uname)
	else:
		return False


def main():

	democonf = open("/home/ambrish/democonf.txt",'r')

	uname = raw_input("Please insert username: ")
	uhome = raw_input("Please insert user home directory name: ")
	ubs = raw_input("Do you want to give shell access to user? ")
	password = generate_ran_pass()

	ucr = create_user(uname,uhome,ubs,password)
	print("User created successfully")

	uweb = raw_input("Please provide website name/url: ")
	ualias = raw_input("Please provide website alias url: ")

	apacheconf = open('/home/ambrish/'+ uhome + ".conf",'w')

	for ln in democonf:
#		nln = ln.replace('WEB_HOME', '/home/'+uhome)

		apacheconf.writelines(ln.replace('WEB_HOME', '/home/'+uhome).replace('WEB_URL', uweb).replace('WEB_USER', uname).replace('WEB_ALIAS', ualias))
		#apacheconf.writelines(ln.replace('WEB_HOME', '/home/'+uhome))
		#apacheconf.writelines(ln.replace('WEB_URL', uweb))
		#apacheconf.writelines(ln.replace('WEB_USER', uname))
		#apacheconf.writelines(ln.replace('WEB_ALIAS', ualias))
	democonf.close()
	apacheconf.close()


#	copyfile(democonf,apacheconf)
#	with fileinput.FileInput(apacheconf, inplace=True, backup='.bak') as file:
#		for line in file:
#			print(line.replace('WEB_HOME', '/home/'+uhome))
#			print(line.replace('WEB_URL', uweb))
#			print(line.replace('WEB_USER', uname))
#			print(line.replace('WEB_ALIAS', ualias))
#		file.close()


#	if create_user()==False:
#		print("Cannot create user. Please contact the Server Administrator")



if __name__ == '__main__' : main()
