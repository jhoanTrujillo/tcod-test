from __future__ import annotations

# Some other library that works for classes.
import attrs
# Imports from tcod lib
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

@attrs.define()
class ExampleState:
    """Example state with a hard-coded player position."""

    player_x: int
    """Player X position, left-most position is zero."""
    player_y: int
    """Player Y position, top-most position is zero."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the player glyph."""
        console.print(self.player_x, self.player_y, "@")

def main() -> None:
    """Load a tileset and open a window using it, this window will immediately close."""
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    """Here we add a console log to check a window and the program running"""
    console = tcod.console.Console(80, 50)
    console.print(30, 30, "Hello World")
    
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:  # Main loop
            context.present(console)  # Render the console to the window and show it
            for event in tcod.event.wait():  # Event loop, blocks until pending events exist
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


if __name__ == "__main__":
    main()