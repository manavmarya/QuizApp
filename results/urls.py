from django.urls import path
from .views import add_edit_result, view_result

app_name = 'results'
urlpatterns = [ path('results/', add_edit_result, name='add_edit_result'),
                path('results/<pk>/view', view_result, name='view_result'),
            ]