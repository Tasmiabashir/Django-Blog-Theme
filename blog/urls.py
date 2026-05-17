from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:slug>/', views.category, name="category"),

    # ✅ Post Detail URL
   path('post/<slug:slug>/', views.post_detail, name="post_detail"),
    path('contact/', views.contact, name="contact"),
    path('write-for-us/', views.write_for_us, name="write_for_us"),
    path("category/<slug:slug>/", views.category, name="category")

]
