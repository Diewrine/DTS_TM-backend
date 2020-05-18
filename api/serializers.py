from rest_framework import serializers, fields
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ("id",'firstname', 'lastname', 'address', 'phone', 'updated_at') 
			

"""
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
"""