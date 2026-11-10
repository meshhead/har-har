# app.py
# Single-file Flask app for Render
# requirements.txt (add these on Render / in your repo):
#   flask==3.0.3
#   gunicorn==22.0.0
#
# Render start command: gunicorn app:app

import os
from flask import Flask, Response

app = Flask(__name__)

REAPER = r"""
       ________________                              _______________
      /                \                            / /           \ \
     / /          \ \   \                          |    -    -       \
     |                  |                          | /        -   \  |
    /                  /                           \                 \
   |      ___\ \| | / /                             \____________  \  \
   |      /           |                             |            \    |
   |      |     __    |                             |             \   \
  /       |       \   |                             |              \  |
  |       |        \  |                             | ====          | |
  |       |       __  |                             | (o-)      _   | |
  |      __\     (_o) |                             /            \  | |
  |     |             |     Heh Heh Heh            /            ) ) | |
   \    ||             \      /      Huh Huh Huh  /             ) / | |
    |   |__             \    /                \  |___            - |  |
    |   |           (*___\  /                  \    *'             |  |
    |   |       _     |    /                    \  |____           |  |
    |   |    //_______|                             ####\          |  |
    |  /       |_|_|_|___/\                        ------          |_/
     \|       \ -         |                        |                |
      |       _----_______/                        \_____           |
      |      /                                          \           |
      |_____/                                            \__________|

                   WE SEE YOU AND WE KNOW WHAT YOU DID
"""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>.</title>
<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background: #000;
    overflow: hidden;
  }
  body {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  pre {
    margin: 0;
    color: #e6e6e6;
    font-family: "Courier New", Courier, monospace;
    font-size: 12px;
    line-height: 1.05;
    white-space: pre;
    /* keeps it decently scaled on small screens */
    transform-origin: center center;
  }
  @media (max-width: 900px) {
    pre { font-size: 9px; }
  }
  @media (max-width: 600px) {
    pre { font-size: 6px; }
  }
  @media (max-width: 400px) {
    pre { font-size: 4px; }
  }
</style>
</head>
<body>
<pre>__REAPER__</pre>
</body>
</html>
"""


@app.route("/")
def index():
    # Escape HTML special chars so the ASCII renders literally
    safe = (
        REAPER.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    page = HTML.replace("__REAPER__", safe.lstrip("\n"))
    return Response(page, mimetype="text/html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
