[![Version](https://img.shields.io/pypi/v/ascii_canvas.svg)](https://pypi.org/project/ascii_canvas/)

# Treat Strings like Items on a 2D Canvas

With this primitive library you can do things like this:

```python
from ascii_canvas import canvas
from ascii_canvas import item

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
print(canvas_.render())
```

Which results in this output:

```
+-----+                         +-+
|Hello|----+               +----|!|
+-----+    |               |    +-+
           |               |
           |               |
           |    +-----+    |
           +----|World|----+
                +-----+
```
