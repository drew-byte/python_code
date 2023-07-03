import sys

print(sys.version +"\n" + sys.executable + "\n" + sys.platform)

"""
for line in sys.stdin:
    if line.strip() == "exit":
        break
    sys.stdout.write(">> {}".format(line))
    """

if len(sys.argv) != 3:
    print("To run the {} enter a username and password".format(sys.argv))

username = sys.argv[1]
password = sys.argv[2]

print("The username is {} and the password is {}".format(username,password))
