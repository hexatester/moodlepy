from typing import List, Optional

from moodle import ResponsesFactory, MoodleWarning
from moodle.attr import dataclass, fields


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
        repositorytype (Optional[str]): The repository type for external files.
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
class Config:
    """Config
    Args
        id (Optional[int]): assign_plugin_config id
        assignment (Optional[int]): assignment id
        plugin (str): plugin
        subtype (str): subtype
        name (str): name
        value (str): value
    """
    id: Optional[int]
    assignment: Optional[int]
    plugin: str
    subtype: str
    name: str
    value: str


@dataclass
class Assignment:
    """Assigment
    Args:
        id (int): assignment id
        cmid (int): course module id
        course (int): course id
        name (str): assignment name
        nosubmissions (int): no submissions
        submissiondrafts (int): submissions drafts
        sendnotifications (int): send notifications
        sendlatenotifications (int): send notifications
        sendstudentnotifications (int): send student notifications (default)
        duedate (int): assignment due date
        allowsubmissionsfromdate (int): allow submissions from date
        grade (int): grade type
        timemodified (int): last time assignment was modified
        completionsubmit (int): if enabled, set activity as complete following submission
        cutoffdate (int): date after which submission is not accepted without an extension
        gradingduedate (int): the expected date for marking the submissions
        teamsubmission (int): if enabled, students submit as a team
        requireallteammemberssubmit (int): if enabled, all team members must submit
        teamsubmissiongroupingid (int): the grouping id for the team submission groups
        blindmarking (int): if enabled, hide identities until reveal identities actioned
        hidegrader (int): If enabled, hide grader to student
        revealidentities (int): show identities for a blind marking assignment
        attemptreopenmethod (str): method used to control opening new attempts
        maxattempts (int): maximum number of attempts allowed
        markingworkflow (int): enable marking workflow
        markingallocation (int): enable marking allocation
        requiresubmissionstatement (int): student must accept submission statement
        preventsubmissionnotingroup (Optional[int]): Prevent submission not in group
        submissionstatement (Optional[str]): Submission statement formatted.
        submissionstatementformat (int): submissionstatement format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        configs (Config): configuration settings
        intro (Optional[str]): assignment intro, not allways returned because it deppends on the activity configuration
        introformat (Optional[int]): intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        introfiles (List[File]): Files in the introduction text
        introattachments (List[File]): intro attachments files
    """
    id: int
    cmid: int
    course: int
    name: str
    nosubmissions: int
    submissiondrafts: int
    sendnotifications: int
    sendlatenotifications: int
    sendstudentnotifications: int
    duedate: int
    allowsubmissionsfromdate: int
    grade: int
    timemodified: int
    completionsubmit: int
    cutoffdate: int
    gradingduedate: int
    teamsubmission: int
    requireallteammemberssubmit: int
    teamsubmissiongroupingid: int
    blindmarking: int
    hidegrader: int
    revealidentities: int
    attemptreopenmethod: str
    maxattempts: int
    markingworkflow: int
    markingallocation: int
    requiresubmissionstatement: int
    preventsubmissionnotingroup: Optional[int]
    submissionstatement: Optional[str]
    submissionstatementformat: int
    configs: Config
    intro: Optional[str]
    introformat: Optional[int]
    introfiles: List[File] = fields(File)
    introattachments: List[File] = fields(File)


@dataclass
class AssignmentCourse(ResponsesFactory[Assignment]):
    """Courses with assignment
    Args:
        id (int): course id
        fullname (str): course full name
        shortname (str): course short name
        timemodified (int): last time modified
        assignments (List[Assignment]): assignment info
    """
    id: int
    fullname: str
    shortname: str
    timemodified: int
    assignments: List[Assignment] = fields(Assignment)

    @property
    def items(self) -> List[Assignment]:
        return self.assignments


@dataclass
class Assignments(ResponsesFactory[AssignmentCourse]):
    """Assigments from get assignments
    Args:
        courses (List[AssignmentCourse]): List of course with assigments
        warnings (List[Warning]): List of warnings
    """
    courses: List[AssignmentCourse] = fields(AssignmentCourse)
    warnings: List[MoodleWarning] = fields(MoodleWarning)

    @property
    def items(self) -> List[AssignmentCourse]:
        return self.courses
