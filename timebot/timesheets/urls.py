from rest_framework import routers
from .api import TimesheetViewset, WorkViewset

router = routers.DefaultRouter()
router.register('api/timesheets', TimesheetViewset, 'timesheets')
router.register('api/works', WorkViewset, 'works')

urlpatterns = router.urls