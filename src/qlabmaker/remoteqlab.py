from pythonosc import udp_client

QLAB_IP = "10.0.0.197"  # Or the IP of your QLab machine
#QLAB_IP = "127.0.0.1"  # Or the IP of your QLab machine
QLAB_PORT = 53000

client = udp_client.SimpleUDPClient(QLAB_IP, QLAB_PORT)

GFX_PATH = '/Users/creativecrew/Desktop/Konsoll25'
#GFX_PATH = '/Users/technocake/prosjekter/Konsoll25'


def looppath(loop):
	return f"{GFX_PATH}/GFX/Misc//{loop}_Loop.mp4"

def cuename(loop):
	return f"{loop}Full"

def schedulepath(day):
	return f"{GFX_PATH}/GFX/Schedule/{day}/{day} Schedule.mp4"
def  watermarkpath(name):
	return f"{GFX_PATH}/GFX/Overlays/{name}_2025_RGB.mp4"

def create_group(name):
	# Create a group
	client.send_message("/new", "group")
	client.send_message("/cue/selected/name", name)
	client.send_message("/cue/selected/number", name)

def create_loop_cue(loop):
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"{loop}_Loop.mp4")
	client.send_message("/cue/selected/number", cuename(loop))
	client.send_message("/cue/selected/fileTarget", looppath(loop))

	client.send_message("/cue/selected/stageName", "Video") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Video") # Qlab4


def create_schedule_cue(day):
	day = 'Day 1' if day == 1 else 'Day 2'
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"{day}_Schedule.mp4")
	client.send_message("/cue/selected/number", cuename(day))
	client.send_message("/cue/selected/fileTarget", schedulepath(day))

	client.send_message("/cue/selected/stageName", "Video") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Video") # Qlab4


def create_overlay_cue(name):
	client.send_message("/new", "video")
	client.send_message("/cue/selected/name", f"{name}_2025.mp4")
	client.send_message("/cue/selected/number", f"{name}Low")
	client.send_message("/cue/selected/fileTarget", watermarkpath(name))

	client.send_message("/cue/selected/stageName", "Overlay") # Qlab5
	client.send_message("/cue/selected/videoSurface", "Overlay") # Qlab4

def create_loops():
	create_group('Loops')

	for loop in ['Social', 'Team', 'Sponsors']:
		create_loop_cue(loop)

	for day in [1, 2]:
		create_schedule_cue(day)



if __name__ == '__main__':
	#create_loops()

	create_group('Overlays')
	for overlay in ['Watermark']:
		create_overlay_cue(overlay)

