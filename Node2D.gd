extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$HTTPRequest.request_completed.connect(_on_http_request_request_completed)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_button_pressed():
	$HTTPRequest.request(URL.Cloth)
	print("Data Pulled")


func _on_http_request_request_completed(result, response_code, headers, body):
	pass # Replace with function body.
