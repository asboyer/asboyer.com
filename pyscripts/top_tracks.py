f = open('convert.txt', 'r')
raw = f.read()
f.close()
raw = raw.replace('<li>', '').strip('\n').strip()
raw_list = raw.split("</li>")
raw_list.pop()
track_list = []
for i in range(len(raw_list)):
    track_list.append(raw_list[i].strip("\n").strip())

print(track_list)

final_string = "["

for track in track_list:
    if track == track_list[0]:
        final_string += f'"{track}",\n'
    elif track == track_list[len(track_list) - 1]:
        final_string += f'                        "{track}"]'
    else:
        final_string += f'                        "{track}",\n'

f = open('convert.txt', 'w')
f.write(final_string)
