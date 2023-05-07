name = open('name.txt')
print(name.read())
name.close()

#choices (r || w || a)

bday = open('bday.txt','choices')
bday.write("text")
bday.close()

# r = read
# w = write
# a = append