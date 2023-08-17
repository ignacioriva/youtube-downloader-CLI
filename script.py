from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def getVideoQualities(url):
	yt = YouTube(url)
	qualities = []

	for stream in yt.streams.order_by('resolution'):
		qualities.append(stream.resolution)

	qualitiesClean = list(dict.fromkeys(qualities))

	return qualitiesClean

def downloadVideo(url, quality):
	yt = YouTube(url).streams.filter(resolution = quality).first().download()
	print('el video ha sido descargado correctamente.')


videoURL = input('ingresar la URL del video a descargar:\n')
qualities = getVideoQualities(videoURL)

print('CALIDADES')

for idx, quality in enumerate(qualities): 
	print(f'{idx}) ' + quality)

optionQuality = input('Elige alguna opcion: ')

optionSelected = qualities[int(f'{optionQuality}')]

downloadVideo(videoURL, optionSelected)

