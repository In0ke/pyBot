#
#
#
# bot = telebot.TeleBot('1691294316:AAECFy049o8-er9Kytficy-J4MKhZnzP3yo')
# reglet_id = ''
#
#
# tarif = ['Start-0, disk: 5, memory: 512, CPU: 1, price month: 215',
#          'Start-1, disk: 10, memory: 1024, CPU: 1, price month: 248',
#          'Start-2, disk: 15, memory: 2048, CPU: 2, price month: 590',
#          'Start-3, disk: 25, memory: 4096, CPU: 2, price month: 990',
#          'Cloud-1, disk: 25, memory: 1024, CPU: 1, price month: 298',
#          'Cloud-2a, disk: 50, memory: 1024, CPU: 2, price month: 480',
#          'Cloud-2b, disk: 50, memory: 2048, CPU: 1, price month: 660',
#          'Cloud-3a, disk: 60, memory: 1024, CPU: 3, price month: 880',
#          'Cloud-3b, disk: 60, memory: 2048, CPU: 2, price month: 880',
#          'Cloud-3c, disk: 60, memory: 3072, CPU: 1, price month: 880',
#          'Cloud-4, disk: 80, memory: 4096, CPU: 2, price month: 1590',
#          'Cloud-5, disk: 100, memory: 6144, CPU: 4, price month: 2290',
#          'Cloud-6, disk: 120, memory: 8192, CPU: 4, price month: 2890',
#          'Cloud-7, disk: 160, memory: 10240, CPU: 6, price month: 3590',
#          'Cloud-8, disk: 240, memory: 16384, CPU: 8, price month: 5830',
#          'Cloud-9, disk: 320, memory: 24576, CPU: 12, price month: 9940',
#          'Turbo-1, disk: 60, memory: 2048, CPU: 1, price month: 990',
#          'Turbo-2, disk: 80, memory: 4096, CPU: 2, price month: 1870',
#          'Turbo-3, disk: 80, memory: 6144, CPU: 3, price month: 2490',
#          'Turbo-4, disk: 120, memory: 8192, CPU: 4, price month: 3340',
#          'Turbo-5, disk: 120, memory: 10240, CPU: 5, price month: 4140',
#          'Turbo-6, disk: 160, memory: 12228, CPU: 6, price month: 4990',
#          'Turbo-7, disk: 160, memory: 14336, CPU: 7, price month: 5780',
#          'Turbo-8, disk: 200, memory: 16384, CPU: 8, price month: 6650',
#          'Dedicated-1, disk: 120, memory: 8192, CPU: 2, price month: 3380',
#          'Dedicated-2, disk: 160, memory: 16384, CPU: 4, price month: 6680',
#          'Dedicated-3, disk: 240, memory: 24576, CPU: 6, price month: 9990',
#          'Dedicated-4, disk: 320, memory: 32768, CPU: 8, price month: 13340',
#          'Dedicated-5, disk: 500, memory: 49152, CPU: 12, price month: 19980']
# reglet_list = request_collections.get_reglet_list()
#
# keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard.row('/get_plans', '/get_apps_list', '/get_os_list', '/get_server_list', '/create_a_server')
#
# @bot.message_handler(commands=['get_plans'])
# def get_plans(message):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     start_0 = types.InlineKeyboardButton(tarif[0], callback_data='start_0')
#     start_1 = types.InlineKeyboardButton(tarif[1], callback_data='start_1')
#     start_2 = types.InlineKeyboardButton(tarif[2], callback_data='start_2')
#     start_3 = types.InlineKeyboardButton(tarif[3], callback_data='start_3')
#     cloud_1 = types.InlineKeyboardButton(tarif[4], callback_data='cloud_1')
#     cloud_2a = types.InlineKeyboardButton(tarif[5], callback_data='cloud_2a')
#     cloud_2b = types.InlineKeyboardButton(tarif[6], callback_data='cloud_2b')
#     cloud_3a = types.InlineKeyboardButton(tarif[7], callback_data='cloud_3a')
#     cloud_3b = types.InlineKeyboardButton(tarif[8], callback_data='cloud_3b')
#     cloud_3c = types.InlineKeyboardButton(tarif[9], callback_data='cloud_3c')
#     cloud_4 = types.InlineKeyboardButton(tarif[10], callback_data='cloud_4')
#     cloud_5 = types.InlineKeyboardButton(tarif[11], callback_data='cloud_5')
#     cloud_6 = types.InlineKeyboardButton(tarif[12], callback_data='cloud_6')
#     cloud_7 = types.InlineKeyboardButton(tarif[13], callback_data='cloud_7')
#     cloud_8 = types.InlineKeyboardButton(tarif[14], callback_data='cloud_8')
#     cloud_9 = types.InlineKeyboardButton(tarif[15], callback_data='cloud_9')
#     turbo_1 = types.InlineKeyboardButton(tarif[16], callback_data='turbo_1')
#     turbo_2 = types.InlineKeyboardButton(tarif[17], callback_data='turbo_2')
#     turbo_3 = types.InlineKeyboardButton(tarif[18], callback_data='turbo_3')
#     turbo_4 = types.InlineKeyboardButton(tarif[19], callback_data='turbo_4')
#     turbo_5 = types.InlineKeyboardButton(tarif[20], callback_data='turbo_5')
#     turbo_6 = types.InlineKeyboardButton(tarif[21], callback_data='turbo_6')
#     turbo_7 = types.InlineKeyboardButton(tarif[22], callback_data='turbo_7')
#     turbo_8 = types.InlineKeyboardButton(tarif[23], callback_data='turbo_8')
#     dedicated_1 = types.InlineKeyboardButton(tarif[24], callback_data='dedicated_1')
#     dedicated_2 = types.InlineKeyboardButton(tarif[25], callback_data='dedicated_2')
#     dedicated_3 = types.InlineKeyboardButton(tarif[26], callback_data='dedicated_3')
#     dedicated_4 = types.InlineKeyboardButton(tarif[27], callback_data='dedicated_4')
#     dedicated_5 = types.InlineKeyboardButton(tarif[28], callback_data='dedicated_5')
#
#     markup.add(start_0, start_1, start_2, start_3,
#                cloud_1, cloud_2a, cloud_2b, cloud_3a,
#                cloud_3b, cloud_3c, cloud_4, cloud_5,
#                cloud_6, cloud_7, cloud_8, cloud_9,
#                turbo_1, turbo_2, turbo_3, turbo_4,
#                turbo_5, turbo_6, turbo_7, turbo_8,
#                dedicated_1, dedicated_2, dedicated_3, dedicated_4, dedicated_5)
#     bot.send_message(message.chat.id, 'Доступные ОС: ', reply_markup=markup)
#
#
# @bot.message_handler(commands=['get_apps_list'])
# def get_apps(message):
#     markup = types.InlineKeyboardMarkup(row_width=4)
#     bitrix_1c = types.InlineKeyboardButton('1С-Битрикс с ISPmanager', callback_data='bitrix_1c')
#     bitrix_vm = types.InlineKeyboardButton('BitrixVM', callback_data='bitrix_vm')
#     django = types.InlineKeyboardButton('Django', callback_data='django')
#     docker = types.InlineKeyboardButton('Docker', callback_data='docker')
#     isp_manager = types.InlineKeyboardButton('ISPManager 5 Lite', callback_data='isp_manager')
#     jitsi_meet = types.InlineKeyboardButton('Jitsi Meet', callback_data='jitsi_meet')
#     lamp = types.InlineKeyboardButton('LAMP', callback_data='lamp')
#     lemp = types.InlineKeyboardButton('LEMP', callback_data='lemp')
#     node_js = types.InlineKeyboardButton('Node.js', callback_data='node_js')
#     vesta = types.InlineKeyboardButton('Vesta', callback_data='vesta')
#
#     markup.add(vesta, bitrix_vm, django, docker, isp_manager, jitsi_meet, lamp, lemp, node_js, bitrix_1c)
#     bot.send_message(message.chat.id, 'Доступные Приложения: ', reply_markup=markup)
#
#
# @bot.message_handler(commands=['get_os_list'])
# def get_os_list(message):
#     markup = types.InlineKeyboardMarkup(row_width=3)
#     ubuntu_16_04 = types.InlineKeyboardButton('ubuntu 16.04', callback_data='ubuntu-16-04-amd64')
#     ubuntu_18_04 = types.InlineKeyboardButton('ubuntu 18.04', callback_data='ubuntu-18-04-amd64')
#     ubuntu_20_04 = types.InlineKeyboardButton('ubuntu 20.04', callback_data='ubuntu-20-04-amd64')
#     centos_7 = types.InlineKeyboardButton('centos 7', callback_data='centos-7-amd64')
#     centos_8 = types.InlineKeyboardButton('centos 8', callback_data='centos-8-amd64')
#     debian_9 = types.InlineKeyboardButton('debian 9', callback_data='debian-9-amd64')
#     debian_10 = types.InlineKeyboardButton('debian 10', callback_data='debian-10-amd64')
#
#     markup.add(ubuntu_16_04, ubuntu_18_04, ubuntu_20_04, centos_7, centos_8, debian_9, debian_10)
#     bot.send_message(message.chat.id, 'Доступные ОС: ', reply_markup=markup)
#
#
# @bot.message_handler(commands=['get_operation_list'])
# def get_operation_list(message):
#     global reglet_id
#     markup = types.InlineKeyboardMarkup(row_width=3)
#     start = types.InlineKeyboardButton('Запустить сервер', callback_data='start')
#     stop = types.InlineKeyboardButton('Остановить сервер', callback_data='stop')
#     change_plan = types.InlineKeyboardButton('Изменить тариф', callback_data='change_plan')
#     reboot = types.InlineKeyboardButton('Перезагрузить сервер', callback_data='reboot')
#     delete = types.InlineKeyboardButton('Удалить сервер', callback_data='delete')
#     markup.add(stop, start, change_plan, reboot, delete)
#     bot.send_message(message.chat.id, f'Операции над сервером {reglet_id}:', reply_markup=markup)
#
#
#
# @bot.message_handler(commands=['get_server_list'])
# def button(message):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     response = request_collections.get_reglet_list()
#     servers = {}
#     for i in range(len(response)):
#         servers[i] = types.InlineKeyboardButton(f'{str(response[i][0])}' + ' ' +
#                                                 f'{str(response[i][1])}' + ' ' +
#                                                 f'{str(response[i][2])}' + ' ' +
#                                                 f'{str(response[i][3])}',
#                                                 callback_data=str(response[i][1]))
#     for i in servers:
#         markup.add(servers[i])
#
#     bot.send_message(message.chat.id, 'Твой сервер:', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     global reglet_id
#     if call.data == str(reglet_list[0][1]):
#         bot.send_message(call.message.chat.id, f'Ты выбрал сервер c id {reglet_list[0][1]}, че тебе надо?')
#         reglet_id = reglet_list[0][1]
#         #get_operation_list()
#     elif call.data == str(reglet_list[1][1]):
#         bot.send_message(call.message.chat.id, f'Ты выбрал сервер c id {reglet_list[1][1]}, че тебе надо?')
#         reglet_id = reglet_list[1][1]
#         #get_operation_list()
#
#
# @bot.message_handler(commands=['create_a_server'])
# def create_a_server(message):
#         bot.send_message(message.chat.id, 'Пожалуйста, выберите операционную систему:')
#         get_os_list(message)
#         bot.register_next_step_handler(message, get_plans)
#         bot.send_message(message.chat.id, 'Теперь выбери тарифный план:')
#         get_os_list(message)
#         bot.register_next_step_handler(message, get_plans)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.message:
#         if call.data == 'ubuntu-16-04-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал ubuntu-16')
#         elif call.data == 'ubuntu-18-04-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал ubuntu-18')
#         elif call.data == 'ubuntu-20-04-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал ubuntu-20')
#         elif call.data == 'centos-7-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал centos-7')
#         elif call.data == 'centos-8-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал centos-8')
#         elif call.data == 'debian-9-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал debian-9')
#         elif call.data == 'debian-10-amd64':
#             bot.send_message(call.message.chat.id, 'Ты выбрал debian-10')
#
#
#
#
#
#
#
# bot.polling()
