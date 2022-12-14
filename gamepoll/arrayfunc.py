from gamepoll.addingList import getListPeaces
from gamepoll.arraySamples import mainPiece

resurgence = {
    1: "๐",
    2: "๐",
    3: "๐",
    4: "๐",
    5: "๐",
    6: "๐",
    7: "๐",
    8: "๐",
    9: "๐",
    10: "๐"
}

doesNotExists = {
    1: "1 {0}",
    2: "2 {0}",
    3: "3 {0}",
    4: "4 {0}",
    5: "5 {0}",
    6: "6 {0}",
    7: "7 {0}",
    8: "8 {0}",
    9: "9 {0}",
    10: "10 {0}"
}

doesNotExistsBaku = {
    1: "1 {0}",
    2: "2 {0}",
    3: "3 {0}",
    4: "4 {0}",
    5: "5 {0}",
    6: "6 {0}",
    7: "7 {0}",
    8: "8 {0}",
    9: "9 {0}",
    10: "10 {0}",
    11: "11 {0}",
    12: "12 {0}",
    13: "13 {0}",
    14: "14 {0}",
    15: "15 {0}"
}

fifi = {
    1: "           1.",
    2: "                     2.",
    3: "     3.",
    4: "                4.",
    5: "5.",
    6: "              6.",
    7: "                         7.",
    8: "      8.",
    9: "                 9.",
    10: "10."
}


freeWill = {
    1: "๐ แ {0}  โโ,",
    2: "            ๐ ๐งท {0}  ๐",
    3: "                        ๐ เป {0}  โโ,",
    4: "๐ แ {0}  โโ,",
    5: "            ๐ ๐งท {0}  ๐",
    6: "                        ๐ เป {0} โโ,",
    7: "๐ แ {0}  โโ,",
    8: "            ๐ ๐งท {0} ๐",
    9: "                        ๐ เป {0}  โโ,",
    10: "๐ แ {0}  โโ,"
}

freeWillBaku = {
    1: "๐ แ {0}  โโ,",
    2: "            ๐ ๐งท {0}  ๐",
    3: "                        ๐ เป {0}  โโ,",
    4: "๐ แ {0}  โโ,",
    5: "            ๐ ๐งท {0}  ๐",
    6: "                        ๐ เป {0} โโ,",
    7: "๐ แ {0}  โโ,",
    8: "            ๐ ๐งท {0} ๐",
    9: "                        ๐ เป {0}  โโ,",
    10: "๐ แ {0}  โโ,",
    11: "            ๐ ๐งท {0} ๐",
    12: "                        ๐ เป {0}  โโ,",
    13: "๐ แ {0}  โโ,",
    14: "            ๐ ๐งท {0}  ๐",
    15: "                        ๐ เป {0}  โโ"
}


memento_mori = {
    "๐ โ  {}",
    "๐ โ  {}",
    "๐ โ  {}",
    "๐ โ  {}",
    "๐ โ  {}.  ๐๐๐๐๐๐๐",
    "๐ โ  {}",
    "ล โ  {}}",
    "๐ โ  {}",
    "๐ โ  {}",
    "๐ โ  {}"
}


def MafiaArray(usernames, isTrue, captain='@captain', team=0):
        if isTrue:
            bot = 'True'
            list_game = doesNotExists
        else:
            bot = 'Baku'
            list_game = doesNotExistsBaku

        res = ""
        maxlen = len(usernames)
        if not type(usernames) == bool:
            if not mainPiece(chat_id=team, bot=bot) is None:
                for i in range(1, len(mainPiece(chat_id=team, bot=bot).values()) + 1):
                    if i > maxlen:
                        break
                    else:
                        res = f"{res}\n{mainPiece(chat_id=team, bot=bot)[i].format(usernames[i - 1])}"

                res = f'{getListPeaces(chat_id=team, opening=True, bot=bot).format(captain)}\n{res}\n' \
                      f'{getListPeaces(chat_id=team, ending=True, bot=bot)}'
                return res
            else:
                for i in range(1, len(list_game.values()) + 1):
                    if i > maxlen:
                        break
                    else:
                        res = f"{res}\n{list_game[i].format(usernames[i - 1])}"

                res = f'Cap: {captain}\n{res}'
                return res
