from fastapi import HTTPException, status
import phonenumbers
import pycountry
from phonenumbers import geocoder



def get_country_details(phone):
  try:
    ph = remove_zero(phone)
    if is_valid_number(ph):
      phone_number = phonenumbers.parse(ph)
      country_name = geocoder.country_name_for_number(phone_number, "en")
      country_code = get_country_code(country_name)
      return {'phone': ph, 'country': country_code}
    else:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid phone number")
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid phone number")

def is_valid_number(phone):
  try:
    phone_number = phonenumbers.parse(phone, None)
    return phonenumbers.is_valid_number(phone_number)
  except:
    return False


def get_country_code(name):
  countries = {}
  for country in pycountry.countries:
    countries[country.name] = country.alpha_2
  return countries.get(name, 'Unknown')

def remove_zero(phone):
  if phone.startswith('0'):
    return remove_zero(phone[1:])
  elif phone.startswith('+'):
    return phone
  else:
    return '+' + phone