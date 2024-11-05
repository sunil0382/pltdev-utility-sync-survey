#!/bin/bash
python server.py &
uvicorn rest_server:app --reload --host 0.0.0.0 --port 80