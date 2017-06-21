#!/usr/bin/python
username = raw_input("Логин:")
password = raw_input("Пароль:")

f = open("config.py", "w")
f.write("username = '" + username + "'\n")
f.write("password = '" + password + "'\n")
f.close()
print
print "Done."
print
