import phonenumbers

from phonenumbers import geocoder
phone_number = phonenumbers.parse('+18033360564')


print(geocoder.description_for_number(phone_number, 'en'))
