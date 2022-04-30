from requests import get, post




# print(post('http://localhost:5000/api/create_history_post',
#            json={'chat_id': 123,
#                  'request': 'Тек69798ости',
#                  'subject': 'sdfghjdfbdvcsftgeh'}).json())
#
# print(post(f'http://localhost:5000/api/add_bookmark/{123}',
#                       json={'request': 'content'}).json())


# print(post('http://localhost:5000/api/create_new_profile',
#            json={'chat_id': 123,
#                  'login': 'fsef',
#                  'password': 'sdfghjdfbdvcsftgeh'}).json())

print(get('http://localhost:5000/api/logins_for_registration').json())
print(get('http://localhost:5000/api/chat_id_for_registration').json())
print(get(f'http://localhost:5000/api/get_history/{122+1}').json())
print(get(f'http://localhost:5000/api/get_genres/{122+1}').json())
print(get(f'http://localhost:5000/api/get_last_film/{499106358}').json())
