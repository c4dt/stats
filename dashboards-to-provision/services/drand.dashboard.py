"""drand dashboard"""

from common import DASHBOARD_TIME_SPAN, simple_graph
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos, Target

dashboard = Dashboard(
    title="drand",
    uid="drand",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        simple_graph(
            "drand.c4dt.org: connectivity",
            Target(target="drand.check-connectivity"),
            GridPos(h=8, w=24, x=0, y=0),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=2,
        ),
        simple_graph(
            "drand: memory usage",
            Target(target="drand.get-used-memory"),
            GridPos(h=8, w=12, x=0, y=8),
            UNITS.KILO_BYTES,
            frequency=1 * 60,
            alert_at=200000,
        ),
        simple_graph(
            "drand: CPU usage",
            Target(target="drand.get-cpu-percentage"),
            GridPos(h=8, w=12, x=12, y=8),
            UNITS.NO_FORMAT,
            frequency=1 * 60,
            alert_at=10,
        ),
        simple_graph(
            "drand.c4dt.org: TTY activity",
            Target(target="drand.get-tty-activity"),
            GridPos(h=8, w=24, x=0, y=16),
            UNITS.COUNTS_PER_MIN,
            frequency=1 * 60,
            alert_at=300,
        ),
    ],
).auto_panel_ids()
