Main (Node2D)
├── Player (CharacterBody2D)
│   ├── Sprite2D
│   └── CollisionShape2D
├── Zombie (CharacterBody2D)
│   ├── Sprite2D
│   └── CollisionShape2D
├── Goal (Area2D)
│   ├── Sprite2D
│   └── CollisionShape2D
├── ScoreLabel (Label)
├── GameOverLabel (Label)
├── WinLabel (Label)
└── Timer (Timer)

#player
extends CharacterBody2D

@export var speed = 200

func _physics_process(delta):
	var direction = Vector2.ZERO
	
	if Input.is_action_pressed("ui_right"):
		direction.x += 1
	if Input.is_action_pressed("ui_left"):
		direction.x -= 1
	if Input.is_action_pressed("ui_up"):
		direction.y -= 1
	if Input.is_action_pressed("ui_down"):
		direction.y += 1
	
	velocity = direction.normalized() * speed
	move_and_slide()

#zombie
extends CharacterBody2D

@export var speed = 100
@onready var player = $"../Player"
@onready var main = $".."

func _physics_process(delta):
	if main.game_over:
		return
	
	var direction = (player.global_position - global_position).normalized()
	
	velocity = direction * speed
	move_and_slide()
	look_at(player.global_position)
	
	for i in range(get_slide_collision_count()):
		var collision = get_slide_collision(i)
		if collision.get_collider().name == "Player":
			main.show_game_over()


#main
extends Node2D

var score = 0
var game_over = false

@onready var score_label = $ScoreLabel
@onready var game_over_label = $GameOverLabel
@onready var win_label = $WinLabel

func _ready():
	score_label.text = "Score: 0"
	game_over_label.visible = false
	win_label.visible = false

func _on_timer_timeout():
	if not game_over:
		score += 1
		score_label.text = "Score: " + str(score)

func show_game_over():
	if game_over:
		return
	
	game_over = true
	game_over_label.visible = true
	
	$Player.set_physics_process(false)
	$Zombie.set_physics_process(false)
	$Timer.stop()
	
	await get_tree().create_timer(2.0).timeout
	get_tree().reload_current_scene()

func _on_goal_body_entered(body):
	if body.name == "Player" and not game_over:
		show_win()

func show_win():
	if game_over:
		return
	
	game_over = true
	win_label.visible = true
	
	$Player.set_physics_process(false)
	$Zombie.set_physics_process(false)
	$Timer.stop()
	
	await get_tree().create_timer(2.0).timeout
	get_tree().reload_current_scene()

timer > timeout
body > on_Entered
