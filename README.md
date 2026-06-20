# Rock Paper Scissors CGI Application

A Python CGI-based Rock Paper Scissors game deployed on Apache HTTP Server inside a Red Hat UBI 9 Docker container.

## Technologies Used

- Python
- Apache HTTPD
- CGI
- Docker
- GitHub

## Build

```bash
docker build -t python-game .
```

## Run

```bash
docker run -d -p 8080:80 --name python-game python-game
```

## Access

http://localhost:8080/cgi-bin/game.py
