#!/usr/bin/env sh
cd $(dirname $0)

set -eu
# set -o pipefail

usage() {
        cat <<'EOF'
Usage: gitdo [-gv] [--] COMMAND... [--]
       gitdo -h

Execute COMMAND on all tracked files in a Git repository.
The file names will be provided as command line arguments to COMMAND.

Options:
  -h, --help      Print this message and exit
EOF
}

PARSED_OPTIONS=$(getopt -o h --long help -- "$@")

# Reorder the arguments based on the parsing result
eval set -- "$PARSED_OPTIONS"

force=false
while true; do
        case "$1" in
        -h|--help) usage; exit 0;;
        --) shift; break;;
        *) echo "Unknown option $1" >&2; usage >&2; exit 1;;
        esac
done

shift $((OPTIND-1))

start_backend() {
    cd backend
    python main.py
}

start_frontend() {
    cd frontend
    npm run dev
}

start_backend &
BACKEND_PID=$!

start_frontend &
FRONTEND_PID=$!

# Function to clean up processes on Ctrl+C
cleanup() {
    echo "Stopping processes..."
    kill $BACKEND_PID $FRONTEND_PID
    wait
    echo "Processes stopped."
}

trap cleanup SIGINT
# wait for kill to finish
wait
