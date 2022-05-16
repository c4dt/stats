"""drand dashboard"""

from common import DASHBOARD_TIME_SPAN, simple_graph
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos

dashboard = Dashboard(
    title="drand",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        simple_graph(
            "drand.c4dt.org: connectivity",
            "drand.check-connectivity",
            GridPos(h=8, w=24, x=0, y=0),
            UNITS.SECONDS,
            frequency=1,
            alert_at=2,
        ),
        simple_graph(
            "drand: memory usage",
            "drand.get-used-memory",
            GridPos(h=8, w=12, x=0, y=8),
            UNITS.KILO_BYTES,
            frequency=1,
            alert_at=200000,
        ),
        simple_graph(
            "drand: CPU usage",
            "drand.get-cpu-percentage",
            GridPos(h=8, w=12, x=12, y=8),
            UNITS.PERCENT_FORMAT,
            frequency=1,
            alert_at=1.5,
        ),
        simple_graph(
            "drand.c4dt.org: TTY activity",
            "drand.get-tty-activity",
            GridPos(h=8, w=24, x=0, y=16),
            UNITS.COUNTS_PER_MIN,
            frequency=1,
            alert_at=150,
        ),
    ],
).auto_panel_ids()
