# Rewrite forge service

Turns plain text into a new style.
For example “pirate”, “haiku”, or “formal”.
The service responds with both the original and transformed text.

## Requirements

Docker version 28.2.2 or higher

## Post request

```json
{
    "text": "<Text to rewrite>",
    "style": "<Style>"
}
```

## Example docker-compose

```yaml
services:
  rewrite-forge:
    image: rewrite-forge-image
    build:
      context: .
    container_name: rewrite-forge-api-server
    restart: always
    networks:
      - rw_fg_net
    ports:
      - 8000:8000
    environment:
      OPENAI_API_KEY: <Open AI API Key>
      ANTHROPIC_API_KEY: <Anthropic API Key>
  redis:
    image: redis
    container_name: redis-server
    command: redis-server
    restart: always
    networks:
      - rw_fg_net

networks:
  rw_fg_net:
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/16
```

## Adapter

The preference of API keys is:

1. OPENAI_API_KEY
2. ANTHROPIC_API_KEY

## The command to fire-up the service

```console
docker compose build; docker compose up -d
```
