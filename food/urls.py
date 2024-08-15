from django.urls import path

from . import views


app_name = 'food'
urlpatterns = [

                   # /food/
    #path('', views.index, name="index"),

    #🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩 # CLASS BASE URLS # -> for index
    path('', views.IndexClassView.as_view(), name="index"),



    # /food/item
    path('item/', views.item, name='item'),

                    # /food/item/1

    # # 🚩🚩🚩🚩🚩VIDEO 58🚩🚩🚩🚩🚩 # CLASS BASE URLS # -> for detail
    path('<int:pk>/', views.DetailClassView.as_view(), name="detail"),

      # path('<int:item_id>/',views.detail, name='detail'),

    # add Item
    path('add/', views.create_Item_View.as_view(),name='create_Item'),
    # edit Item

    path('update/<int:id>', views.update_item,name='update_item'),

    # delite item

    path('delete/<int:pk>',views.delete_item,name='delete_item'),



    # # CLASS BASE URLS

    # -> for index














    path('ordinateur/', views.ordinateur, name='ordinateur'),
    path('periferiques/', views.periferiques, name='periferiques'),
    path('uc/', views.uc, name="uc"),
    path('soureis/', views.soureis, name='soureis'),
    path('titre1/', views.titre1, name='titre1'),
    path('titre2/', views.titre2, name='titre2'),
    path('titre3/', views.titre3, name='titr3'),
    path('titre4/', views.titre4, name='titr4'),
    path('titre5/', views.titre5, name='titre5'),
    path('titre6/', views.titre6, name='titre6'),

]
