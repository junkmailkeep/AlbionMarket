extends Node2D

var currentURLIndex :=0

func _on_pull_all_button_pressed():
	MakeHttpRequest()

func MakeHttpRequest():
	if currentURLIndex < URLS.URLArray.size():
		$HTTP_1.download_file = "res://Data/Data"+str(currentURLIndex)+".json"
		$HTTP_1.request(URLS.URLArray[currentURLIndex])
	else:
		print("All Data Pulled")
		
func _on_http_1_request_completed(result, response_code, headers, body):
	if response_code == 200:
		currentURLIndex +=1
		MakeHttpRequest()
	
