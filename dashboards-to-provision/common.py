"""Shared code for the dashboards"""

from typing import Union

from grafanalib.core import (
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

DASHBOARD_TIME_SPAN = Time("now-7d", "now")


def simple_graph(
    title: str,
    target: str,
    pos: GridPos,
    y_axis_format: str,
    *,
    frequency: int,
    alert_at: Union[int, float],
) -> Graph:
    """Return a Graph with a single target and its alert value."""

    return Graph(
        title=title,
        gridPos=pos,
        targets=[
            Target(
                refId="A",
                target=target,
            ),
        ],
        yAxes=YAxes(
            YAxis(format=y_axis_format, min=0, max=alert_at * 1.5),
        ),
        alert=Alert(
            name=title,
            message=title,
            frequency=f"{frequency}m",
            gracePeriod=f"{frequency*2}m",
            alertConditions=[
                AlertCondition(
                    target=Target(refId="A"),
                    timeRange=TimeRange(f"{frequency*2}m", "now"),
                    evaluator=GreaterThan(alert_at),
                    operator=OP_AND,
                    reducerType=RTYPE_AVG,
                ),
            ],
        ),
    )
