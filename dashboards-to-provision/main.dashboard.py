"""main dashboard"""

from common import DASHBOARD_TIME_SPAN
from grafanalib.core import (
    ALERTLIST_STATE_ALERTING,
    ALERTLIST_STATE_EXECUTION_ERROR,
    ALERTLIST_STATE_NO_DATA,
    ALERTLIST_STATE_PAUSED,
    ALERTLIST_STATE_PENDING,
    AlertList,
    Dashboard,
    DashboardList,
    GridPos,
)

dashboard = Dashboard(
    title="main",
    time=DASHBOARD_TIME_SPAN,
    panels=[
        AlertList(
            title="errors",
            id=1,
            gridPos=GridPos(h=12, w=12, x=0, y=0),
            stateFilter=[
                ALERTLIST_STATE_ALERTING,
                ALERTLIST_STATE_NO_DATA,
                ALERTLIST_STATE_EXECUTION_ERROR,
            ],
            onlyAlertsOnDashboard=False,
        ),
        AlertList(
            title="warnings",
            id=2,
            gridPos=GridPos(h=8, w=12, x=0, y=12),
            stateFilter=[
                ALERTLIST_STATE_PAUSED,
                ALERTLIST_STATE_PENDING,
            ],
            onlyAlertsOnDashboard=False,
        ),
        DashboardList(
            gridPos=GridPos(h=12, w=12, x=12, y=0),
            id=3,
            showSearch=True,
        ),
    ],
)
# TODO auto_panel_ids() when weaveworks/grafanalib#441 is released
