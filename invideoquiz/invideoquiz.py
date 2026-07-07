"""
This XBlock allows for edX components to be displayed to users inside of
videos at specific time points.
"""

# Installed packages (via pip)
from django.template import Context, Template
from django.utils.translation import gettext_lazy as _
import os
import pkg_resources

# Edx dependencies
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin


def get_resource_string(path):
    """
    Retrieve string contents for the file path
    """
    path = os.path.join('public', path)
    resource_string = pkg_resources.resource_string(__name__, path)
    return resource_string.decode('utf8')


class InVideoQuizXBlock(StudioEditableXBlockMixin, XBlock):
    # pylint: disable=too-many-ancestors
    """
    Display CAPA problems within a video component at a specified time.
    """

    show_in_read_only_mode = True

    display_name = String(
        display_name=_('Display Name'),
        default='In-Video Quiz XBlock',
        scope=Scope.settings,
    )

    video_id = String(
        display_name=_('Video ID'),
        default='',
        scope=Scope.settings,
        help=_(
            'This is the component ID for the video in which '
            'you want to insert your quiz question.'
        ),
    )

    timemap = String(
        display_name=_('Problem Timemap'),
        default='{}',
        scope=Scope.settings,
        help=_(
            'A simple string field to define problem IDs '
            'and their time maps (in seconds) as JSON. '
            'Example: {"60": "50srvqlii4ru9gonprp35gkcfyd5weju"}'
        ),
        multiline_editor=True,
    )

    editable_fields = [
        'video_id',
        'timemap',
    ]

    def render_template(self, template_path, context):
        template_str = get_resource_string(template_path)
        template = Template(template_str)
        return template.render(Context(context))

    # Decorate the view in order to support multiple devices e.g. mobile
    # See: https://openedx.atlassian.net/wiki/display/MA/Course+Blocks+API
    # section 'View @supports(multi_device) decorator'
    @XBlock.supports('multi_device')
    def student_view(self, context=None):  # pylint: disable=unused-argument
        """
        Show to students when viewing courses
        """
        context={
            'video_id': self.video_id,
            'user_mode': self.user_mode,
            'timemap': self.timemap,
        }
        template = self.render_template(
            'html/invideoquiz.html', context)
        frag = Fragment(template)
        frag.add_css(str(get_resource_string("css/invideoquiz.css")))
        frag.add_javascript(str(get_resource_string("js/src/invideoquiz.js")))
        frag.initialize_js('InVideoQuizXBlock')
        return frag

    @property
    def user_mode(self):
        """
        Check user's permission mode for this XBlock.
        Returns:
            user permission mode
        """
        try:
            if self.xmodule_runtime.user_is_staff:
                return 'staff'
        except AttributeError:
            pass
        return 'student'

    @staticmethod
    def workbench_scenarios():
        """
        A canned scenario for display in the workbench.
        """
        return [
            ("InVideoQuizXBlock",
             """<in-video-quiz-block display_name='In-Video Quiz XBlock' video_id='###' timemap='{ 10: "###" }' />
             """),
            ("Multiple InVideoQuizXBlock",
             """<vertical_demo>
                <in-video-quiz-block display_name='In-Video Quiz XBlock' video_id='###' timemap='{ 10: "###" }' />
                <in-video-quiz-block display_name='In-Video Quiz XBlock' video_id='###' timemap='{ 10: "###" }' />
                <in-video-quiz-block display_name='In-Video Quiz XBlock' video_id='###' timemap='{ 10: "###" }' />
                </vertical_demo>
             """),
        ]
