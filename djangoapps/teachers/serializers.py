from rest_framework import serializers
from teachers.models import Teacher, Language, Experience, Education, Certificate, Immersion
from locations.models import Location, Position
from locations.serializers import LocationSerializer


class ImmersionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Immersion model """

    class Meta:
        model = Immersion
        fields = ('id',
                  'active',
                  'category',
                  'user_type',)
        read_only_fields = ('id',)


class CertificateSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Certificate model """

    class Meta:
        model = Certificate
        fields = ('id',
                  'name',
                  'institution',
                  'date_received',
                  'description',)

        read_only_fields = ('id',)


class EducationSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Education model """

    class Meta:
        model = Education
        fields = ('id',
                  'school',
                  'degree',
                  'field_study',
                  'date_start',
                  'date_finish',
                  'description',)

        read_only_fields = ('id',)


class ExperienceSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Experience model """

    class Meta:
        model = Experience
        fields = ('id',
                  'position',
                  'company',
                  'city',
                  'country',
                  'date_start',
                  'date_finish',
                  'description',)

        read_only_fields = ('id',)


class LanguageSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Language model """

    class Meta:
        model = Language
        field = ('id',
                 'native',
                 'teach',
                 'learn',)

        read_only_fields = ('id',)


class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """
    location = LocationSerializer()
    languages = LanguageSerializer()
    experiences = ExperienceSerializer(many=True, read_only=True, source='experience_set')
    educations = EducationSerializer(many=True, read_only=True, source='education_set')
    certificates = CertificateSerializer(many=True, read_only=True, source='certificate_set')
    immersion = ImmersionSerializer()

    class Meta:
        model = Teacher
        fields = ('id',
                  'location',
                  'email',
                  'phone_number',
                  'first_name',
                  'last_name',
                  'sex',
                  'birth_date',
                  'born',
                  'about',
                  'languages',
                  'type',
                  'teacher_since',
                  'methodology',
                  'experiences',
                  'educations',
                  'certificates',
                  'immersion',
                  'created_at',
                  'updated_at',)

    def create(self, validated_data):
        # Get location object in order to save on DB
        location_data = validated_data.pop('location', None)

        if location_data:
            # Get position object in order to save on DB
            position_data = location_data.pop('position', None)

            if position_data:
                position = Position.objects.get_or_create(**position_data)[0]
                # This part is important to avoid error (Cannot assign "": "" must be a instance)
                location_data['position'] = position
            location = Location.objects.get_or_create(**location_data)[0]
            # This part is important to avoid error (Cannot assign "": "" must be a instance)
            validated_data['location'] = location

        languages_data = validated_data.pop('languages', None)

        if languages_data:
            languages = Language.objects.get_or_create(**languages_data)[0]
            validated_data['languages'] = languages

        immersion_data = validated_data.pop('immersion', None)

        if immersion_data:
            immersion = Immersion.objects.get_or_create(**immersion_data)[0]
            validated_data['immersion'] = immersion

        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        position_data = location_data.pop('position')
        languages_data = validated_data.pop('languages')
        immersion_data = validated_data.pop('immersion')

        languages = instance.languages
        immersion = instance.immersion
        location = instance.location
        position = instance.location.position

        # Create teacher instance in order to save on DB
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.born = validated_data.get('born', instance.born)
        instance.about = validated_data.get('about', instance.about)
        instance.type = validated_data.get('type', instance.type)
        instance.teacher_since = validated_data.get('teacher_since', instance.teacher_since)
        instance.methodology = validated_data.get('methodology', instance.methodology)
        instance.save()

        if location_data:
            # Create location instance in order to save on DB
            location.country = location_data.get('country', location.country)
            location.address = location_data.get('address', location.address)
            location.city = location_data.get('city', location.city)
            location.state = location_data.get('state', location.state)
            location.zip_code = location_data.get('zip_code', location.zip_code)
            location.save()

        if position_data:
            # Create position instance in order to save on DB
            position.lng = position_data.get('lng', position.lng)
            position.lat = position_data.get('lat', position.lat)
            position.save()

        if languages_data:
            # Create languages instance in order to save on DB
            languages.native = languages_data.get('native', languages.native)
            languages.teach = languages_data.get('teach', languages.teach)
            languages.learn = languages_data.get('learn', languages.learn)
            languages.save()

        if immersion_data:
            # Create immersion instance in order to save on DB
            immersion.active = immersion_data.get('active', immersion.active)
            immersion.user_type = immersion_data.get('user_type', immersion.user_type)
            immersion.category = immersion_data.get('category', immersion.category)
            immersion.save()

        return instance
