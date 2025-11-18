from pythonosc import udp_client
from programdata import *

QLAB_IP = "127.0.0.1"  # Or the IP of your QLab machine
QLAB_PORT = 53000

client = udp_client.SimpleUDPClient(QLAB_IP, QLAB_PORT)

GFX_PATH = '/Users/technocake/prosjekter/Konsoll25'


def lowerthird(day, speaker, type, folder):
	day = 'Day 1' if day == 1 else 'Day 2'
	return f"{GFX_PATH}/GFX/LowerThirds/Speakers/{day}/{folder}/RGB_{type}_{speaker}.mp4"


def speakerintro(day, speaker, folder):
	day = 'Day 1' if day == 1 else 'Day 2'
	return f"{GFX_PATH}/GFX/SpeakerIntros/{day}/{folder}/Intro_{speaker}.mp4"


def create_group(name):
	# Create a group
	client.send_message("/new", "group")
	client.send_message("/cue/selected/name", name)
	client.send_message("/cue/selected/number", name)



def create_lowerthird_cue(day, speaker, type, folder):
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"RGB_{type}_{speaker}.mp4")
	client.send_message("/cue/selected/number", f"{speaker}{type}Low")
	client.send_message("/cue/selected/fileTarget", lowerthird(day, speaker, type, folder))
	#Overlay video output
	client.send_message("/cue/selected/stageName", "Overlay") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Overlay") # Qlab4


def create_speakerintro_cue(day, speaker, folder):
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"Intro_{speaker}.mp4")
	client.send_message("/cue/selected/number", f"{speaker}Intro")
	client.send_message("/cue/selected/fileTarget", speakerintro(day, speaker, folder))

	client.send_message("/cue/selected/stageName", "Video") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Video") # Qlab4


def create_speaker_gfx(day, speaker, folder, skip):
	for type in 'Title', 'Name', 'Combo':
		if speaker in skip and type in skip[speaker]:
			continue
		if not type in skip[folder]:
			create_lowerthird_cue(day, speaker, type, folder)

	if speaker in skip and 'Intro' in skip[speaker]:
		return
	if not 'Intro' in skip[folder]:
		create_speakerintro_cue(day, speaker, folder)


def main():
	for group in speakers2.keys():
		create_group(group)
		for speaker in speakers2[group]:
			create_speaker_gfx(2, speaker, group, skip2)


if __name__ == '__main__':
	main()