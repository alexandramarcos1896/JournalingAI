from django.contrib import admin
from django.urls import path, include
from journal_app.views import RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('journal_app.urls')),  # ViewSets via routers
    path('api/register/', RegisterView.as_view(), name='register'),  # Registration
    path('api/profile/', UserProfileView.as_view(), name='profile'),  # Optional profile endpoint
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]