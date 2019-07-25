"""Items can be placed on the Canvas."""
from __future__ import print_function


try:
    from typing import List
except ImportError:
    pass


class Item(object):
    """Defined by an arbitrary text and a position on the Canvas."""

    def __init__(self, text: str, position: List[int]=None):
        """Hold a text and a position."""
        self.text = text
        self.position = position or [0, 0]

    @property
    def bbox(self) -> List[int]:
        """Make the bbox encompass the text."""
        lines = self.text.split('\n')
        return [0, 0, max([len(l) for l in lines]), len(lines)]


class Line(Item):
    """A line between two points.

    START---+
            |
            |
            +---END
    """

    def __init__(self, start: List[int], end: List[int]):
        """Define the line by a start and an end point."""
        self.start = start
        self.end = end

    @property
    def bbox(self) -> List[int]:
        """Make the bbox encompass the entire line."""
        return [0, 0,
                abs(self.end[0] - self.start[0]) + 1,
                abs(self.end[1] - self.start[1]) + 1]

    @property
    def text(self) -> str:  # type: ignore
        """Create a string representing the line.

        1. Go half way horizontally
        2. Go straight down to the end of y
        3. Continue rest horizontally
        """
        text = ''
        first_y = self.bbox[1]
        half_x = int((self.bbox[2] - self.bbox[0]) * 0.5)
        last_y = self.bbox[3] - 1
        for row in range(self.bbox[1], self.bbox[3]):
            for column in range(self.bbox[0], self.bbox[2]):
                if row == first_y and column < half_x:
                    text += '-'
                elif row == last_y and column > half_x:
                    text += '-'
                elif row == first_y and column == half_x:
                    if self.bbox[3] - self.bbox[1] > 1:
                        text += '+'
                    else:
                        text += '-'
                elif row == last_y and column == half_x:
                    text += '+'
                elif row != first_y and row != last_y and column == half_x:
                    text += '|'
                else:
                    text += ' '
            text += '\n'
        if self.start[1] > self.end[1]:
            text = '\n'.join(text.split('\n')[::-1])
        return text

    @property
    def position(self) -> List[int]:  # type: ignore
        """Offset the position if the start is left of the end."""
        if self.start[1] <= self.end[1]:
            return self.start
        else:
            return [self.start[0], self.start[1] - self.bbox[3]]


class Rectangle(Item):
    """A rectangle.

    +---+
    |   |
    |   |
    +---+
    """

    def __init__(self, width: int, height: int, position: List[int]=None,
                 horizontal_border: str=None, vertical_border: str=None,
                 corner: str=None, fill: str=None):
        """Define the shape, position and render options for the Rectangle."""
        self.width = width
        self.height = height
        self.position = position or [0, 0]
        self.horizontal_border = horizontal_border or '-'
        self.vertical_border = vertical_border or '|'
        self.corner = corner or '+'
        self.fill = fill or ' '

    @property
    def text(self) -> str:  # type: ignore
        """Width and height have to be at least 1 in order for it to render."""
        text = ''
        if not self.width or not self.height:
            return text

        text += self._horizontal()

        for _ in range(self.height - 2):
            for column in range(self.width):
                if column == 0:
                    text += self.vertical_border
                elif column == self.width - 1:
                    text += self.vertical_border + '\n'
                else:
                    text += self.fill

        text += self._horizontal()

        return text

    def _horizontal(self) -> str:
        """Create a horizontal line."""
        text = ''
        for i in range(self.width):
            if i == 0:
                text += self.corner
            elif i == self.width - 1:
                text += self.corner + '\n'
            else:
                text += self.horizontal_border
        return text
