from ascii_canvas.canvas import Canvas
from ascii_canvas.item import Item
from ascii_canvas.item import Line
from ascii_canvas.item import Rectangle


def test_render_items_on_canvas():
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

    rendered = canvas.render(line_numbers=False)
    print(rendered)

    rendered = canvas.render(line_numbers=True)
    print(rendered)


def test_rectangle():
    """Render a bunch of rectangles."""
    canvas = Canvas()

    null_rect = Rectangle(width=0, height=0)
    canvas.add_item(null_rect)

    null_hor_rect = Rectangle(width=0, height=1, position=[5, 0])
    canvas.add_item(null_hor_rect)

    null_ver_rect = Rectangle(width=1, height=0, position=[10, 0])
    canvas.add_item(null_ver_rect)

    three_by_three_quad = Rectangle(width=3, height=3, position=[15, 0])
    canvas.add_item(three_by_three_quad)

    rect = Rectangle(width=4, height=9, position=[0, 5],
                     horizontal_border='H', vertical_border='V',
                     corner='C', fill='F')
    canvas.add_item(rect)

    rect = Rectangle(width=4, height=5, position=[10, 5],
                     horizontal_border='.', vertical_border='.',
                     corner='.', fill=' ')
    canvas.add_item(rect)

    print(canvas.render(line_numbers=False))
