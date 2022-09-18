#!/bin/bash
# get specific repo tag info

curl --request GET \
  "https://hub.docker.com/v2/namespaces/persuadertechnology/repositories/getit/tags/0.2" \
  --header "Content-Type: application/json"
