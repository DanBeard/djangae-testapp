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
from .django_model_tests.update.tests import *
from .django_model_tests.update.models import *
from .django_model_tests.update_only_fields.tests import *
from .django_model_tests.update_only_fields.models import *
from .django_model_tests.ordering.tests import *
from .django_model_tests.ordering.models import *


from unittest import expectedFailure

ProxyModelTests.test_proxy_load_from_fixture = expectedFailure(ProxyModelTests.test_proxy_load_from_fixture) #Can't load fixture due to hacky importing
AdvancedTests.test_update_fk = expectedFailure(AdvancedTests.test_update_fk) #Attempts to do a join
CustomPKTests.test_custom_pk = expectedFailure(CustomPKTests.test_custom_pk) #Attempts to do a join
DeletionTests.test_m2m = expectedFailure(DeletionTests.test_m2m) #"M2M test, not supported"
FastDeleteTests.test_fast_delete_joined_qs = expectedFailure(FastDeleteTests.test_fast_delete_joined_qs) #Attempts to do a join
ModelToDictTests.test_model_to_dict_many_to_many = expectedFailure(ModelToDictTests.test_model_to_dict_many_to_many) #M2M test, not supported
OneToOneTests.test_manager_get = expectedFailure(OneToOneTests.test_manager_get) #Attempts to do a join, although this could be inheritence, check this again later
ProxyModelTests.test_proxy_included_in_ancestors = expectedFailure(ProxyModelTests.test_proxy_included_in_ancestors) # Unsupported aggregate, although I think it's just a MAX so perhaps possible?
SimpleTest.test_empty_update_with_inheritance = expectedFailure(SimpleTest.test_empty_update_with_inheritance) #Attempts to do a join, although perhaps inheritence?
SimpleTest.test_nonempty_update_with_inheritance = expectedFailure(SimpleTest.test_nonempty_update_with_inheritance) #Attempts to do a join, although perhaps inheritence?
UniqueTest.test_inherited_unique = expectedFailure(UniqueTest.test_inherited_unique) # Attempts a join
UpdateOnlyFieldsTests.test_select_related_only_interaction = expectedFailure(UpdateOnlyFieldsTests.test_select_related_only_interaction) # Cross-table select
UpdateOnlyFieldsTests.test_update_fields_fk_defer = expectedFailure(UpdateOnlyFieldsTests.test_update_fields_fk_defer)

#This is a weird one. The Django test does this:
#         assert_filter_waiters(restaurant=self.p1.pk)
#         assert_filter_waiters(restaurant=self.r)
#         assert_filter_waiters(id__exact=self.p1.pk) # <<- WTF? Get the waiter by the place ID?
# This must only work in normal Django because the IDs are sequential, and it just so happens that this is the same ID as the place
# so I'm skipping it. TODO: Check and see if this exists in Django trunk and file a bug
OneToOneTests.test_foreign_key = expectedFailure(OneToOneTests.test_foreign_key)

ProxyModelTests.test_with_data = expectedFailure(ProxyModelTests.test_with_data) #Attempts a join
ProxyModelTests.test_proxy_bug = expectedFailure(ProxyModelTests.test_proxy_bug) #Attempts a join
