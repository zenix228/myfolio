from rest_framework.serializers import *
from apps.about.models import About
from apps.about.models import Post
#from apps.user.models import 

class AboutSerializer():
    class Meta:

        model = About
        fields = '__all__'

class PostSerializer():
    class Meta:

        model = Post
        fields = '__all__'

class AboutSerializer():
    class Meta:

        model = About
        fields = '__all__'