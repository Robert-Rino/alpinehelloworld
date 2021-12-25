# Local run
`docker-compose up`

# Release
- Build (Heroku only support linux/amd64 platform build)

`docker buildx build --platform linux/amd64 -t evening-reaches-68081 .`

- Tag

`docker tag evening-reaches-68081 registry.heroku.com/evening-reaches-68081/web`

- Push

`docker push registry.heroku.com/evening-reaches-68081/web`

- Relase

`heroku container:release web` (cli)

(REST API)
```shell
HEROKU_APP_ID=evening-reaches-68081
HEROKU_IMAGE_ID=$(docker inspect registry.heroku.com/evening-reaches-68081/web --format={{.Id}})
HEROKU_TOKEN=$(heroku auth:token)


curl -X PATCH https://api.heroku.com/apps/$APP_ID/formation \
  -d '{
  "updates": [
    {
      "type": "web",
      "docker_image": $HEROKU_IMAGE_ID
    }
  ]
}' \
  -H "Content-Type: application/json" \
  -H "Accept: application/vnd.heroku+json; version=3.docker-releases" \
  -H "Authorization: Bearer $HEROKU_TOKEN"
```

# Heroku
## Generate Heroku token

`heroku authorizations:create  -d 'getting started token'`

## Fetch token
`heroku auth:token`


# K8s
```shell
export IMAGE=ghcr.io/robert-rino/heroku-alpinehelloworld
export IMAGE_TAG=sha-5515f99

kustomize edit set image IMAGE:TAG=$IMAGE:$IMAGE_TAG
kustomize edit add configmap k8s-helloworld-configmap --from-literal=version=$IMAGE_TAG --disableNameSuffixHash

kustomize build . -o dev.yaml

kubectl apply -f dev.yaml
```
