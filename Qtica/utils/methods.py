import unicodedata
from PySide6.QtCore import Qt


def slugify(original: str) -> str:
    """
    Make a string url friendly. Useful for creating routes for navigation.

    >>> slugify("What's    up?")
    'whats-up'

    >>> slugify("  Mitä kuuluu?  ")
    'mitä-kuuluu'
    """
    slugified = original.strip()
    slugified = " ".join(slugified.split())  # Remove extra spaces between words
    slugified = slugified.lower()
    # Remove unicode punctuation
    slugified = "".join(
        character
        for character in slugified
        if not unicodedata.category(character).startswith("P")
    )
    slugified = slugified.replace(" ", "-")

    return slugified


def qt_corner_to_edge(corner: Qt.Corner,
                      default: Qt.Edge = Qt.Edge(0)) -> Qt.Edge:
    return {
        Qt.Corner.TopLeftCorner: Qt.Edge.LeftEdge | Qt.Edge.TopEdge,
        Qt.Corner.TopRightCorner: Qt.Edge.RightEdge | Qt.Edge.TopEdge,
        Qt.Corner.BottomLeftCorner: Qt.Edge.LeftEdge | Qt.Edge.BottomEdge,
        Qt.Corner.BottomRightCorner: Qt.Edge.RightEdge | Qt.Edge.BottomEdge
    }.get(corner, default)