[![Version](https://img.shields.io/pypi/v/ascii_canvas.svg)](https://pypi.org/project/ascii_canvas/)
[![Build Status](https://travis-ci.org/PaulSchweizer/ascii-canvas.svg?branch=master)](https://travis-ci.org/PaulSchweizer/ascii-canvas) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1e97852797d14c679d7c89337b022c92)](https://www.codacy.com/app/paulschweizer/ascii-canvas?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PaulSchweizer/ascii-canvas&amp;utm_campaign=Badge_Grade)


# Treat strings like Items on a 2D Canvas

With this primitive library you can do things like this:

```python
from ascii_canvas.canvas import Canvas
from ascii_canvas.item import Item, Line

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
print(canvas.draw())
```

Which results in this output:

```
    0+-----+                         +-+
    1|Hello|----+               +----|!|
    2+-----+    |               |    +-+
    3           |               |
    4           |               |
    5           |    +-----+    |
    6           +----|World|----+
    7                +-----+
```
