Main
├── ColorRect
├── Player
├── Shark
├── CanvasLayer
│   ├── ScoreLabel
│   └── ResultLabel
├── RestartTimer


#player
extends CharacterBody2D

@export var speed = 250

func _physics_process(delta):
	var direction = Vector2.ZERO
	
	if Input.is_action_pressed("ui_right"):
		direction.x += 1
	if Input.is_action_pressed("ui_left"):
		direction.x -= 1
	if Input.is_action_pressed("ui_down"):
		direction.y += 1
	if Input.is_action_pressed("ui_up"):
		direction.y -= 1
	
	velocity = direction.normalized() * speed
	move_and_slide()

#coin body_enter
extends Area2D

func _on_body_entered(body):
	if body.name == "Player":
		get_parent().add_score()
		queue_free()


#shark
extends CharacterBody2D

@export var speed = 120
@onready var player = get_parent().get_node("Player")

func _physics_process(delta):
	if get_parent().game_ended:
		return
	
	velocity = (player.global_position - global_position).normalized() * speed
	move_and_slide()
	
	for i in range(get_slide_collision_count()):
		var collision = get_slide_collision(i)
		if collision.get_collider().name == "Player":
			get_parent().game_over("GAME OVER")


#main
extends Node2D

var score = 0
var total_coins = 5
var game_ended = false

@onready var score_label = $CanvasLayer/ScoreLabel
@onready var result_label = $CanvasLayer/ResultLabel
@onready var restart_timer = $RestartTimer

var coin_scene = preload("res://coin.tscn")

func _ready():
	spawn_coins()

func spawn_coins():
	for i in range(total_coins):
		var coin = coin_scene.instantiate()
		
		coin.position = Vector2(
			randi_range(50, 750),
			randi_range(50, 450)
		)
		
		add_child(coin)

func add_score():
	if game_ended:
		return
	
	score += 1
	score_label.text = "Score: " + str(score)
	
	if score == total_coins:
		game_over("YOU WIN!")

func game_over(message):
	if game_ended:
		return
	
	game_ended = true
	result_label.text = message
	result_label.visible = true
	restart_timer.start()

func _on_restart_timer_timeout():
	get_tree().reload_current_scene()
