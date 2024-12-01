from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HellowWrldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HellowWrldClass.as_view()),
    path('appp/', include('helloworldapp.urls'))
]
