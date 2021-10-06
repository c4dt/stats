# Systemctl Cheatsheet

All measurements are triggered by systemctl. Here are the most common
commands when working with it:

You can get a list of all services running for graphite like this:

```bash
systemctl --user list-units '*graphite*'
```

To get a log of what is happening:

```bash
journalctl --user --follow --full --boot
```

Restart one of the services:

```
systemctl --user restart `timer_type@name_of_service`
```

Stop one of the services:

```bash
systemctl --user stop `timer_type@name_of_service`
```
