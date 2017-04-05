import sys
import glob
from moviepy.editor import *
import string
import pygame
from moviepy.video.fx.speedx import speedx

#Reading the dialogue from console
inputDialogue = input("Enter a sentence spoken by a mathematics teacher:")

#Removing the punctuations
inputDialogue = inputDialogue.translate(str.maketrans('','',string.punctuation))

#Splitting the inputDialogue to retrieve the different words spoken from the mathematical domain
wordsSpoken = inputDialogue.split()

#Changing the first word of the dialogue to lower case
wordsSpoken[0] = wordsSpoken[0].lower()

#Computing the length of the spoken sentence
numberOfWordsSpoken = len(wordsSpoken)

#Defining an empty list which will later hold all the relevant video files together
clips = []

#Looking for relevant video files from the dataset of videos and then, importing the relevent video files
#If there is no relevant video available for the input word, this means the word is out of pre-defined dictionary domain: 
#it is either a function word or is a mathematical term not defined to the system
k = 0
for i in range(numberOfWordsSpoken):
	if(k!=0): #Checking to differentiate between labels like 'perfect square' (number **2) and 'square' (The shape)
		i=k+1
		k=0
	for name in glob.glob('./signLanguageDataset/*'): #Looping to find the relevant label
		relevantVideoFileName = (((name.split("/")[2]).split(".")[0]).split())	
		if(len(relevantVideoFileName)==1): #Checking for videos which have 1 as length of word label.
			if(wordsSpoken[i] == relevantVideoFileName[0]):
				clip = VideoFileClip(name)
				clips.append(clip)
				del clip
		
		elif(len(relevantVideoFileName)==2):   #Checking for videos which have 2 as length of word label.
			if(wordsSpoken[i] == relevantVideoFileName[0] and wordsSpoken[i+1] == relevantVideoFileName[1]):
				clip=VideoFileClip(name)
				clips.append(clip)
				k=i+1
				del clip

#Concatenating the relevant videos
final_clip = concatenate_videoclips(clips)

#Increasing the play speed of the new translated video file.
translatedClip = speedx(final_clip, factor=2)

#Playing the required video file
translatedClip.preview()



