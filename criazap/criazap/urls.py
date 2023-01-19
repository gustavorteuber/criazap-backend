from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from simple_chatbot.views import SimpleChatbot
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from core.views import (
    StatusViewSet,
    ChatsViewSet,
    MyTokenObtainPairView,
    UsuarioViewSet,
    botViewSet,
)
from uploader.router import router as uploader_router



router = DefaultRouter()
router.register(r'chats', ChatsViewSet)
router.register(r'status', StatusViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'bot', botViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("media/", include(uploader_router.urls)),
    path("simple_chatbot/", SimpleChatbot.as_view())
    
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)