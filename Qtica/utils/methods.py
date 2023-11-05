import unicodedata


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
