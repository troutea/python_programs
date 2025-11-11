

albums = [("album1", "name1"), ("album2", "name2"), ("album3", "name3"), ("album4", "name4"), ("album5", "name5") ]

print(len(albums))


for album in albums:
    print("Album: {}, Artist: {}".format(album[0], album[1]))
