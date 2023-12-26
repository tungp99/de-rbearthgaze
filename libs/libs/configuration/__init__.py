__all__ = ["configure"]

import logging
from pathlib import Path
from pprint import pprint
from typing import Any, Dict, List

from dotenv import dotenv_values

from libs.configuration.models import Configuration


def configure(
    files: List[str] = ["../../.env.development", "../../.env.development.local"]
) -> Configuration:
    instance = Configuration()
    if instance.initialised:
        return instance

    logging.basicConfig(
        level=logging.INFO,
        # format="%(asctime)s | %(name)s | %(levelname)s\n%(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )

    content: Dict[str, Any] = {"initialised": True}

    for filepath in files:
        file = Path(filepath)
        if file.exists() and file.is_file():
            content.update(dotenv_values(file))

    pprint({"file": filepath, **content})

    return instance.fromDict(content)
