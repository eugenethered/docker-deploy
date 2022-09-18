#!/bin/bash
# get a list of repository tags

curl --request GET \
  "https://hub.docker.com/v2/namespaces/persuadertechnology/repositories/getit/tags" \
  --header "Content-Type: application/json"
