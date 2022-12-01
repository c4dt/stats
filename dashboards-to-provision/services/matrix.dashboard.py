"""matrix dashboard"""

from common import DASHBOARD_TIME_SPAN, simple_graph
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos, Target
from grafanalib.influxdb import InfluxDBTarget

dashboard = Dashboard(
    title="matrix",
    uid="matrix",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        simple_graph(
            "matrix.c4dt.org: loading time",
            Target(target="website.matrix.loaded"),
            GridPos(h=8, w=12, x=0, y=0),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=1,
        ),
        simple_graph(
            "tequila.epfl.ch: loading time",
            InfluxDBTarget(
                query="""
                from(bucket: "stats")
                    |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                    |> filter(fn: (r) => r._measurement == "exec")
                    |> aggregateWindow(every: v.windowPeriod, fn: mean)
                """,
            ),
            GridPos(h=8, w=12, x=12, y=0),
            UNITS.SECONDS,
            frequency=10,
            alert_at=1,
        ),
    ],
).auto_panel_ids()
