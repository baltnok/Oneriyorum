from django.conf.urls import url
from oneri.views import ProductDetailView, AnasayfaView, SssView, ProductCreate

urlpatterns=[
    url(r"^$", AnasayfaView.as_view(), name="Anasayfa"),
    url(r"^product/(?P<pk>\d+)$", ProductDetailView.as_view(), name="product"),
    url(r"sss$", SssView.as_view()),
    url(r'product/add/$', ProductCreate.as_view(), name='product-add'),
]