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

`heroku container:release web`
