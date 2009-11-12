from django.conf.urls.defaults import patterns, url
from django.views.generic.create_update import create_object, update_object
from schools.companies.models import Company
from schools.search.views import object_list

urlpatterns = patterns('schools.companies.views',
    url(r'company/create/$', create_object, {'model':Company}, name='companies_company_create'),
    url(r'company/(?P<object_id>\d+)/$', 'company_update', {'model':Company}, name='companies_company_update'),
    url(r'company/$', object_list, {'queryset':Company.objects.all(), 'search_fields':['name__contains']}, name='companies_company_list'),
)