# Docker Deploy
Example of how to deploy docker container.

## Docker Hub without any tag
1. Run `./docker-image-tag-info.sh` (simulation/docker/api). Should have this output:
```
{"message":"tag '0.1' not found","errinfo":{"namespace":"persuadertechnology","repository":"getit","tag":"0.1"}}
```
2. Build the image locally `docker build . -t persuadertechnology/getit:0.1 && docker image prune --filter label=stage=BUILDER`
3. `docker images` (to verfify the locally built image)
4. `docker push persuadertechnology/getit:0.1`

## Docker Hub with existing tag
1. Run `./docker-image-tag-info.sh` (simulation/docker/api). Should have this output:
2. Within the repose there should be `"tag_status": "active"` & `tag_last_pushed`