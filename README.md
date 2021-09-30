# stats

The user setup behind [stats.c4dt.org](https://stats.c4dt.org).

At root, it contains a bunch of script to run measurement, each regularly
started by an user systemd timer, found in `.config`.
The timers output the results in a graphite database and shown in a grafana.
Both are handle by the root `docker-compose.yaml`.
To add or modify grafana's panels, look in `data/grafana`.

Deployment is done via Github Actions, it's simply a rsync of the repo to
the home directory of the user on the stats' server.

## Systemctl

All measurements are triggered by systemctl. If you remove one of the targets
in `.config/systemd/user/timers.targets.wants`, you'll have to remove it by hand:

```bash
systemctl --user stop `timer_type@name_of_service`
```

You can get a list of all services running for graphite like this:

```bash
systemctl --user list-units '*graphite*'
```

And to restart one of the services:

```
systemctl --user restart `timer_type@name_of_service`
```

To get a log of what is happening:

```bash
journalctl --user --follow --full --boot
```
