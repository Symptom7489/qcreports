from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reports-home'),
    path('add_project/', views.add_project, name='add-project'),
    path('add_jmf/', views.add_jmf, name='add-jmf'),
    path('add_readings/', views.add_readings, name='add-readings'),
    path('qc_report/', views.add_qcreport, name='qc_report'),
    path('show_projects/<project_id>',views.show_projects, name='show-projects'),
    path('show_jmfs/<jmf_id>',views.show_jmfs, name='show-jmfs'),
    path('test_data/',views.test_data, name='test-data'),
    path('update_project/<project_id>', views.update_project, name='update-projects'),
    path('nightly_form/', views.nightly_form, name='nightly-form'),
    #path('nightly_form_setup/', views.nightly_form_setup, name= 'nightly-form-setup')
]
