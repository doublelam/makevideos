"""huangsite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import view
from . import temp
from . import getpost
from .common import handle_request as hr
from .operate_database.op_base import list_bases
from .apis.apis_urls import URLPATTERNS
from .apis.common_apis import URLPATTERNS as COMMON_URLPATTERNS

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', view.hello),
    url(r'^tem/', temp.temp),
    url(r'^textSend', hr.handle_request('post', getpost.get_post)),
    url(r'^post/list_bases', hr.handle_request('post', list_bases)),
    url(r'^make_video_post/', include(URLPATTERNS)),
    url(r'^common_apis/', include(COMMON_URLPATTERNS)),
    url(r'^', view.default),
]
