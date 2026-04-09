Main (Node2D)
├── BG (Sprite2D)
├── Player(CharacterBody2D)
│   ├── Sprite2D
│   ├── CollisionShape2D
│   └── Camera2D
├── Roof (StaticBody2D)
│   ├── Sprite2D
│   └── CollisionShape2D
└── CanvasLayer
    └── ScoreLabel (Label)

#main
extends Node2D

@onready var player = $Player
@onready var roof_template = $Roof
@onready var score_label = $CanvasLayer/ScoreLabel

var score = 0
var next_roof_x = 200
var roof_y = 114
var roof_width = 500

func _ready():
	randomize()

	# create first few roofs
	for i in range(5):
		spawn_roof()

func _process(delta):
	score += delta * 10
	score_label.text = "Score: " + str(int(score))

	# keep generating roofs ahead of player
	if player.position.x + 1200 > next_roof_x:
		spawn_roof()

	# remove old roofs behind player
	for roof in get_children():
		if roof.name.begins_with("GeneratedRoof"):
			if roof.position.x < player.position.x - 1200:
				roof.queue_free()

func spawn_roof():
	var new_roof = roof_template.duplicate()
	new_roof.name = "GeneratedRoof" + str(randi())

	var gap = randf_range(-100, 100)
	new_roof.position = Vector2(next_roof_x + gap, roof_y)

	add_child(new_roof)

	next_roof_x = new_roof.position.x + roof_width

#player

extends CharacterBody2D

const SPEED = 250.0
const JUMP_FORCE = -700.0
const GRAVITY = 900.0

func _physics_process(delta):
	if not is_on_floor():
		velocity.y += GRAVITY * delta

	velocity.x = SPEED

	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_FORCE

	move_and_slide()

	if position.y > 700:
		get_tree().reload_current_scene()
