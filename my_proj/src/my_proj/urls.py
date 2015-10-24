from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^services/$', views.ServicesPage.as_view(), name='services'),
    url(r'^projects/$', views.ProjectsPage.as_view(), name='projects'),
    url(r'^clients/$', views.ClientsPage.as_view(), name='clients'),
    url(r'^contacts/$', views.ContactsPage.as_view(), name='contacts'),
    url(r'^python/$', views.PythonPage.as_view(), name='python'),
    url(r'^latex/$', views.LatexPage.as_view(), name='latex'),
    url(r'^php/$', views.PhpPage.as_view(), name='php'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
