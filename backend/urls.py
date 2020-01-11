from django.conf.urls import url
from django.contrib import admin
from django.urls import path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework_jwt.views import obtain_jwt_token

# from yamod.views import FileUploadView
from rest_framework_jwt.views import obtain_jwt_token

from .yamod import views

# schema_view = get_schema_view(
#   openapi.Info(
#        title='API',
#       default_version='v1'
#   ),
# )

urlpatterns = [
    path('', admin.site.urls),
    path('label/options', views.labels_option_list),
    path('artist/options', views.artist_option_list),
    path('song/list', views.song_list),
    # song CRUD #
    path('song/create', views.song_form_create),
    path('song/<int:pk>/get', views.song_form_get),
    path('song/<int:pk>/update', views.song_form_update),
    path('song/<int:pk>/delete', views.song_delete),
    # song CRUD end #
    # artist CRUD #
    path('artist/create', views.artist_form_create),
    path('artist/<int:pk>/get', views.artist_form_get),
    path('artist/<int:pk>/update', views.artist_form_update),
    path('artist/<int:pk>/delete', views.artist_delete),
    # artist CRUD end #
    url(r'^api-token-auth/', obtain_jwt_token),
    # test end #

    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^media$', FileUploadView.as_view()),
    # path('media/<int:pk>', views.media_download),
    # path('media/<int:pk>/get', views.media_get),

    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
