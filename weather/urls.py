from django.urls import path
from weather import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='index')
]
