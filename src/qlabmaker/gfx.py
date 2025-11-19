from pythonosc import udp_client
from programdata import *

QLAB_IP = "127.0.0.1"  # Or the IP of your QLab machine
QLAB_PORT = 53000

client = udp_client.SimpleUDPClient(QLAB_IP, QLAB_PORT)

#GFX_PATH = '/Users/technocake/prosjekter/Konsoll25'
GFX_PATH = '/Users/creativecrew/Desktop/Konsoll25'


def lowerthird(day, speaker, type, group):
	day = 'Day 1' if day == 1 else 'Day 2'
	return f"{GFX_PATH}/GFX/LowerThirds/Speakers/{day}/{group}/RGB_{type}_{speaker}.mp4"


def speakerintro(day, speaker, group):
	day = 'Day 1' if day == 1 else 'Day 2'
	return f"{GFX_PATH}/GFX/SpeakerIntros/{day}/{group}/Intro_{speaker}.mp4"


def create_group(name):
	# Create a group
	client.send_message("/new", "group")
	client.send_message("/cue/selected/name", name)
	client.send_message("/cue/selected/number", name)


def cuename(name, type):
	if type == 'Intro':
		return f"{name}Full"
	return f"{name}Low{type}"


def create_lowerthird_cue(day, speaker, type, group, shortname):
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"RGB_{type}_{speaker}.mp4")
	client.send_message("/cue/selected/number", cuename(shortname, type))
	client.send_message("/cue/selected/fileTarget", lowerthird(day, speaker, type, group))
	#Overlay video output
	client.send_message("/cue/selected/stageName", "Overlay") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Overlay") # Qlab4


def create_speakerintro_cue(day, speaker, group, shortname):
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"Intro_{speaker}.mp4")
	client.send_message("/cue/selected/number", cuename(shortname, 'Intro'))
	client.send_message("/cue/selected/fileTarget", speakerintro(day, speaker, group))

	client.send_message("/cue/selected/stageName", "Video") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Video") # Qlab4




def create_speaker_gfx(day, speaker, group, skip, shortname):
	for type in 'Title', 'Name', 'Combo':
		if speaker in skip and type in skip[speaker]:
			continue
		if not type in skip[group]:
			create_lowerthird_cue(day, speaker, type, group, shortname)

	if speaker in skip and 'Intro' in skip[speaker]:
		return
	if not 'Intro' in skip[group]:
		create_speakerintro_cue(day, speaker, group, shortname)



def main():
	for group in speakers2.keys():
		create_group(group)
		for i, speaker in enumerate(speakers2[group]):
			shortname = shortnames2[group][i]
			create_speaker_gfx(2, speaker, group, skip2, shortname)


if __name__ == '__main__':
	main()