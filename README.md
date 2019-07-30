[![Version](https://img.shields.io/pypi/v/ascii_canvas.svg)](https://pypi.org/project/ascii_canvas/)
[![Build Status](https://travis-ci.org/PaulSchweizer/ascii-canvas.svg?branch=master)](https://travis-ci.org/PaulSchweizer/ascii-canvas) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1e97852797d14c679d7c89337b022c92)](https://www.codacy.com/app/paulschweizer/ascii-canvas?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PaulSchweizer/ascii-canvas&amp;utm_campaign=Badge_Grade)[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/1e97852797d14c679d7c89337b022c92)](https://www.codacy.com/app/paulschweizer/ascii-canvas?utm_source=github.com&utm_medium=referral&utm_content=PaulSchweizer/ascii-canvas&utm_campaign=Badge_Coverage)


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
print(canvas_.draw())
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

# Type hints

The library contains Python3.6-style type hints. For lower Python versions the hints are however stripped on the fly with [strip-hints](https://github.com/abarker/strip-hints)!, making ascii-canvas compatible all the way down to Python 2.6.
Please note that in Python < 3.6 you can NOT import the classes directly due to the stripping of the type hints, so stick with the way that the example imports the module.
