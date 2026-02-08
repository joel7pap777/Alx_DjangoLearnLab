from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes created by the router
    path('', include(router.urls)),
]
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # <-- important
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token endpoint
]
