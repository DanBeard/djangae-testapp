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
from .django_model_tests.one_to_one.tests import *
from .django_model_tests.one_to_one.models import *
from .django_model_tests.proxy_models.tests import *
from .django_model_tests.proxy_models.models import *
from .django_model_tests.timezones.tests import *
from .django_model_tests.timezones.models import *
from .django_model_tests.update.tests import *
from .django_model_tests.update.models import *
from .django_model_tests.update_only_fields.tests import *
from .django_model_tests.update_only_fields.models import *
from .django_model_tests.ordering.tests import *
from .django_model_tests.ordering.models import *