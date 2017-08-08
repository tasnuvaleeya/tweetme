from rest_framework import generics
from .serializers import TweetModelSerializer
from django.db.models import Q

from tweets.models import Tweet


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query= self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                        Q(content__icontains=query)|
                        Q(user__username__icontains=query)
                        )
        return qs