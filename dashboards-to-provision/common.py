"""Shared code for the dashboards"""

from typing import Union

from grafanalib.core import (
    NULL_AS_NULL,
    OP_AND,
    RTYPE_AVG,
    Alert,
    AlertCondition,
    Graph,
    GreaterThan,
    GridPos,
    Target,
    Time,
    TimeRange,
    YAxes,
    YAxis,
)
from grafanalib.influxdb import InfluxDBTarget

DASHBOARD_TIME_SPAN = Time("now-7d", "now")

DATA_SOURCE_GRAPHITE = "Graphite"
DATA_SOURCE_INFLUXDB = "InfluxDB"


def simple_graph(
    title: str,
    target: Union[Target, InfluxDBTarget],
    pos: GridPos,
    y_axis_format: str,
    *,
    frequency: int,
    alert_at: Union[int, float],
) -> Graph:
    """Return a Graph with a single target and its alert value."""

    target.refId = "A"
    data_source = (
        DATA_SOURCE_INFLUXDB
        if isinstance(target, InfluxDBTarget)
        else DATA_SOURCE_GRAPHITE
    )

    return Graph(
        title=title,
        gridPos=pos,
        targets=[target],
        dataSource=data_source,
        nullPointMode=NULL_AS_NULL,
        yAxes=YAxes(
            YAxis(format=y_axis_format, min=0, max=alert_at * 1.5),
        ),
        alert=Alert(
            name=title,
            message=title,
            frequency=f"{frequency}m",
            gracePeriod=f"{frequency*4}m",
            alertConditions=[
                AlertCondition(
                    target=target,
                    timeRange=TimeRange(f"{frequency*4}m", "now"),
                    evaluator=GreaterThan(alert_at),
                    operator=OP_AND,
                    reducerType=RTYPE_AVG,
                ),
            ],
        ),
    )
