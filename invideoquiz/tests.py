# -*- coding: utf-8 -*-
# Python Standard Libraries
import logging

# Installed packages (via pip)
from mock import Mock

# Edx dependencies
from common.djangoapps.util.testing import UrlResetMixin
from xblock.field_data import DictFieldData
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase

# Internal project dependencies
from .invideoquiz import InVideoQuizXBlock

logger = logging.getLogger(__name__)

class TestInVideoQuizXBlock(UrlResetMixin, ModuleStoreTestCase):
    def setUp(self):
        super(TestInVideoQuizXBlock, self).setUp()
        self.xblock = InVideoQuizXBlock(Mock(), DictFieldData({}), Mock())
    
    def test_workbench_scenarios(self):
        """
            Checks workbench scenarios title and basic scenario
        """
        result_title = 'InVideoQuizXBlock'
        basic_scenario = "<in-video-quiz-block display_name="
        test_result = self.xblock.workbench_scenarios()
        self.assertEqual(result_title, test_result[0][0])
        self.assertIn(basic_scenario, test_result[0][1])

    def test_student_view(self):
        """
            Check if xblock template loaded correctly
        """
        student_view = self.xblock.student_view()
        student_view_html = student_view.content
        self.assertIn('in-video-quiz-block', student_view_html)
