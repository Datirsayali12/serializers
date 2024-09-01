from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        error_messages={
            'required': 'Please provide the item name.',
            'max_length': 'Name cannot be longer than 100 characters.'
        }
    )
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'required': 'Please provide the price.',
            'invalid': 'Enter a valid price.',
            'max_digits': 'The price cannot exceed 10 digits in total.',
        }
    )
    quantity = serializers.IntegerField(
        min_value=1,
        error_messages={
            'required': 'Please provide the quantity.',
            'min_value': 'Quantity cannot be less than 1.',
            'invalid': 'Enter a valid integer for quantity.'
        }
    )

    # Custom field-level validation
    def validate_name(self, value):
        if 'invalid' in value.lower():
            raise serializers.ValidationError("The name cannot contain the word 'invalid'.")
        return value

    # Custom object-level validation
    def validate(self, data):
        price = data.get('price')
        quantity = data.get('quantity')

        if price and price > 1000 and quantity < 10:
            raise serializers.ValidationError("For items priced above 1000, quantity must be at least 10.")

        return data
