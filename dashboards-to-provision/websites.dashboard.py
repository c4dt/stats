"""Websites dashboard"""

from common import DASHBOARD_TIME_SPAN, simple_graph
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos

dashboard = Dashboard(
    title="websites",
    uid="websites",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        simple_graph(
            "c4dt.org: loading time",
            "website.wordpress.loaded",
            GridPos(h=8, w=8, x=0, y=0),
            UNITS.SECONDS,
            frequency=1,
            alert_at=3,
        ),
        simple_graph(
            "www.c4dt.org: loading time",
            "website.wordpress-www.loaded",
            GridPos(h=8, w=8, x=8, y=0),
            UNITS.SECONDS,
            frequency=1,
            alert_at=3,
        ),
        simple_graph(
            "showcase.c4dt.org: loading time",
            "website.showcase.loaded",
            GridPos(h=8, w=8, x=16, y=0),
            UNITS.SECONDS,
            frequency=1,
            alert_at=2,
        ),
        simple_graph(
            "library.c4dt.org: loading time",
            "website.library.loaded",
            GridPos(h=8, w=8, x=0, y=8),
            UNITS.SECONDS,
            frequency=1,
            alert_at=1,
        ),
        simple_graph(
            "cryptpad.c4dt.org: loading time",
            "website.cryptpad.loaded",
            GridPos(h=8, w=8, x=8, y=8),
            UNITS.SECONDS,
            frequency=1,
            alert_at=1,
        ),
        simple_graph(
            "matrix.c4dt.org: loading time",
            "website.matrix.loaded",
            GridPos(h=8, w=8, x=16, y=8),
            UNITS.SECONDS,
            frequency=1,
            alert_at=1,
        ),
    ],
).auto_panel_ids()
