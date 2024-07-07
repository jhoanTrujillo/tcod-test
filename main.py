#!/usr/bin/env python3
import tcod
# Modules folder packages
from modules.engine import Engine
from modules.input_handlers import EventHandler    
from modules.entity import Entity

# None because it returns no values
def main() -> None:
    # Screen size variables
	screen_width = 80
	screen_height = 50

    # Declare tileset
	tileset = tcod.tileset.load_tilesheet(
		"data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
	)

	# declare function to handle events
	event_handler = EventHandler()	

	# declare entities
	player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255,255,255))
	npc = Entity(int(screen_width / 2 + 5), int(screen_height / 2), "T", (255,255,255))
	entities = {npc, player}

	# Instance the engine class to render entities and handle inputs
	engine = Engine(entities=entities, event_handler=event_handler, player=player)

	""" Create console to display """
	with tcod.context.new_terminal(
		screen_width,
		screen_height,
		tileset=tileset,
		title="Yet Another Roguelike Tutorial",
		vsync=True,
	) as context:
		# Creates the screen object with the values declared above
		root_console = tcod.Console(screen_width, screen_height, order="F")

		while True:
			engine.render(console=root_console, context=context)
			events = tcod.event.wait()
			engine.handle_events(events)


if __name__ == "__main__":
	main()