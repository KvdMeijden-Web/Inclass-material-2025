add_song = True

song_list = []
import random
print("Welcome to the Music Playlist Manager!")
# never use: file = open("songlist.txt", "r")

with open("songlist.txt", "r") as file:
        for line in file:
            song_list.append(line.strip())

print(song_list)

while add_song == True:
    song = input("Do you want to add a song? (yes/no):\n ").lower().strip()
    if song == "yes":
        
        song_name = input("Enter the name of the song:\n ")
        song_list.append(song_name)
        print(song_list)
        # add song to playlist (append song_name to song_list)
        # with open(file, "w") as file:
        #     for song in playlist:
        #         file.write(song + "\n")
    else:
        add_song = False
length_songlist = len(song_list)
print("You have", length_songlist, "songs in your playlist.")
choice_song =input("What song do you want to play? nr/random:\n")
if choice_song == "random":
    r_choice = random.choice(song_list)
    print("playing", r_choice)


else:
    choice_song = int(choice_song)
    choice_index = choice_song - 1
    print("playing", song_list[choice_index])

# code to play song (print the song name)