#!/usr/bin/env python3
import tcod
# Modules folder packages
from modules.actions import EscapeAction, MovementAction
from modules.input_handlers import EventHandler    

# None because it returns no values
def main() -> None:
    # Declare tileset
	tileset = tcod.tileset.load_tilesheet(
		"data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
	)

	# declare function to handle events
	event_handler = EventHandler()	

	# Screen size variables
	screen_width = 80
	screen_height = 50
	
	# Player position variables
	player_x = int(screen_width / 2)
	player_y = int(screen_height / 2)
	
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
			root_console.print(x=player_x, y=player_y, string="@")
			# Displays the console in root_console
			context.present(root_console)

			root_console.clear()
			# Process the events in the game
			for event in tcod.event.wait():
       
				action = event_handler.dispatch(event)
    
				if action is None:
					continue

				if isinstance(action, MovementAction):
					player_x += action.dx
					player_y += action.dy

				elif isinstance(action, EscapeAction):
					raise SystemExit()



if __name__ == "__main__":
	main()