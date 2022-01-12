"""Websites dashboard"""

from common import DASHBOARD_TIME_SPAN
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos, Stat, Target, Threshold

dashboard = Dashboard(
    title="servers",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        Stat(
            title="stats.c4dt.org: disk usage",
            gridPos=GridPos(h=8, w=8, x=0, y=0),
            targets=[
                Target(
                    refId="A",
                    target="server.stats.disk-usage",
                )
            ],
            reduceCalc="lastNotNull",
            thresholds=[
                Threshold(index=0, color="green", value=0.0),
                Threshold(index=1, color="orange", value=75.0),
                Threshold(index=2, color="red", value=90.0),
            ],
            format=UNITS.PERCENT_FORMAT,
        ),
    ],
).auto_panel_ids()
