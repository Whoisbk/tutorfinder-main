import django_filters

from .models import *

class TutorFilter(django_filters.FilterSet):
 
    CHOICES=(
        ('newest','Newest'),
        ('oldest','Oldest')
    )
    
    ordering = django_filters.ChoiceFilter(label='Order by latest',choices=CHOICES,method='filter_by_order')
    sub = django_filters.CharFilter(field_name ='subject',lookup_expr='icontains' ,label='Subject')

    class Meta:
        model = Tutors
        fields = '__all__'
        exclude = ['user','subject','id_num','phone_num','img','date_created','types','fee_field','serv_desc','Experiance','qualification','facebook_link','linkedin_link','instagram_link','gender']
  
    def filter_by_order(self,queryset,name,value):
        expression = 'user' if value == 'oldest' else '-user'
        return queryset.order_by(expression)

    