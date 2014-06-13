import os
import tempfile

TEMP_DIR = tempfile.mkdtemp(prefix='django_')
os.environ['DJANGO_TEST_TEMP_DIR'] = TEMP_DIR

from .django_model_tests.model_forms.tests import *
from .django_model_tests.model_forms.models import *
from .django_model_tests.get_or_create.tests import *
from .django_model_tests.get_or_create.models import *
from .django_model_tests.basic.tests import *
from .django_model_tests.basic.models import *
from .django_model_tests.custom_managers.tests import *
from .django_model_tests.custom_managers.models import *
from .django_model_tests.custom_pk.tests import *
from .django_model_tests.custom_pk.models import *
from .django_model_tests.delete.tests import *
from .django_model_tests.delete.models import *