import unittest

from ascii_canvas.canvas import Canvas
from ascii_canvas.item import Item
from ascii_canvas.item import Line


class TestCanvas(unittest.TestCase):
    """Test the Canvas."""

    def test_render_items_on_canvas(self):
        """Render the added items correctly."""
        canvas = Canvas()

        rect_a = Item('+-----+\n|Hello|\n+-----+', position=[0, 0])
        rect_b = Item('+-----+\n|World|\n+-----+', position=[16, 5])
        rect_c = Item('+-+\n|!|\n+-+', position=[32, 0])
        line_a = Line(start=[7, 1], end=[15, 6])
        line_b = Line(start=[23, 6], end=[31, 1])

        canvas.add_item(rect_a)
        canvas.add_item(rect_b)
        canvas.add_item(rect_c)
        canvas.add_item(line_a)
        canvas.add_item(line_b)
        rendered = canvas.render()
        print(rendered)


if __name__ == '__main__':
    unittest.main(exit=False)
