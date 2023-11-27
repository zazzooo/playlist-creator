import random

dict_keys = {
    '1A' : (['12A', '2A', '1B', '4B', '10B'], ['3A', '8A', '6A']),
    '2A' : (['1A', '3A', '5B', '11B', '2B'], ['4A', '7A', '9A']),
    '3A' : (['2A', '4A', '6B', '12B', '3B'], ['5A', '8A', '10A']),
    '4A' : (['3A', '5A', '7B', '1B', '4B'], ['6A', '9A', '11A']),
    '5A' : (['4A', '6A', '8B', '2B', '5B'], ['7A', '10A', '12A']),
    '6A' : (['5A', '7A', '9B', '3B', '6B'], ['8A', '11A', '1A']),
    '7A' : (['6A', '8A', '10B', '4B', '7B'], ['9A', '12A', '2A']),
    '8A' : (['7A', '9A', '11B', '5B', '8B'], ['10A', '1A', '3A']),
    '9A' : (['8A', '10A', '12B', '6B', '9B'], ['11A', '2A', '4A']),
    '10A' : (['9A', '11A', '1B', '7B', '10B'], ['12A', '3A', '5A']),
    '11A' : (['10A', '12A', '2B', '8B', '11B'], ['1A', '4A', '6A']),
    '12A' : (['11A', '1A', '3B', '9B', '12B'], ['2A', '5A', '7A']),
    '1B' : (['12B', '2B', '1A', '4A', '10A'], ['3B', '8B', '6B']),
    '2B' : (['1B', '3B', '5A', '11A', '2A'], ['4B', '7B', '9B']),
    '3B' : (['2B', '4B', '6A', '12A', '3A'], ['5B', '8B', '10B']),
    '4B' : (['3B', '5B', '7A', '1A', '4A'], ['6B', '9B', '11B']),
    '5B' : (['4B', '6B', '8A', '2A', '5A'], ['7B', '10B', '12B']),
    '6B' : (['5B', '7B', '9A', '3A', '6A'], ['8B', '11B', '1B']),
    '7B' : (['6B', '8B', '10A', '4A', '7A'], ['9B', '12B', '2B']),
    '8B' : (['7B', '9B', '11A', '5A', '8A'], ['10B', '1B', '3B']),
    '9B' : (['8B', '10B', '12A', '6A', '9A'], ['11B', '2B', '4B']),
    '10B' : (['9B', '11B', '1A', '7A', '10A'], ['12B', '3B', '5B']),
    '11B' : (['10B', '12B', '2A', '8A', '11A'], ['1B', '4B', '6B']),
    '12B' : (['11B', '1B', '3A', '9A', '12A'], ['2B', '5B', '7B'])
    }

class song:
    def __init__(self, name, key):
        self.name = name
        self.key = key
        self.compatible_keys = dict_keys[self.key][0]
        self.boost_keys = dict_keys[self.key][1]

    def __str__(self):
        return f' Song: {self.name} \n Key: {self.key} \n Compatible songs: {self.list_compatible} \n Boost songs: {self.list_boost}'

    def recomended_song(self, playlist):
        list_compatible = []
        list_boost = []
        for song in playlist:
            if song.key in self.compatible_keys:
                list_compatible.append((song.name, song.key))
            if song.key in self.boost_keys:
                list_boost.append((song.name, song.key))
        self.list_compatible = list_compatible
        self.list_boost = list_boost

    def match_compatible_song(self):
        return random.choice(self.list_compatible)
    
    def match_boost_song(self):
        return random.choice(self.list_boost)

# first_song = song('name_song1', '1B')
# final_order = []
# final_order[0] = first_song
# playlist = [song('NAME2', '3A'), song('name3', '1A') , song('name4', '7A'), song('name5', '9A')]
# first_song.recomended_song(playlist)
# final_order[-1] = final_order[-1].match_compatilble_song()
# print(final_order)

# if __name__ == '__manin__':
#     first_song = song('name_song1', '1B')
    
#     playlist = [song('NAME2', '3A'), song('name3', '1A') , song('name4', '7A'), song('name5', '9A')]
#     first_song.recomended_song(playlist)
#     print(first_song)