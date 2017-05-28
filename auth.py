username = raw_input("VK Username:")
password = raw_input("VK Password:")

f = open("config.py", "w")
f.write("username = '" + username + "'\n")
f.write("password = '" + password + "'\n")
f.close()
print
print "Done."
print
