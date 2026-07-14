from django.contrib import admin
from django.urls import path
from reports import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Start Page
    path('', views.start_page, name='start_page'),

    # User Authentication
    path('signup/', views.signup_view, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='reports/login.html'
        ),
        name='login'
    ),
    path('logout/', views.logout_view, name='logout'),

    # Admin Login
    path('admin-login/', views.admin_login, name='admin_login'),

    # Home Page
    path('home/', views.category_list, name='category_list'),

    # Category Page
    path(
        'categories/<str:category>/',
        views.issues_by_category,
        name='issues_by_category'
    ),

    # Issue Detail
    path(
        'issue/<int:issue_id>/',
        views.issue_detail,
        name='issue_detail'
    ),

    # Optional Django Admin
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
