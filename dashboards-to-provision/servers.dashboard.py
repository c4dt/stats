"""Websites dashboard"""

from common import DASHBOARD_TIME_SPAN, DATA_SOURCE_INFLUXDB
from grafanalib import formatunits as UNITS
from grafanalib.core import (
    NULL_AS_NULL,
    OP_AND,
    RTYPE_LAST,
    Alert,
    AlertCondition,
    Dashboard,
    GaugePanel,
    Graph,
    GreaterThan,
    GridPos,
    Repeat,
    Template,
    Templating,
    Threshold,
    TimeRange,
)
from grafanalib.influxdb import InfluxDBTarget


# the 'every' in the 'aggregateWindow' will always aggregate to 800 points,
# no matter the range being shown.
def target(server_name: str) -> InfluxDBTarget:
    """Generate Target for disk usage on given server"""
    return InfluxDBTarget(
        refId="A",
        query=f"""
          from(bucket: "stats")
            |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
            |> filter(fn: (r) => r._measurement == "disk")
            |> filter(fn: (r) => r.host == "{server_name}")
            |> filter(fn: (r) => r._field == "used_percent")
            |> keep(columns: ["_time", "_value", "path"])
            |> aggregateWindow(every: duration(v:(uint(v: v.timeRangeStop) -
               uint(v: v.timeRangeStart))/uint(v: 800)), fn: mean)
        """,
    )


DATA_SOURCE = DATA_SOURCE_INFLUXDB

HOSTS = [
    "srv-epfl-1",
    "srv-switch-ls-1",
    "srv-switch-ls-2",
    "srv-switch-zh-1",
]

dashboard = Dashboard(
    title="servers",
    uid="servers",
    time=DASHBOARD_TIME_SPAN,
    templating=Templating(
        list=[
            Template(
                name="server",
                multi=True,
                includeAll=True,
                query="""
                  import "influxdata/influxdb/schema"
                  schema.tagValues(bucket: "stats", tag: "host")
                """,
                dataSource=DATA_SOURCE,
            ),
        ]
    ),
    panels=[
        GaugePanel(
            title="$server: disk usage",
            gridPos=GridPos(h=8, w=32, x=0, y=0),
            targets=[target("$server")],
            dataSource=DATA_SOURCE,
            calc="lastNotNull",
            thresholds=[
                Threshold(index=0, color="green", value=0.0),
                Threshold(index=1, color="orange", value=75.0),
                Threshold(index=2, color="red", value=90.0),
            ],
            format=UNITS.PERCENT_FORMAT,
            thresholdMarkers=False,
            repeat=Repeat(direction="v", variable="server"),
        )
    ]
    + [
        # one graph/serie per host to actually generate alerts
        Graph(
            title=f"{host}: trigger disk usage alert",
            gridPos=GridPos(h=0, w=0, x=0, y=0),  # invisible
            targets=[target(host)],
            dataSource=DATA_SOURCE,
            nullPointMode=NULL_AS_NULL,
            alert=Alert(
                name=f"{host} disk nearly full",
                message=f"{host} disk nearly full",
                frequency="10s",
                gracePeriod="1m",
                alertConditions=[
                    AlertCondition(
                        target=target(host),
                        timeRange=TimeRange("1m", "now"),
                        evaluator=GreaterThan(90),
                        operator=OP_AND,
                        reducerType=RTYPE_LAST,
                    ),
                ],
            ),
        )
        for host in HOSTS
    ],
).auto_panel_ids()
