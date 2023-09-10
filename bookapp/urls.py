from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('abou/',views.about),
    path('cont/',views.contact),
    path('serv/',views.service),
    path('reg/',views.registerr),
    path('log/',views.login),
    path('log_out/',views.logoutt),   


    
    path('admin_det/',views.admin_detail), 

    path('newregist/',views.new_reg),

    path('approve/',views.Approve),
    path('remove/',views.Remove),
    path('memb/',views.Members),

    path('addition/',views.add_book),

    path('update_page/',views.updatepage),
    path('remove_book/',views.remoove),
    path('up_date/',views.updatelink),

    path('new_form/',views.newform),

    path('img_link/',views.img),
    path('img_update/',views.image_update),

    path('detail/',views.details),



    path('user_det/',views.user_detail),

    path('boook/',views.bookss),
    path('bu_review/',views.bookrvw),
    path('req/',views.requ),

    path('back/',views.backpage),


    path('is/',views.issu),
    path('ap/',views.app),
    path('re/',views.ree),

    path('track/',views.trackk),
    path('tra_remo/',views.tremove),
  ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
