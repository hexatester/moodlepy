from dataclasses import dataclass
from typing import List, Optional
from moodle import MoodleWarning


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
    warnings: List[MoodleWarning]
    canaddinstance: Optional[int]
    canviewdiscussion: Optional[int]
    canviewhiddentimedposts: Optional[int]
    canstartdiscussion: Optional[int]
    canreplypost: Optional[int]
    canaddnews: Optional[int]
    canreplynews: Optional[int]
    canviewrating: Optional[int]
    canviewanyrating: Optional[int]
    canviewallratings: Optional[int]
    canrate: Optional[int]
    canpostprivatereply: Optional[int]
    canreadprivatereplies: Optional[int]
    cancreateattachment: Optional[int]
    candeleteownpost: Optional[int]
    candeleteanypost: Optional[int]
    cansplitdiscussions: Optional[int]
    canmovediscussions: Optional[int]
    canpindiscussions: Optional[int]
    caneditanypost: Optional[int]
    canviewqandawithoutposting: Optional[int]
    canviewsubscribers: Optional[int]
    canmanagesubscriptions: Optional[int]
    canpostwithoutthrottling: Optional[int]
    canexportdiscussion: Optional[int]
    canexportpost: Optional[int]
    canexportownpost: Optional[int]
    canaddquestion: Optional[int]
    canallowforcesubscribe: Optional[int]
    cancanposttomygroups: Optional[int]
    cancanoverridediscussionlock: Optional[int]
    cancanoverridecutoff: Optional[int]
    cancantogglefavourite: Optional[int]
