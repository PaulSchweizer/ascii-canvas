"""Aggregate items into a string canvas."""
from __future__ import print_function


class Canvas(object):
    """Aggregate string objects onto a 2D string canvas."""

    BLANK = ' '

    def __init__(self):
        """Hold a list of Items."""
        self.items = []

    def add_item(self, item, index=-1):
        """Insert the item at the given index."""
        self.items.insert(index, item)

    @property
    def bbox(self):
        """Encompass all items in the bounding box."""
        bbox = [0, 0, 0, 0]
        for item in self.items:
            if item.position[0] + item.bbox[2] < bbox[0]:
                bbox[0] = item.position[0] + item.bbox[2]
            elif item.position[0] + item.bbox[2] > bbox[2]:
                bbox[2] = item.position[0] + item.bbox[2]
            if item.position[1] + item.bbox[3] < bbox[1]:
                bbox[1] = item.position[1] + item.bbox[3]
            elif item.position[1] + item.bbox[3] > bbox[3]:
                bbox[3] = item.position[1] + item.bbox[3]
        return bbox

    def render(self):
        """Fill it with placeholders and add the items to it."""
        canvas = []
        for row in range(self.bbox[1] + self.bbox[3]):
            canvas.append([self.BLANK
                           for c in range(self.bbox[0] + self.bbox[2])])
        for item in self.items:
            for i, line in enumerate(item.text.split('\n')):
                row = item.position[1] + i
                start = item.position[0]
                for j, s in enumerate(line):
                    if s != ' ':
                        canvas[row][start + j] = s
        for i, row in enumerate(canvas):
            row.insert(0, '{0:4d} | '.format(i))
        return '\n'.join([''.join(row) for row in canvas])
