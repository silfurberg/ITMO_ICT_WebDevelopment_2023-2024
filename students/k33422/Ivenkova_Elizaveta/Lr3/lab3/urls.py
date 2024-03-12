from django.urls import path
from lab3 import views

app_name = 'lab3'

urlpatterns = [
     # path('add_model_data/', views.InitDataView.as_view()),
    path('reader/books/<int:reader_pk>', views.ReaderBooksApiView.as_view(), name='reader_books'),
    path('reader/outdated', views.OutdatedReadersApiView.as_view(), name='reader_outdated'),
    path('reader/rare_books', views.ReaderRareBook.as_view(), name='reader_rare_books'),
    path('reader/book_month_ago', views.ReaderBookMonthAgoApi.as_view(), name='reader_book_month_age'),
    path('reader/list', views.ReaderListApiView.as_view()),
    path('reader/create', views.ReaderCreateApiView.as_view(), name='reader_new'),
    path('reader/add_book', views.ReaderBookHistoryCreateView.as_view(), name='book_history/create'),
    path('statistics/education', views.StatisticsEducationApiView.as_view(), name='statistics_education'),
    path('statistics/age', views.StatisticsAgeApiView.as_view(), name='statistice_age'),
    path('statistics/room/<int:pk>', views.StatisticsRoomApiView.as_view(), name='statistics_room'),
    path('statistics/room/list', views.StatisticsRoomListApiView.as_view(), name='statistics_room_list'),
    path('statistics/library', views.StatisticsLibraryApiView.as_view(), name='statistics_library'),
    path('book_instance/list', views.BookInstanceListApi.as_view(), name='book_instance_list'),
    path('book_instance/<int:pk>', views.BookInstanceRetrieveDestroyApiView.as_view(), name='book_instance_retrieve'),
    path('book_instance/remove/<int:pk>', views.BookInstanceRetrieveDestroyApiView.as_view(), name='book_instance_remove'),
    path('book_instance/update/<int:pk>', views.BookInstanceUpdateApiView.as_view()),
    path('book_instance/create', views.BookInstanceCreateView.as_view(), name='book_instance_create'),
    path('book/create', views.BookCreateView.as_view(), name='book_create')
]
