"""Kalakendra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('',views.main_index),
    path('log',views.log),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('user_home',views.user_home),
    path('logout',views.logout),

# ---------
    path('admin_add_category',views.admin_add_category),
    path('admin_add_category_post',views.admin_add_category_post),
    path('admin_view_category',views.admin_view_category),
    path('admin_delete_category/<id>',views.admin_delete_category),
    path('admin_add_tutor',views.admin_add_tutor),
    path('admin_add_tutor_post',views.admin_add_tutor_post),
    path('admin_view_tutors',views.admin_view_tutors),
    path('admin_edit_tutor/<id>',views.admin_edit_tutor),
    path('admin_edit_tutor_post/<id>',views.admin_edit_tutor_post),
    path('admin_remove_tutor/<id>',views.admin_remove_tutor),
    path('admin_view_user',views.admin_view_user),
    path('admin_view_tutor_request/<id>',views.admin_view_tutor_request),
    path('accept_request/<id>',views.accept_request),
    path('reject_request/<id>',views.reject_request),
    path('admin_add_batch',views.admin_add_batch),
    path('admin_add_batch_post',views.admin_add_batch_post),
    path('admin_view_batch',views.admin_view_batch),
    path('admin_edit_batch/<id>',views.admin_edit_batch),
    path('admin_edit_batch_post/<id>',views.admin_edit_batch_post),
    path('admin_remove_batch/<id>',views.admin_remove_batch),
    path('admin_add_ornament_costume/<id>',views.admin_add_ornament_costume),
    path('admin_add_ornament_costume_post/<id>',views.admin_add_ornament_costume_post),
    path('admin_view_ornaments_and_costume/<id>',views.admin_view_ornaments_and_costume),
    path('admin_edit_ornaments_and_costume/<id>',views.admin_edit_ornaments_and_costume),
    path('admin_edit_ornaments_and_costume_post/<id>',views.admin_edit_ornaments_and_costume_post),
    path('admin_remove_ornaments_and_costume/<id>',views.admin_remove_ornaments_and_costume),
    path('admin_view_booking',views.admin_view_booking),
    path('update_return_status/<id>',views.update_return_status),
    path('update_return_status_post/<id>',views.update_return_status_post),
    path('admin_allocate_tutor/<id>',views.admin_allocate_tutor),
    path('admin_allocate_tutor_post/<id>',views.admin_allocate_tutor_post),
    path('admin_view_feedback',views.admin_view_feedback),
    path('update_return_status/<id>',views.update_return_status),
    path('update_return_status_post/<id>',views.update_return_status_post),


# ---------------------------- USER ------------------------------
    path('user_register',views.user_register),
    path('user_register_post',views.user_register_post),
    path('manage_profile',views.manage_profile),
    path('manage_profile_post',views.manage_profile_post),
    path('user_view_allocated_tutor',views.user_view_allocated_tutor),
    path('user_send_request/<id>',views.user_send_request),
    path('user_view_verified_request',views.user_view_verified_request),
    path('user_make_tutor_payment/<id>',views.user_make_tutor_payment),
    path('on_payment_success/<id>',views.on_payment_success),
    path('get_ornaments_by_category/<cat_id>/',views.get_ornaments_by_category),
    path('user_book_ornament_and_costume',views.user_book_ornament_and_costume),
    path('user_book_ornament_and_costume_post',views.user_book_ornament_and_costume_post),
    path('user_view_cart',views.user_view_cart),
    path('user_place_order',views.user_place_order),
    path('user_payment_mode/<order_id>',views.user_payment_mode),
    path('user_costume_and_ornament_pay/<rid>',views.user_costume_and_ornament_pay),
    path('costume_and_ornament_pay/<id>',views.costume_and_ornament_pay),
    path('cancel_cart/<id>',views.cancel_cart),
    path('user_send_feedback',views.user_send_feedback),
    path('user_send_feedback_post',views.user_send_feedback_post),
]
