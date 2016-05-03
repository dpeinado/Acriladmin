from django.conf.urls import url
from inventories import views

urlpatterns = [
    url(r'^product/(?P<pk>\d+)/$', views.ProductInventoryView.as_view(), name='products_inventory'),
    url(r'^material/(?P<pk>\d+)/$', views.MaterialInventoryView.as_view(), name='materials_inventory'),
    url(r'^consumable/(?P<pk>\d+)/$', views.ConsumableInventoryView.as_view(), name='consumables_inventory'),
    url(r'^durable_good/(?P<pk>\d+)/$', views.DurableGoodInventoryView.as_view(), name='durable_goods_inventory'),
]