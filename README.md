# stats

The user setup behind [stats.c4dt.org](https://stats.c4dt.org).

At root, it contains a bunch of script to run measurement, each regularly
started by a user systemd timer, found in `.config`.
The timers output the results in a graphite database and shown in a grafana.
Both are handle by the root `docker-compose.yaml`.
To add or modify grafana's panels, look in `data/grafana`.

Deployment is done via ansible: [stats role](https://github.com/c4dt/ansible-config/tree/main/playbooks/roles/stats)

If you need help with systemd, there is a [Systemd Cheatsheet](README.systemd.md)

## Testing

To test the new values, the easiest way is to do the following:

- ssh to the stats-server, then

```bash
sudo -iu stats
git pull
git checkout your_branch
make
```

Once you've finished testing, don't forget to

```bash
git checkout main
make
```

And then re-apply ansible.
