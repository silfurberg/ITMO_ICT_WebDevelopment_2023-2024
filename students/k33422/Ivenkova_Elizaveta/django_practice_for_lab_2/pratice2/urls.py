from django.urls import path
import pratice2.views

app_name = 'pratice2'
urlpatterns = [
    path('owner/<int:pk>', pratice2.views.OwnerView.as_view(), name='OwnerView'),
    path('owner_generic/<int:pk>', pratice2.views.OwnerViewGeneric.as_view(), name='OwnerViewGeneric'),
    path('time_fun/', pratice2.views.example_view_function, name="TimeFun"),
    path('time_template/', pratice2.views.example_view_template.as_view(), name="TimeTemp"),
    path('owner_list/', pratice2.views.OwnerViewList.as_view(), name="OwnerList"),
    path('owner_form/', pratice2.views.OwnerForm.as_view(), name="OwnerForm"),
    path('car_create_view/', pratice2.views.CarCreateView.as_view(), name="CarCreateView"),
    path('car_delete_view/<int:pk>', pratice2.views.CarDeleteView.as_view(), name="CarDeleteView"),
    path('car_update_view/<int:pk>', pratice2.views.CarUpdateView.as_view(), name="CarCreateView"),
    path('car/<int:pk>', pratice2.views.CarView.as_view(), name='CarView')
]