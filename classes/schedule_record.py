from dataclasses import dataclass


# Объект, отражающий запись о занятии
# class_id = номер пары
# class_name = названия дисциплины
# class_room = номер аудитории
# teacher_name = имя преподавателя
# week_day = день недели
@dataclass
class ScheduleRecord:
    class_id: int
    class_name: str
    class_room: str
    teacher_name: str
    week_day: str
