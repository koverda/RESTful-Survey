from rest_framework import serializers
from surveys.models import Survey
from django.contrib.auth.models import User


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Survey
        fields = ('url', 'owner', 'recommend_company', 'what_changes', 'was_researched', 'feedback')

'''
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')
'''                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    surveys = serializers.HyperlinkedRelatedField(queryset=Survey.objects.all(), view_name='survey-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'surveys')
