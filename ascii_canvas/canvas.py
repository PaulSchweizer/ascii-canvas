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

    def render(self, line_numbers=False):
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
        if line_numbers:
            for i, row in enumerate(reversed(canvas)):
                if i == len(canvas) - 1:
                    row.insert(0, '{0:4d} ^'.format(i))
                else:
                    row.insert(0, '{0:4d} |'.format(i))

            canvas.append([' ' * 5] +
                          ['+'] +
                          ['-' * (self.bbox[0] + self.bbox[2] - 1)] +
                          ['>'])
            horizontal_numbers = [
                str(n) for n in range(self.bbox[0] + self.bbox[2])]
            for index in range(len(horizontal_numbers[-1])):
                hor_number_row = [" " * 6]
                for number in horizontal_numbers:
                    if index < len(number):
                        hor_number_row.append(number[index])
                    else:
                        hor_number_row.append(" ")
                canvas.append(hor_number_row)

        return '\n'.join([''.join(row) for row in canvas])
