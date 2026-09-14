"""Тикет 0: парсер лога осады.

Запуск: python3 siege.py siege_log.txt
"""

import sys
from cmath import inf


def main(path: str) -> None:
    # TODO: прочитать лог, посчитать урон, напечатать строки вида
    # "Игрок <Имя> из гильдии <Тег> нанес <Урон> по воротам."
    file = open('siege_log.txt').readlines()[2::]
    for line in file:
        data = [a.strip() for a in line.split('|')]
        if len(data) == 5 and data[4] != '7':
            data[0] = data[0] + data[1]
            del data[1]
        """
        data[0] - гильдия + ник
        data[1] - базовый урон
        data[2] - множитель состояния
        data[3] - количество бафов
        """
        guild, nickname = GuildAndNickname(data[0])
        try:
            data[2]
        except Exception:
            data.append('None')
        try:
            data[3]
        except Exception:
            data.append(0)
        damages = damage(data[1], data[2], data[3])


        print(f'Игрок {nickname} из гильдии {guild} нанес {round(damages, 2)} по воротам.')

def GuildAndNickname(username):
        if ']' in username:
            guild, separator, nickname = username.partition("]")
            if '[' in guild:
                rest, separator, guild = guild.partition("[")
        else:
            guild = ''
            nickname = username
        guild = guild.replace('[', '')
        if guild == '':
            guild = '--'
        if nickname[0] == ']':
            nickname = nickname[1:]
        return guild, nickname
def conditiondef (condition):
    if condition.lower() == 'active':
        return 1.5
    elif condition == 'None':
        return 1
    else:
        return 0.5
def buff (buffs):
    if buff == '' or 'N/A':
        return 0
    else:
        return float(buffs)
def damage(base_damage, condition , buffs):
    return float(base_damage.replace(',','.').replace(' ','')) * conditiondef(condition) * (1 + 0.15 * buff(buffs))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "siege_log.txt")
