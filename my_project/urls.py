"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^EMPLOYEE/sel',views.employee_sel),
    url(r'^EMPLOYEE',views.employee),
    url(r'^DEPARTMENT/sel',views.department_sel),
    url(r'^DEPARTMENT',views.department),
    url(r'^DEPT_LOCATION/sel',views.dept_location_sel),
    url(r'^DEPT_LOCATION',views.dept_location),
    url(r'^PROJECT/sel',views.project_sel),
    url(r'^PROJECT',views.project),
    url(r'^WORKS_ON/sel',views.works_on_sel),
    url(r'^WORKS_ON',views.works_on),
    url(r'^DEPENDENT/sel',views.dependent_sel),
    url(r'^DEPENDENT',views.dependent),
    url(r'^init',views.init),
    # url(r'^enter',views.enter),
]
