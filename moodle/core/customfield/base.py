from moodle import BaseMoodle
from . import ReloadTemplate


class BaseCustomfield(BaseMoodle):
    def create_category(self, component: str, area: str, itemid: int) -> int:
        """Creates a new category

        Args:
            component (str): component
            area (str): area
            itemid (int): itemid

        Returns:
            int: Id of the category
        """
        data = self.moodle.post(
            "core_customfield_create_category",
            component=component,
            area=area,
            itemid=itemid,
        )
        return data

    def delete_category(self, id: int) -> None:
        """Deletes a category

        Args:
            id (int): category ID to delete
        """
        self.moodle.post("core_customfield_delete_category", id=id)

    def delete_field(self, id: int) -> None:
        """Deletes an entry

        Args:
            id (int): Custom field ID to delete
        """
        self.moodle.post("core_customfield_delete_field", id=id)

    def move_category(self, id: int, beforeid: int = 0) -> None:
        """Drag and drop categories

        Args:
            id (int): Category ID to move
            beforeid (int, optional): Id of the category before which it needs to be moved. Defaults to 0.
        """
        self.moodle.post(
            "core_customfield_move_category",
            id=id,
            beforeid=beforeid,
        )

    def move_field(self, id: int, categoryid: int, beforeid: int = 0) -> None:
        """Drag and drop

        Args:
            id (int): Id of the field to move
            categoryid (int): New parent category id
            beforeid (int, optional): Id of the field before which it needs to be moved. Defaults to 0.
        """
        self.moodle.post(
            "core_customfield_move_field",
            id=id,
            categoryid=categoryid,
            beforeid=beforeid,
        )

    def reload_template(self, component: str, area: str, itemid: int) -> ReloadTemplate:
        """Reloads template

        Args:
            component (str): component
            area (str): area
            itemid (int): itemid

        Returns:
            ReloadTemplate: Response
        """
        data = self.moodle.post(
            "core_customfield_reload_template",
            component=component,
            area=area,
            itemid=itemid,
        )
        return self._tr(ReloadTemplate, **data)
