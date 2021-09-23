# stats

The user setup behind [stats.c4dt.org](https://stats.c4dt.org).

At root, it contains a bunch of script to run measurement, each regularly
started by an user systemd timer, found in `.config`.
The timers output the results in a graphite database and shown in a grafana.
Both are handle by the root `docker-compose.yaml`.
To add or modify grafana's panels, look in `data/grafana`.

Deployment is done via Github Actions, which do:

- rsync of the repo to the home directory of the user on the stats' server
- stop all timers of the user
- start timers in the repo

If you need help with systemd, there is a [Systemd Cheatsheet](README.systemd.md)
