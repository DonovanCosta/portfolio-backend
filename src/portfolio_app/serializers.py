from rest_framework import serializers
from . import models

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ProjectsSerializer(DynamicFieldsModelSerializer):
    technologies = serializers.StringRelatedField(many=True)
    #image = serializers.SerializerMethodField('get_photo')
    class Meta:
        model = models.Projects
        fields = ['id', 'project_name', 'github_link', 'content', 'preview_link', 'image', 'video', 'technologies','short_description']

    def get_photo(self, obj):
        
        request = self.context.get('request')
        photo = models.Projects.image.url
        print(request)
        return request.build_absolute_uri(photo)

class BiographySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Biography
        fields = ['about_me', 'experience']

class ContactMeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model= models.ContactMe
        fields = ['name', 'email', 'message']