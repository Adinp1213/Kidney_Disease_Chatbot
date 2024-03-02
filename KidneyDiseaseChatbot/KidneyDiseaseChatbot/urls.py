"""
URL configuration for KidneyDiseaseChatbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "home"),
    path("login/", views.login , name = "login"),
    path("create/", views.create , name = "create"),
    path("failed/", views.failed , name = "failed"),
    path("logout/", views.logout , name = "logout"),
    path("logout_2/", views.logout_2 , name = "logout_2"),
    path("login_admin/", views.login_admin , name = "login_admin"),
    path("admin_home/", views.admin_home , name = "admin_home"),
    path("view_users/", views.view_users , name = "view_users"),
    path("view_feedbacks/", views.view_feedbacks , name = "view_feedbacks"),
    path("give_feedback/", views.give_feedback , name = "give_feedback"),
    # path("ckd_detection/", views.ckd_detection , name = "ckd_detection"),
    path("demo/", views.demo , name = "demo"),
    path('chatbot/', views.chatbot, name='chatbot'),
    path("previous_detection/", views.previous_detection , name = "previous_detection"),
    path("profile_management/", views.profile_management , name = "profile_management"),
    path("edit_profile/", views.edit_profile , name = "edit_profile"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)