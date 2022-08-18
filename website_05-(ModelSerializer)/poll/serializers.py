from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	## 3. Validators
	def starts_with_r(value):
		if value[0].lower() != 'r':
			raise serializers.ValidationError('Name should start with R')

	name = serializers.CharField(validators=[starts_with_r])

	# name = serializers.CharField(read_only=True)
	class Meta:
		model = Student
		fields = '__all__'
		# read_only_fields = ['name', 'roll']
		extra_kwargs = {'name':{'read_only':True}}

	## 1. Field Level Validation
	def validate_roll(self, value):
		if value >= 200:
			raise serializers.ValidationError('Seat Full')
		return value

	## 2. Object Level Validation
	def validate(self, data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
			raise serializers.ValidationError('City Must be ranchi')
		return data