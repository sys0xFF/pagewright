#!/usr/bin/env python3
"""Serve a generated site locally so you can open it in a browser / screenshot it.

Usage:
    python preview.py path/to/site            # serves on first free port from 5500
    python preview.py path/to/site --port 8080 --open

Stdlib only. Ctrl+C to stop.
"""
import argparse
import contextlib
import functools
import http.server
import socket
import sys
import webbrowser
from pathlib import Path


def free_port(start: int) -> int:
    for p in range(start, start + 50):
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:
                return p
    return start


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("directory")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--open", action="store_true", help="open in the default browser")
    args = ap.parse_args()

    root = Path(args.directory).resolve()
    if not (root / "index.html").exists():
        print(f"! no index.html in {root}", file=sys.stderr)
        return 1

    port = args.port or free_port(5500)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    url = f"http://127.0.0.1:{port}/"
    print(f"serving {root}\n  -> {url}\n(Ctrl+C to stop)")
    if args.open:
        webbrowser.open(url)
    try:
        http.server.ThreadingHTTPServer(("127.0.0.1", port), handler).serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
