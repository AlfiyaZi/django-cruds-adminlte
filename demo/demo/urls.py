"""demo URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from cruds_adminlte.urls import crud_for_app
from testapp.forms import CustomerForm, InvoiceForm, LineForm, AddressesForm
from testapp.views import AutorCRUD, InvoiceCRUD, IndexView
from django.contrib.auth import views as auth_views


authorcrud = AutorCRUD()
invoicecrud = InvoiceCRUD()

ns = crud_for_app('testapp', check_perms=True, namespace="ns")

urlpatterns = [
    url(r'^$', IndexView.as_view()),

    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^select2/', include('django_select2.urls')),
    url('^namespace/', include(ns, namespace='ns')),
    url(r'', include(authorcrud.get_urls())),
    url(r'', include(invoicecrud.get_urls()))
]


custom_forms = {
    'add_customer': CustomerForm,
    'update_customer': CustomerForm,
    'add_invoice': InvoiceForm,
    'update_invoice': InvoiceForm,
    'add_line': LineForm,
    'update_line': LineForm,
    'add_addresses': AddressesForm,
    'update_addresses': AddressesForm,
}

urlpatterns += crud_for_app('testapp', login_required=True,
                            check_perms=True, modelforms=custom_forms)
urlpatterns += crud_for_app('auth')

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
