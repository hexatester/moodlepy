from typing import List

from moodle import BaseMoodle
from moodle.base.general import GeneralNameValue


class BaseData(BaseMoodle):
    def add_entry(self, databaseid: int, groupid: int, data: List[dict]):
        data = self.moodle.post(
            "mod_data_add_entry",
            databaseid=databaseid,
            groupid=groupid,
            data=data,
        )
        return data

    def approve_entry(self, entryid: int, approve: int = 1):
        data = self.moodle.post(
            "mod_data_approve_entry",
            entryid=entryid,
            approve=approve,
        )
        return data

    def delete_entry(self, entryid: int):
        data = self.moodle.post(
            "mod_data_delete_entry",
            entryid=entryid,
        )
        return data

    def get_data_access_information(self, databaseid: int, groupid: int = 0):
        data = self.moodle.post(
            "mod_data_get_data_access_information",
            databaseid=databaseid,
            groupid=groupid,
        )
        return data

    def get_databases_by_courses(self, courseids: List[int]):
        data = self.moodle.post(
            "mod_data_get_databases_by_courses",
            courseids=courseids,
        )
        return data

    def get_entries(
        self,
        databaseid: int,
        groupid: int = 0,
        returncontents: int = None,
        sort: int = None,
        page: int = 0,
        perpage: int = 0,
    ):
        data = self.moodle.post(
            "mod_data_get_entries",
            databaseid=databaseid,
            groupid=groupid,
            returncontents=returncontents or "",
            sort=sort,
            page=page,
            perpage=perpage,
        )
        return data

    def get_entry(self, entryid: int, returncontents: int = None):
        data = self.moodle.post(
            "mod_data_get_entry",
            entryid=entryid,
            returncontents=returncontents or "",
        )
        return data

    def get_fields(self, databaseid: int):
        data = self.moodle.post(
            "mod_data_get_fields",
            databaseid=databaseid,
        )
        return data

    def search_entries(
        self,
        databaseid: int,
        groupid: int = 0,
        returncontents: int = None,
        search: str = "",
        advsearch: List[GeneralNameValue] = None,
        sort: int = None,
        order: str = None,
        page: int = 0,
        perpage: int = 0,
    ):
        data = self.moodle.post(
            "mod_data_search_entries",
            databaseid=databaseid,
            groupid=groupid,
            returncontents=returncontents or "",
            search=search,
            advsearch=advsearch or list(),
            sort=sort,
            order=order,
            page=page,
            perpage=perpage,
        )
        return data

    def update_entry(self, entryid: int, data: List[dict]):
        data = self.moodle.post(
            "mod_data_update_entry",
            entryid=entryid,
            data=data,
        )
        return data

    def view_database(self, databaseid: int):
        data = self.moodle.post(
            "mod_data_view_database",
            databaseid=databaseid,
        )
        return data
