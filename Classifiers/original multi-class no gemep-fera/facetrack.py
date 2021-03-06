# Python script to obtain vectors of facial landmarks from emotion datasets, and to categorise these vectors into emotions
# First step in building a classifier pipeline

import shutil 
import os, sys, glob

# Emotion classes to consider in data
emotions = {
1: "Angry", 
2 : "Contempt",
3 : "Disgust",
4 : "Fear",
5 : "Happy",
6 : "Sadness",
7 : "Surprise"
}
data = {}

# Data source dependent - don't want to include in emotion class list but still want to initialise
data["Natural"] = [] 

# Obtain face data from CK+ Database (http://www.consortium.ri.cmu.edu/ckagree/)
print "Processing CK+ database"
for sequence in os.listdir("../../Datasets/CK+/Emotion"):
	if sequence != '.DS_Store':
		for episode in os.listdir('../../Datasets/CK+/Emotion/' + sequence):
			if episode != '.DS_Store':
				for index in glob.glob("../../Datasets/CK+/Emotion/" + sequence + "/" + episode + "/*.txt"):
					index = os.path.basename(index)
					index = index[:index.index("_emotion")]
					for i, index_content in enumerate(open("../../Datasets/CK+/Emotion/" + sequence + "/" + episode + "/" + index + "_emotion.txt")):
						emotion = emotions[int(float(index_content.strip()))]
	 					if not emotion in data: data[emotion] = []
						os.system("cp ../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".png . ; ./face_tracker " + index + ".png ; mv " + index + "* ../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/")
						data[emotion].append("../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + ".vector")
						data[emotion].append("../../Datasets/CK+/cohn-kanade-images/" + sequence + "/" + episode + "/" + index + "_mirror.vector")

# # Obtain face data for KDEF Database (http://www.emotionlab.se/resources/kdef)
print "Processing KDEF database"
for sequence in os.listdir("../../Datasets/KDEF"):
	if sequence != '.DS_Store':
		for face in glob.glob("../../Datasets/KDEF/" + sequence + '/*.JPG'):
			face = os.path.basename(face)
			if face[6] == "S":
				os.system("cp ../../Datasets/KDEF/" + sequence + "/" + face + " . ; ./face_tracker " + face + " ; mv " + face[:face.index(".")] + "* ../../Datasets/KDEF/" + sequence + "/")
				if face[4:6] == "AF":
					data["Fear"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Fear"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "AN":
					data["Angry"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Angry"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "DI":
					data["Disgust"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Disgust"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "HA":
					data["Happy"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Happy"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "NE":
					data["Natural"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Natural"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "SA":
					data["Sadness"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Sadness"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")
				elif face[4:6] == "SU":
					data["Surprise"].append("../../Datasets/KDEF/" + sequence + "/" + face.replace("JPG", "vector"))
					data["Surprise"].append("../../Datasets/KDEF/" + sequence + "/" + face[:face.index(".")] + "_mirror.vector")


# Obtain face data from JAFFE Database (http://www.kasrl.org/jaffe.html)
print "Processing JAFFE database"
for face in glob.glob('../../Datasets/jaffe/*.jpeg'):	
	face = os.path.basename(face)
	os.system("cp ../../Datasets/jaffe/" + face + " . ; ./face_tracker " + face + " ; mv " + face[:face.index(".")] + "* ../../Datasets/jaffe/")
	if face[3:5] == "FE":
		data["Fear"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Fear"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "AN":
		data["Angry"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Angry"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "DI":
		data["Disgust"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Disgust"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "HA":
		data["Happy"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Happy"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "NE":
		data["Natural"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Natural"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "SA":
		data["Sadness"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Sadness"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")
	elif face[3:5] == "SU":
		data["Surprise"].append("../../Datasets/jaffe/" + face.replace("jpeg", "vector"))
		data["Surprise"].append("../../Datasets/jaffe/" + face[:face.index(".")] + "_mirror.vector")

# Obtain face data from RaFD database (http://www.socsci.ru.nl:8180/RaFD2/RaFD?p=main)
print "Processing RaFD database"
for face in glob.glob('../../Datasets/RaFD/*.jpg'):
	face = os.path.basename(face)
	os.system("cp ../../Datasets/RaFD/" + face + " . ; ./face_tracker " + face + " ; mv " + face[:face.index(".")] + "* ../../Datasets/RaFD/")
	components = face.split('_')
	if components[4] == 'angry':
		data["Angry"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Angry"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'contemptuous':
		data["Contempt"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Contempt"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'disgust':
		data["Disgust"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Disgust"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'fearful':
		data["Fear"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Fear"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'happy':
		data["Happy"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Happy"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'neutral':
		data["Natural"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Natural"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'sad':
		data["Sadness"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Sadness"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	elif components[4] == 'surprised':
		data["Surprise"].append("../../Datasets/RaFD/" + face.replace("jpg", "vector"))
		data["Surprise"].append("../../Datasets/RaFD/" + face[:face.index(".")] + "_mirror.vector")
	 			 
# Output vectors to emotion folders
print "Categorising vectors"
for emotion_id in data:
	if not os.path.exists("Face data/" + emotion_id): os.makedirs("Face data/" + emotion_id)
	for index in data[emotion_id]: 
		try:
			shutil.copy2(index, "Face data/" + emotion_id)
		except:
			print("Error:", index)