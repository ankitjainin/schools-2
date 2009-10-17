from django.conf.urls.defaults import patterns, url
from django.views.generic.create_update import create_object, update_object
from schools.buildings.models import Building, Classroom, BuildingMonthExpense
from django.views.generic.list_detail import object_list

urlpatterns = patterns('schools.buildings.views',
   url(r'building/create/$', create_object, {'model':Building, 'template_name':'buildings/building_create.html'}, name='buildings_building_create'),
   
   url(r'building/(?P<object_id>\d+)/$', 'building_update', name='buildings_building_update'),
   
   url(r'building/$', object_list, {'queryset':Building.objects.all()}, name='buildings_building_list'),
)