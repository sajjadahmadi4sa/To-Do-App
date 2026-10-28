from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'


router = DefaultRouter()
router.register('tasks',views.TaskViewSet,basename='task')

urlpatterns = router.urls




# urlpatterns = [
#     path('task/',view.tasklist,name='task_list'),
# ]