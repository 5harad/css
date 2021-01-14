#!/usr/bin/env python3
"""Build exercise notebook from answer notebook by removing answers"""

import argparse
import json


def censor_nb(nb):
    """Censor a json object of notebook nb

    Args:
      nb: notebook parsed as a python object

    Returns:
      censors python object nb in-place
    """
    for cell in nb["cells"]:
      if cell["cell_type"] != "code":
        continue
      cell["execution_count"] = 0
      cell["outputs"] = []
      censored_source = []
      censor = False
      for line in cell["source"]:
        if "START" in line:
          censor = True
        if not censor:
          censored_source.append(line)
        if "END" in line:
          censor = False
      cell["source"] = censored_source


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(
      description="Create exercise version of notebooks"
    )
    parser.add_argument("--source",
                        "-s",
                        help="source (answer) notebook",
                        required=True)
    flags = parser.parse_args()

    with open(flags.source, "r") as f:
        nb = json.load(f)

    censor_nb(nb)

    if "answers" in flags.source:
      target = flags.source.replace("answers", "exercises")
    else:
      target = flags.source.replace(".ipynb", "-exercises.ipynb")

    with open(target, "w") as f:
        json.dump(nb, f)
