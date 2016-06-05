def song_decoder(song):
    words_list = song.split('WUB')
    words_list2 = []
    for i in words_list:
        if i != '':
            words_list2.append(i)
    song = ' '.join(words_list2)
    return song

print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
  # =>  WE ARE THE CHAMPIONS MY FRIEND
