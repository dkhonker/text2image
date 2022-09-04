from typing import List
import shutil
from huggingface_hub import notebook_login
import translators as ts


def parse_lyrics(path: str, prompt: str, zh2en: bool) -> List[str]:
    """
    Parses the lyrics plain file into a list of verses
    Args:
        path: The lyrics path
        prompt: Extra params
    Returns:
        A list of verses
    """
    with open(path) as f:
        verses = f.readlines()

    verses_clean = []
    for verse in verses:
        verse = verse.replace("\n", "")
        verse = verse.replace(".", "")
        verse = verse.replace("。", "")
        if zh2en:
            verse=ts.google(verse)
        if verse:
            verse += f" {prompt}"
            verses_clean.append(verse)
    return verses_clean
