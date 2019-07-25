from ascii_canvas import canvas
from ascii_canvas import item


def test_render_items_on_canvas():
    """Render the added items correctly."""
    canvas_ = canvas.Canvas()

    rect_a = item.Item('+-----+\n|Hello|\n+-----+', position=[0, 0])
    rect_b = item.Item('+-----+\n|World|\n+-----+', position=[16, 5])
    rect_c = item.Item('+-+\n|!|\n+-+', position=[32, 0])
    line_a = item.Line(start=[7, 1], end=[15, 6])
    line_b = item.Line(start=[23, 6], end=[31, 1])

    canvas_.add_item(rect_a)
    canvas_.add_item(rect_b)
    canvas_.add_item(rect_c)
    canvas_.add_item(line_a)
    canvas_.add_item(line_b)

    rendered = canvas_.render(line_numbers=False)
    assert rendered == '\
+-----+                         +-+\n\
|Hello|----+               +----|!|\n\
+-----+    |               |    +-+\n\
           |               |       \n\
           |               |       \n\
           |    +-----+    |       \n\
           +----|World|----+       \n\
                +-----+            '

    rendered = canvas_.render(line_numbers=True)
    assert rendered == '\
   7 ^+-----+                         +-+\n\
   6 ||Hello|----+               +----|!|\n\
   5 |+-----+    |               |    +-+\n\
   4 |           |               |       \n\
   3 |           |               |       \n\
   2 |           |    +-----+    |       \n\
   1 |           +----|World|----+       \n\
   0 |                +-----+            \n\
     +---------------------------------->\n\
      01234567891111111111222222222233333\n\
                0123456789012345678901234'


def test_rectangle():
    """Render a bunch of rectangles."""
    canvas_ = canvas.Canvas()
    canvas.Canvas.BLANK = '.'

    null_rect = item.Rectangle(width=0, height=0)
    canvas_.add_item(null_rect)

    null_hor_rect = item.Rectangle(width=0, height=1, position=[5, 0])
    canvas_.add_item(null_hor_rect)

    null_ver_rect = item.Rectangle(width=1, height=0, position=[10, 0])
    canvas_.add_item(null_ver_rect)

    three_by_three_quad = item.Rectangle(width=3, height=3, position=[15, 0])
    canvas_.add_item(three_by_three_quad)

    rect = item.Rectangle(width=4, height=9, position=[0, 5],
                     horizontal_border='H', vertical_border='V',
                     corner='C', fill='F')
    canvas_.add_item(rect)

    rect = item.Rectangle(width=4, height=5, position=[10, 5],
                     horizontal_border='~', vertical_border='/',
                     corner='#', fill=' ')
    canvas_.add_item(rect)

    assert canvas_.render(line_numbers=False) == '''\
...............+-+
...............|.|
...............+-+
..................
..................
CHHC......#~~#....
VFFV....../../....
VFFV....../../....
VFFV....../../....
VFFV......#~~#....
VFFV..............
VFFV..............
VFFV..............
CHHC..............
..................'''
