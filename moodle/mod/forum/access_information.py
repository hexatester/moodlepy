from typing import List, Optional

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class AccessInformation:
    """Forum Access Information
    Args:
        warnings (List[Warning]): list of warnings
        canaddinstance (Optional[int]): Whether the user has the capability mod/forum:addinstance allowed.
        canviewdiscussion (Optional[int]): Whether the user has the capability mod/forum:viewdiscussion allowed.
        canviewhiddentimedposts (Optional[int]): Whether the user has the capability mod/forum:viewhiddentimedposts allowed.
        canstartdiscussion (Optional[int]): Whether the user has the capability mod/forum:startdiscussion allowed.
        canreplypost (Optional[int]): Whether the user has the capability mod/forum:replypost allowed.
        canaddnews (Optional[int]): Whether the user has the capability mod/forum:addnews allowed.
        canreplynews (Optional[int]): Whether the user has the capability mod/forum:replynews allowed.
        canviewrating (Optional[int]): Whether the user has the capability mod/forum:viewrating allowed.
        canviewanyrating (Optional[int]): Whether the user has the capability mod/forum:viewanyrating allowed.
        canviewallratings (Optional[int]): Whether the user has the capability mod/forum:viewallratings allowed.
        canrate (Optional[int]): Whether the user has the capability mod/forum:rate allowed.
        canpostprivatereply (Optional[int]): Whether the user has the capability mod/forum:postprivatereply allowed.
        canreadprivatereplies (Optional[int]): Whether the user has the capability mod/forum:readprivatereplies allowed.
        cancreateattachment (Optional[int]): Whether the user has the capability mod/forum:createattachment allowed.
        candeleteownpost (Optional[int]): Whether the user has the capability mod/forum:deleteownpost allowed.
        candeleteanypost (Optional[int]): Whether the user has the capability mod/forum:deleteanypost allowed.
        cansplitdiscussions (Optional[int]): Whether the user has the capability mod/forum:splitdiscussions allowed.
        canmovediscussions (Optional[int]): Whether the user has the capability mod/forum:movediscussions allowed.
        canpindiscussions (Optional[int]): Whether the user has the capability mod/forum:pindiscussions allowed.
        caneditanypost (Optional[int]): Whether the user has the capability mod/forum:editanypost allowed.
        canviewqandawithoutposting (Optional[int]): Whether the user has the capability mod/forum:viewqandawithoutposting allowed.
        canviewsubscribers (Optional[int]): Whether the user has the capability mod/forum:viewsubscribers allowed.
        canmanagesubscriptions (Optional[int]): Whether the user has the capability mod/forum:managesubscriptions allowed.
        canpostwithoutthrottling (Optional[int]): Whether the user has the capability mod/forum:postwithoutthrottling allowed.
        canexportdiscussion (Optional[int]): Whether the user has the capability mod/forum:exportdiscussion allowed.
        canexportpost (Optional[int]): Whether the user has the capability mod/forum:exportpost allowed.
        canexportownpost (Optional[int]): Whether the user has the capability mod/forum:exportownpost allowed.
        canaddquestion (Optional[int]): Whether the user has the capability mod/forum:addquestion allowed.
        canallowforcesubscribe (Optional[int]): Whether the user has the capability mod/forum:allowforcesubscribe allowed.
        cancanposttomygroups (Optional[int]): Whether the user has the capability mod/forum:canposttomygroups allowed.
        cancanoverridediscussionlock (Optional[int]): Whether the user has the capability mod/forum:canoverridediscussionlock allowed.
        cancanoverridecutoff (Optional[int]): Whether the user has the capability mod/forum:canoverridecutoff allowed.
        cancantogglefavourite (Optional[int]): Whether the user has the capability mod/forum:cantogglefavourite allowed.
    """
    warnings: List[MoodleWarning] = field(factory=list)
    canaddinstance: Optional[int] = None
    canviewdiscussion: Optional[int] = None
    canviewhiddentimedposts: Optional[int] = None
    canstartdiscussion: Optional[int] = None
    canreplypost: Optional[int] = None
    canaddnews: Optional[int] = None
    canreplynews: Optional[int] = None
    canviewrating: Optional[int] = None
    canviewanyrating: Optional[int] = None
    canviewallratings: Optional[int] = None
    canrate: Optional[int] = None
    canpostprivatereply: Optional[int] = None
    canreadprivatereplies: Optional[int] = None
    cancreateattachment: Optional[int] = None
    candeleteownpost: Optional[int] = None
    candeleteanypost: Optional[int] = None
    cansplitdiscussions: Optional[int] = None
    canmovediscussions: Optional[int] = None
    canpindiscussions: Optional[int] = None
    caneditanypost: Optional[int] = None
    canviewqandawithoutposting: Optional[int] = None
    canviewsubscribers: Optional[int] = None
    canmanagesubscriptions: Optional[int] = None
    canpostwithoutthrottling: Optional[int] = None
    canexportdiscussion: Optional[int] = None
    canexportpost: Optional[int] = None
    canexportownpost: Optional[int] = None
    canaddquestion: Optional[int] = None
    canallowforcesubscribe: Optional[int] = None
    cancanposttomygroups: Optional[int] = None
    cancanoverridediscussionlock: Optional[int] = None
    cancanoverridecutoff: Optional[int] = None
    cancantogglefavourite: Optional[int] = None
