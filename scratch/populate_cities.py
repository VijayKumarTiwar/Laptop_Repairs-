from core.models import City

state_map = {
    'Agra': 'Uttar Pradesh', 'Ahmedabad': 'Gujarat', 'Aligarh': 'Uttar Pradesh', 
    'Amritsar': 'Punjab', 'Bareilly': 'Uttar Pradesh', 'Bengaluru': 'Karnataka', 
    'Bhagalpur': 'Bihar', 'Bhopal': 'Madhya Pradesh', 'Bhubaneswar': 'Odisha', 
    'Chandigarh': 'Chandigarh', 'Cuttack': 'Odisha', 'Dehradun': 'Uttarakhand', 
    'Delhi': 'Delhi', 'Faridabad': 'Haryana', 'Gandhi Nagar': 'Gujarat', 
    'Ghaziabad': 'Uttar Pradesh', 'Gorakhpur': 'Uttar Pradesh', 'Greater Noida': 'Uttar Pradesh', 
    'Gurugram': 'Haryana', 'Gwalior': 'Madhya Pradesh', 'Haridwar': 'Uttarakhand', 
    'Haldwani': 'Uttarakhand', 'Hyderabad': 'Telangana', 'Indore': 'Madhya Pradesh', 
    'Jabalpur': 'Madhya Pradesh', 'Jaipur': 'Rajasthan', 'Jhansi': 'Uttar Pradesh', 
    'Kanpur': 'Uttar Pradesh', 'Lucknow': 'Uttar Pradesh', 'Ludhiana': 'Punjab', 
    'Meerut': 'Uttar Pradesh', 'Mohali': 'Punjab', 'Moradabad': 'Uttar Pradesh', 
    'Mumbai': 'Maharashtra', 'Mysuru': 'Karnataka', 'Nagpur': 'Maharashtra', 
    'Noida': 'Uttar Pradesh', 'Patna': 'Bihar', 'Panchkula': 'Haryana', 
    'Prayagraj': 'Uttar Pradesh', 'Pune': 'Maharashtra', 'Raipur': 'Chhattisgarh', 
    'Roorkee': 'Uttarakhand', 'Rudrapur': 'Uttarakhand', 'Tirupati': 'Andhra Pradesh', 
    'Ujjain': 'Madhya Pradesh', 'Varanasi': 'Uttar Pradesh', 'Tiwariawada': 'Andhra Pradesh', 
    'Zirakpur': 'Punjab', 'New Delhi': 'Delhi'
}

for city_name, state in state_map.items():
    City.objects.filter(name=city_name).update(state=state)

print('Cities updated with states successfully.')
