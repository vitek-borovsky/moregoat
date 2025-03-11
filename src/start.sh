#!/usr/bin/env sh
cd $(dirname $0)

set -eu
# set -o pipefail

usage() {
        cat <<'EOF'
Usage: ./start.sh [--verbose]
       ./start.sh [-h --help]

It's expected that minikube is already running

Options:
  -h, --help      Print this message and exit
EOF
}

PARSED_OPTIONS=$(getopt -o h --long help,verbose -- "$@")

# Reorder the arguments based on the parsing result
eval set -- "$PARSED_OPTIONS"

force=false
while true; do
        case "$1" in
        -h|--help) usage; exit 0;;
        --verbose) set -x; shift;;
        --) shift; break;;
        *) echo "Unknown option $1" >&2; usage >&2; exit 1;;
        esac
done

shift $((OPTIND-1))

sendNotification() {
    local message=$1
    notify-send "$message"
}


# start minikube if it's not running
minikube status | grep -q "Running" || minikube start

# set docker daemont to minikube-docker
eval $(minikube docker-env)

# build images
docker build -t moregoat-backend:latest backend/ --network=host \
    || (sendNotification "Failed to build backend image" && exit 1)
docker build -t moregoat-frontend:latest frontend/ --network=host \
    || (sendNotification "Failed to build frontend image" && exit 1)

# Force restart all pods
# if their img changed but deployment stayed the same
# the change won't be registred and old pods will stay active (thouse based on old img)
kubectl delete deployments --all
kubectl delete service --all

for file in k8s/*.yaml; do
    kubectl apply -f $file
done

CONTAINER_COUNT=2
while [ $(kubectl get pods --no-headers | grep -c "Running") -lt $CONTAINER_COUNT ]; do
    echo "Waiting for containers to start..."
    sleep 5
done

kubectl port-forward svc/moregoat-service 5173:5173 &
moregoat_service_PID=$!
kubectl port-forward svc/moregoat-server-service 5000:5000 &
moregoat_server_service_PID=$!

# # Function to clean up processes on Ctrl+C
cleanup() {
    echo "Stopping port-forwards..."
    kill $moregoat_service_PID $moregoat_server_service_PID
    wait
    echo "Port-forwarding terminated."
}

trap cleanup SIGINT

sendNotification "New version started succesfully"

wait
