# r --> read
# w --> write
# a --> append
# x --> create


file = open("Name of the file" , "mode")
file.close()

# file = open("test.txt" , "x")
# file.close()


test_text = open("test.txt" , "r")

print(test_text.readline())
print(test_text.readable())

test_text .close()