
from collections import Counter
from typing import Any
from PIL import Image



class ImageColors:
    def __init__(self, image: str):

        self._image_path = image
        self._image = Image.open(image)

        # Resize the image to improve performance
        self._image = self._image.resize((100, 100))
        self._image = self._image.convert('RGB')

        # Count the occurrences of each color
        self._color_counter = Counter(self._image.getdata())

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def total(self):
        return self._color_counter.total()

    @property
    def count(self):
        return self._color_counter.__len__()

    @property
    def colors(self) -> Any:
        return self._image.getdata()

    @property
    def most_common(self, count: int = None) -> list[tuple[tuple[int], int]]:
        '''
        count: int
            count == None, default = cls.total
        '''
        return self._color_counter.most_common(count
                                               if count is not None
                                               else self._color_counter.total())

