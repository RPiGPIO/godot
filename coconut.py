Main (Node2D)
├── Player (CharacterBody2D)
│   ├── Sprite2D
│   └── CollisionShape2D
├── Ground (StaticBody2D)
│   └── CollisionShape2D
├── ScoreLabel (Label)
└── SpawnTimer (Timer)

Coconut (Area2D) body entered
├── Sprite2D
├── CollisionShape2D
└── VisibleOnScreenNotifier2D

#player
extends CharacterBody2D

const SPEED = 400

func _physics_process(delta):
	var direction = 0
	
	if Input.is_action_pressed("ui_left"):
		direction = -1
	elif Input.is_action_pressed("ui_right"):
		direction = 1
	
	velocity.x = direction * SPEED
	move_and_slide()


#coconut
extends Area2D

@export var speed = 300
var game_manager = null

func _process(delta):
	position.y += speed * delta

func _on_body_entered(body):
	if body.name == "Player":
		game_manager.game_over()
		queue_free()
	
	if body.name == "Ground":
		game_manager.add_score()
		queue_free()


#main
extends Node2D

@onready var spawn_timer = $SpawnTimer
@onready var score_label = $ScoreLabel

var coconut_scene = preload("res://coconut.tscn")
var score = 0
var game_ended = false

func _ready():
	randomize()
	spawn_timer.timeout.connect(spawn_coconut)

func spawn_coconut():
	if game_ended:
		return
	
	var coconut = coconut_scene.instantiate()
	add_child(coconut)
	
	coconut.position = Vector2(randi_range(50, 1150), -50)
	coconut.game_manager = self

func add_score():
	score += 1
	score_label.text = "Score: " + str(score)

func game_over():
	game_ended = true
	spawn_timer.stop()
	score_label.text = "Game Over! Score: " + str(score)
	
	await get_tree().create_timer(2.0).timeout
	get_tree().reload_current_scene()
