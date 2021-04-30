from youtubesearchpython import VideosSearch
import sys

def get_results(show,lim):
	results = []
	videosSearch = VideosSearch(show, limit = int(lim))
	result = videosSearch.result()['result']
	for x in result:
		video = {}
		video["title"] = x["title"]
		video["duration"] = x["duration"]
		video["link"] = x["link"]
		video["channel_name"] = x["channel"]["name"]
		video["channel_link"] = x["channel"]["link"]
		results.append(video)
		del video
	return results

def show_results(show,lim):
	results = get_results(show,lim)
	for x in results:
		print("Title: ",x["title"])
		print("Duration: ",x["duration"])
		print("Video Link: ", x["link"])
		print("Channel Name: ",x["channel_name"])
		print("Channel Link: ", x["channel_link"])
		print("-"*100)


show = sys.argv[1]
lim = sys.argv[2]

show_results(show,lim)