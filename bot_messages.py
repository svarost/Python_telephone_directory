from bot_utils import TestStates


help_message = '/input_contact - добавить контакт\n' \
               '/view_contacts - вывести список контактов\n' \
               '/search - поиск контактов\n' \
               '/delete - удалить контакт\n' \
               '/export_csv - экспорт телефонной книги в CSV\n' \

start_message = 'Привет! Это бот телефонного справочника.\n' + help_message
invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
state_change_success_message = 'Текущее состояние успешно изменено'
state_reset_message = 'Состояние успешно сброшено'
current_state_message = 'Текущее состояние - "{current_state}", что удовлетворяет условию "один из {states}"'

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'enter_name': invalid_key_message,
    'state_change': state_change_success_message,
    'state_reset': state_reset_message,
    'current_state': current_state_message,
}