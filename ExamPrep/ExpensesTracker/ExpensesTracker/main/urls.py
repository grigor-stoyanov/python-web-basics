from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ExpensesTracker.main.views import home_view, create_expense_view, edit_expense_view, \
    delete_expense_view, profile_view, edit_profile_view, delete_profile_view
app_name='main'
urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_expense_view, name='create expense'),
    path('edit/<int:pk>/', edit_expense_view, name='edit expense'),
    path('delete/<int:pk>/', delete_expense_view, name='delete expense'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit profile'),
    path('profile/delete/', delete_profile_view, name='delete profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)