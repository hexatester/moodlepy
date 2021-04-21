from typing import List, Optional

from moodle import ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class Response:
    """Response when calling external function
    Constructor arguments:
    params: error (int): Whether an exception was thrown.
    params: data (str): JSON-encoded response data
    params: exception (str): JSON-encoed exception info
    """

    error: int
    data: str
    exception: str


@dataclass
class FunctionsResponses(ResponsesFactory[Response]):
    responses: List[Response] = field(factory=list)

    @property
    def items(self) -> List[Response]:
        return self.responses

    @dataclass
    class Request:
        """For requesting external function
        Constructor arguments:
        params: function (str): Function name
        params: arguments (str): Default for "{}" //JSON-encoded object with named arguments
        params: settingraw (int): Default for "" //Return raw text
        params: settingfilter (int): Default for "" //Filter text
        params: settingfileurl (int): Default for "1" //Rewrite plugin file URLs
        params: settinglang (str): Default for "" //Session language
        """

        function: str
        arguments: str = "{}"
        settingraw: Optional[int] = None
        settingfilter: Optional[int] = None
        settingfileurl: int = 1
        settinglang: str = ""
