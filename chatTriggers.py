from config import chat_report, creator
from localization import normal_char, caps_normal_char, send_name
from manipulationWithName import returnWithoutSmiles
from simple import dp, bot, types
from mongoDB import usersNameExists, getTriggerList, createColl, createNewTrigger, setDefaultTriggerChat, \
    defaultSmilesAreadyExists, updateDefaultSmilesChat, triggerChatExists, updateChatTrigger


@dp.message_handler(commands=["Гир", "гир", "gir", "Gir"], commands_prefix="!/.")
async def send_ready_nick(message: types.Message):
    if message.reply_to_message:
        membersName = message.reply_to_message.from_user.first_name
        membersId = message.reply_to_message.from_user.id
    else:
        membersName = message.from_user.first_name
        membersId = message.from_user.id

    if not usersNameExists(membersId):
        ready_nick = returnWithoutSmiles(membersName)
        print(ready_nick)  # 0
        if ready_nick == 0:
            result = [i for i in membersName if i in normal_char or i in caps_normal_char]
            ready_nick = "".join(result).lstrip()
            print(ready_nick)  # Камoл
            if len(ready_nick) == 0:
                ready_nick = membersName
    else:
        ready_nick = usersNameExists(membersId)

    try:
        ready_name = send_name(chat_id=message.chat.id, name=ready_nick, color=message.text.split()[1])
        #  'is_active'
        print(ready_name)
        await message.answer(ready_name)
    except IndexError:
        ooo = send_name(chat_id=message.chat.id, name=ready_nick, default=True, color=0)
        if not ooo == 'Такого триггера не существует':
            await message.answer(ooo)
        else:
            await message.answer(f'🎻ʀᴇ|{ready_nick}🌅')

    if not message.chat.title is None:
        await bot.send_message(chat_report, f'{message.from_user.first_name} использовал {message.text} в '
                                            f'{message.chat.title}(#{message.chat.id})')
    else:
        await bot.send_message(chat_report, f'{message.from_user.first_name} использовал {message.text} в '
                                            f'в приватном чате(#{message.chat.id})')


@dp.message_handler(commands=['aki', 'Aki'], is_admin=True, commands_prefix='!/.')
async def addNewTriggerChatToColl(msg: types.Message):
    if not msg.chat.type == 'private':
        try:
            if not msg.reply_to_message:
                message = msg.text.split()
                trigger_name = message[1]
                ind = msg.text.find(message[2])
                value = msg.text[ind:]

                index = value.find('NAME')
                if not index == -1:
                    res = [value[:index], value[index + 4:]]
                else:
                    res = value
            else:
                trigger_name = msg.text.split()[1]
                value = msg.reply_to_message.text

                index = value.find('NAME')
                if not index == -1:
                    res = [value[:index], value[index + 4:]]
                else:
                    res = value

            if not triggerChatExists(chatId=msg.chat.id, trigger_name=trigger_name):
                createNewTrigger(collect_name=msg.chat.id, trigger_name=trigger_name, trigger_value=res)
            else:
                updateChatTrigger(chatId=msg.chat.id, trigger_name=trigger_name, trigger_value=res)
            await msg.answer(f'Триггер <code>{trigger_name}</code> добавлен в список. Используйте /list_triggers чтобы '
                             f'получить список.', parse_mode='HTML')
        except IndexError:
            await msg.answer("Недостаточно аргументов. \nПример команды: `!aki [trigger] [sample]`\n"
                             "[Подробнее о sample(шаблонах) читайте тут](https://t.me/savonarola_chan/2)",
                             parse_mode='Markdown', disable_web_page_preview=True)
    else:
        await msg.answer('Используйте команду в чате.')


@dp.message_handler(commands=['aki'], commands_prefix='!/.')
async def addNewTriggerChatToCollbyCreator(msg: types.Message):
    if msg.from_user.id == creator:
        message = msg.text.split()
        trigger_name = message[1]
        ind = msg.text.find(message[2])
        value = msg.text[ind:]

        index = value.find('NAME')
        if not index == -1:
            res = [value[:index], value[index + 4:]]
        else:
            res = value

        createNewTrigger(collect_name=msg.chat.id, trigger_name=trigger_name, trigger_value=res)
        await msg.answer(f'Триггер <code>{trigger_name}</code> добавлен в список. Используйте /list_triggers чтобы '
                         f'получить список.', parse_mode='HTML')


@dp.message_handler(commands=['default'], is_admin=True, commands_prefix='!/.')
async def addNewDefaultTriggerChatToColl(msg: types.Message):
    try:
        if msg.reply_to_message:
            value = msg.reply_to_message.text[9:]
        else:
            value = msg.text[9:]

        index = value.find('NAME')
        if not index == -1:
            res = [value[:index], value[index + 4:]]
        else:
            res = value

        if not defaultSmilesAreadyExists(msg.chat.id):
            setDefaultTriggerChat(chat_id=msg.chat.id, chatName=msg.chat.title, trigger_value=res)
            await msg.answer(f'Установлены новые смайлы по умолчанию.🔥\nИспользуйте /list_triggers чтобы получить '
                             f'список всех триггеров этого чата.', parse_mode='HTML')
        else:
            updateDefaultSmilesChat(chat_id=msg.chat.id, default_trigger=res)
            await msg.answer(f'Обновлены смайлы по умолчанию.🔥\nИспользуйте /list_triggers чтобы получить '
                             f'список всех триггеров этого чата.', parse_mode='HTML')
    except IndexError:
        await msg.answer('Недостаточно аргументов. ')


@dp.message_handler(commands=['list', 'triggers', 'chat_triggers', 'list_triggers'], commands_prefix='/!.#')
async def sendTriggerList(message: types.Message):
    if not message.chat.type == 'private':
        await message.answer(f'{getTriggerList(message.chat.id)}')
    else:
        await message.answer('Команда используется в чате.')