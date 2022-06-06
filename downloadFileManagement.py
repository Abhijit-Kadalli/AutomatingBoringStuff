import os
import shutil

#replace locations for windows with appropriate ones

x = input("Enter your PC username ")

download_file_location = "/home/"+ x +"/Downloads"

image_destination_location = "/home/"+ x +"/Documents/downloaded image"

audio_destination_location = "/home/"+ x +"/Documents/downloaded audio"

video_destination_location = "/home/"+ x +"/Documents/downloaded video"

documents_destination_location = "/home/"+ x +"/Documents/downloaded documents"

for i in  os.listdir(download_file_location):

	print(i)
	
	if i.endswith(".mp3") or i.endswith(".wav"):
		shutil.move(download_file_location + "/" + i, audio_destination_location)
	
	elif i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png") or i.endswith(".gif") or i.endswith(".jfif") or i.endswith(".pjpeg") or i.endswith(".pjp") or i.endswith(".svg") :
		shutil.move(download_file_location + "/" + i, image_destination_location)
	
	elif i.endswith(".mp4") or i.endswith(".mov") or i.endswith(".mwv") or i.endswith(".avi") or i.endswith(".mkv") or i.endswith(".flm") :
		shutil.move(download_file_location + "/" + i, video_destination_location)
	
	else :
		shutil.move(download_file_location + "/" + i, documents_destination_location)	

	print("file moved successfully... \n")		
