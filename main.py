#The lesson list

#myList = ["hello", "I", "love", "you"]

myTuple = (3, 5, (4, 5, 4))

# for i in myTuple:
#     print(i)

# for i in enumerate(myTuple):
#     print(i)
#
for i in range(len(myTuple)):
    if i == len(myTuple) - 1:
        print(i, *myTuple)
        break
    print(i, myTuple)


