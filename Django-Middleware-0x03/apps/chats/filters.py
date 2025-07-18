import django_filters
from .models import Message


class MessageFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    end_state = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')
    sender = django_filters.CharFilter(field_name='sender__username', lookup_expr='iexact')
    conversation_id = django_filters.NumberFilter(field_name='conversation__conversation.id')

    class Meta:
        Model = Message
        fields = ('sender, conversation_id, start_date, end_date')
