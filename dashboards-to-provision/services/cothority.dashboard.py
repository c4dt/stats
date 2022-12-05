"""Cothority dashboard"""

from common import DASHBOARD_TIME_SPAN, DATA_SOURCE_GRAPHITE, simple_graph
from grafanalib import formatunits as UNITS
from grafanalib.core import Dashboard, GridPos, Heatmap, HeatmapColor, Target

dashboard = Dashboard(
    title="cothority",
    uid="cothority",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        simple_graph(
            "cothority: transfer a coin",
            Target(target="cothority.transfer-coin"),
            GridPos(h=8, w=12, x=0, y=8),
            UNITS.SECONDS,
            frequency=30 * 60,
            alert_at=10,
        ),
        simple_graph(
            "cothority: call BEvm",
            Target(target="cothority.call-bevm"),
            GridPos(h=8, w=12, x=12, y=8),
            UNITS.SECONDS,
            frequency=30 * 60,
            alert_at=4,
        ),
        Heatmap(
            title="cothority: leader",
            gridPos=GridPos(h=8, w=24, x=0, y=16),
            targets=[
                Target(
                    refId="A",
                    target="aliasSub(aliasByNode({}, 2), '_', '.')".format(
                        "cothority.get-leader.*"
                    ),
                ),
            ],
            dataSource=DATA_SOURCE_GRAPHITE,
            color=HeatmapColor(mode="opacity"),
            dataFormat="tsbuckets",
            reverseYBuckets=True,
            yBucketBound="middle",
        ),
    ],
).auto_panel_ids()
