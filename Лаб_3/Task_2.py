# TODO Напишите функцию find_common_participants# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(participants_first_group, participants_second_group, separator=','):
  first_group = participants_first_group.split(separator)
  second_group = participants_second_group.split(separator)
  common_participant = list(set(first_group).intersection(second_group))
  common_participant.sort()
  common = sorted(common_participant)
  return common


# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants('Иванов*Петров*Сидоров','Петров*Сидоров*Смирнов', '*'))