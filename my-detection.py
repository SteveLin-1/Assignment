
#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput


from jetson.inference import detectNet
from jetson.utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0") 
display = jetson.utils.videoOutput("display://0")
while display.IsStreaming():
	img = camera.Capture()
	

	if img is None:
		continue

	detections = net.Detect(img)
	print(detections[0])
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))