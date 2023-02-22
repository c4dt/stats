"""Websites dashboard"""

from common import DASHBOARD_TIME_SPAN, simple_graph
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos, Heatmap, HeatmapColor, Target
from grafanalib.influxdb import InfluxDBTarget

dashboard = Dashboard(
    title="websites",
    uid="websites",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        simple_graph(
            "c4dt.org: loading time",
            Target(target="website.wordpress.loaded"),
            GridPos(h=8, w=8, x=0, y=0),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=3,
        ),
        simple_graph(
            "c4dt.epfl.ch: loading time",
            Target(target="website.wordpress-www.loaded"),
            GridPos(h=8, w=8, x=8, y=0),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=3,
        ),
        simple_graph(
            "showcase.c4dt.org: loading time",
            Target(target="website.showcase.loaded"),
            GridPos(h=8, w=8, x=16, y=0),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=2,
        ),
        simple_graph(
            "library.c4dt.org: loading time",
            Target(target="website.library.loaded"),
            GridPos(h=8, w=8, x=0, y=8),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=1,
        ),
        simple_graph(
            "cryptpad.c4dt.org: loading time",
            Target(target="website.cryptpad.loaded"),
            GridPos(h=8, w=8, x=8, y=8),
            UNITS.SECONDS,
            frequency=1 * 60,
            alert_at=1,
        ),
        Heatmap(
            title="websites hits",
            gridPos=GridPos(h=12, w=24, x=0, y=16),
            targets=[
                InfluxDBTarget(
                    query="""
                    from(bucket: "stats")
                      |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                      |> filter(fn: (r) => r._measurement == "website-hits")
                      |> group(columns: ["service"])
                      |> aggregateWindow(
                           every: duration(v: int(v: v.windowPeriod) / 5),
                           fn: sum,
                         )
                    """,
                ),
            ],
            dataFormat="tsbuckets",
            yBucketBound="middle",
            reverseYBuckets=True,
            color=HeatmapColor(colorScheme="interpolateReds"),
        ),
    ],
).auto_panel_ids()
