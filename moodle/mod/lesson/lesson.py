from moodle.attr import dataclass
from typing import List, Optional
from moodle import MoodleWarning, ResponsesFactory


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
    filename: Optional[str]
    filepath: Optional[str]
    filesize: Optional[int]
    fileurl: Optional[str]
    timemodified: Optional[int]
    mimetype: Optional[str]
    isexternalfile: Optional[int]
    repositorytype: Optional[str]


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
    intro: Optional[str]
    introformat: int
    practice: Optional[int]
    modattempts: Optional[int]
    usepassword: Optional[int]
    password: Optional[str]
    dependency: Optional[int]
    conditions: Optional[str]
    grade: Optional[int]
    custom: Optional[int]
    ongoing: Optional[int]
    usemaxgrade: Optional[int]
    maxanswers: Optional[int]
    maxattempts: Optional[int]
    review: Optional[int]
    nextpagedefault: Optional[int]
    feedback: Optional[int]
    minquestions: Optional[int]
    maxpages: Optional[int]
    timelimit: Optional[int]
    retake: Optional[int]
    activitylink: Optional[int]
    mediafile: Optional[str]
    mediaheight: Optional[int]
    mediawidth: Optional[int]
    mediaclose: Optional[int]
    slideshow: Optional[int]
    width: Optional[int]
    height: Optional[int]
    bgcolor: Optional[str]
    displayleft: Optional[int]
    displayleftif: Optional[int]
    progressbar: Optional[int]
    available: Optional[int]
    deadline: Optional[int]
    timemodified: Optional[int]
    completionendreached: Optional[int]
    completiontimespent: Optional[int]
    allowofflineattempts: int
    introfiles: List[File]
    mediafiles: List[File]


@dataclass
class OneLesson:
    lesson: Lesson
    warnings: List[MoodleWarning]


@dataclass
class Lessons(ResponsesFactory[Lesson]):
    lessons: List[Lesson]
    warnings: List[MoodleWarning]

    @property
    def items(self) -> List[Lesson]:
        return self.lessons
