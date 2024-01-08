from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class File:
    """File
    Args:
        filename (Optional[str]): File name.
        filepath (Optional[str]): File path.
        filesize (Optional[int]): File size.
        fileurl (Optional[str]): Downloadable file url.
        timemodified (Optional[int]): Time modified.
        mimetype (Optional[str]): File mime type.
        isexternalfile (Optional[int]): Whether is an external file.
        repositorytype (Optional[str]): The repository type for the external files.
    """

    filename: Optional[str] = None
    filepath: Optional[str] = None
    filesize: Optional[int] = None
    fileurl: Optional[str] = None
    timemodified: Optional[int] = None
    mimetype: Optional[str] = None
    isexternalfile: Optional[int] = None
    repositorytype: Optional[str] = None


@dataclass
class Lesson:
    """Lesson
    Args:
        id (int): Standard Moodle primary key.
        course (int): Foreign key reference to the course this lesson is part of.
        coursemodule (int): Course module id.
        name (str): Lesson name.
        intro (Optional[str]): Lesson introduction text.
        introformat (int): Default untuk "1" intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        practice (Optional[int]): Practice lesson?
        modattempts (Optional[int]): Allow student review?
        usepassword (Optional[int]): Password protected lesson?
        password (Optional[str]): Password
        dependency (Optional[int]): Dependent on (another lesson id)
        conditions (Optional[str]): Conditions to enable the lesson
        grade (Optional[int]): The total that the grade is scaled to be out of
        custom (Optional[int]): Custom scoring?
        ongoing (Optional[int]): Display ongoing score?
        usemaxgrade (Optional[int]): How to calculate the final grade
        maxanswers (Optional[int]): Maximum answers per page
        maxattempts (Optional[int]): Maximum attempts
        review (Optional[int]): Provide option to try a question again
        nextpagedefault (Optional[int]): Action for a correct answer
        feedback (Optional[int]): Display default feedback
        minquestions (Optional[int]): Minimum number of questions
        maxpages (Optional[int]): Number of pages to show
        timelimit (Optional[int]): Time limit
        retake (Optional[int]): Re-takes allowed
        activitylink (Optional[int]): Id of the next activity to be linked once the lesson is completed
        mediafile (Optional[str]): Local file path or full external URL
        mediaheight (Optional[int]): Popup for media file height
        mediawidth (Optional[int]): Popup for media with
        mediaclose (Optional[int]): Display a close button in the popup?
        slideshow (Optional[int]): Display lesson as slideshow
        width (Optional[int]): Slideshow width
        height (Optional[int]): Slideshow height
        bgcolor (Optional[str]): Slideshow bgcolor
        displayleft (Optional[int]): Display left pages menu?
        displayleftif (Optional[int]): Minimum grade to display menu
        progressbar (Optional[int]): Display progress bar?
        available (Optional[int]): Available from
        deadline (Optional[int]): Available until
        timemodified (Optional[int]): Last time settings were updated
        completionendreached (Optional[int]): Require end reached for completion?
        completiontimespent (Optional[int]): Student must do this activity at least for
        allowofflineattempts (int): Whether to allow the lesson to be attempted offline in the mobile app
        introfiles (List[File]): introfiles
        mediafiles (List[File]): mediafiles
    """

    id: int
    course: int
    coursemodule: int
    name: str
    introformat: int
    allowofflineattempts: int
    intro: Optional[str] = None
    practice: Optional[int] = None
    modattempts: Optional[int] = None
    usepassword: Optional[int] = None
    password: Optional[str] = None
    dependency: Optional[int] = None
    conditions: Optional[str] = None
    grade: Optional[int] = None
    custom: Optional[int] = None
    ongoing: Optional[int] = None
    usemaxgrade: Optional[int] = None
    maxanswers: Optional[int] = None
    maxattempts: Optional[int] = None
    review: Optional[int] = None
    nextpagedefault: Optional[int] = None
    feedback: Optional[int] = None
    minquestions: Optional[int] = None
    maxpages: Optional[int] = None
    timelimit: Optional[int] = None
    retake: Optional[int] = None
    activitylink: Optional[int] = None
    mediafile: Optional[str] = None
    mediaheight: Optional[int] = None
    mediawidth: Optional[int] = None
    mediaclose: Optional[int] = None
    slideshow: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    bgcolor: Optional[str] = None
    displayleft: Optional[int] = None
    displayleftif: Optional[int] = None
    progressbar: Optional[int] = None
    available: Optional[int] = None
    deadline: Optional[int] = None
    timemodified: Optional[int] = None
    completionendreached: Optional[int] = None
    completiontimespent: Optional[int] = None
    introfiles: List[File] = field(factory=list)
    mediafiles: List[File] = field(factory=list)


@dataclass
class OneLesson:
    lesson: Lesson
    warnings: List[MoodleWarning] = field(factory=list)


@dataclass
class Lessons(ResponsesFactory[Lesson]):
    lessons: List[Lesson] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Lesson]:
        return self.lessons
