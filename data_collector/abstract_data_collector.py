import abc

from classes.schedule_record import ScheduleRecord


class AbstractDataCollector(abc.ABC):
    # Возвращает словарь доступных факультетов/институтов, где:
    # Ключ - название факультета/института
    # Значение - уникальный идентификатор данного факультета/института
    def get_departments_dict(self) -> dict[str, int]:
        ...

    # Возвращает словарь доступных потоков для данного факультета/института, где:
    # Ключ - название потока
    # Значение - уникальный идентификатор данного потока
    # На входе ожидается уникальный идентификатор факультета/института
    def get_departments_streams_dict(self, department_id: int) -> dict[str, int]:
        ...

    # Возвращает словарь доступных групп для данного факультета/института и потока, где:
    # Ключ - название группы
    # Значение - уникальный идентификатор данной группы
    # На входе ожидается уникальный идентификатор факультета/института и потока
    def get_groups_dict(self, department_id: int, stream_id: int) -> dict[str, int]:
        ...

    # Возвращает словарь расписания для данной группы, где:
    # Ключ - дата занятия
    # Значение - список объектов ScheduleRecord
    # На входе ожидается уникальный идентификатор группы
    def get_schedule(self, group_id: int) -> dict[str, ScheduleRecord]:
        ...
