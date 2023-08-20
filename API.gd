extends Node2D



func _on_cloth_button_pressed():
	$HTTP_Cloth.request(URL.Cloth)
	


func _on_leather_button_pressed():
	pass # Replace with function body.


func _on_plate_button_pressed():
	$HTTP_Plate.request(URL.Plate)


func _on_http_cloth_request_completed(result, response_code, headers, body):
	#var json = JSON.new()
	#json.parse(body)
	#var response = json.get_data()
	pass
