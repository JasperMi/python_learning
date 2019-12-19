def make_album(singer, album, count=''):
    if count:
        singer_album = {'singer': singer, 'album': album, 'count': count}
    else:
        singer_album = {'singer': singer, 'album': album}
    return singer_album


while True:
    print("\nEnter 'q' at any time to quit.")

    s_name = input("Please input singer's name: ")
    if s_name == 'q':
        break

    a_name = input("Please input album's name: ")
    if a_name == 'q':
        break

    singer_album = make_album(s_name, a_name)
    print(singer_album)

# album = make_album('Jay', 'Qingtian', 60)
# print(album)
# album = make_album('Jay', 'Geiwoyishougedeshijian', 20)
# print(album)
# album = make_album('Jay', 'Tiantiande')
# print(album)
