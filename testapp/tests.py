import os
import tempfile
import sys

TEMP_DIR = tempfile.mkdtemp(prefix='django_')
os.environ['DJANGO_TEST_TEMP_DIR'] = TEMP_DIR

try:
    original_path = sys.path[:]
    sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "django_model_tests"))

    for test_folder in (
        "model_forms",
        "get_or_create",
        "basic",
        "custom_managers",
        "custom_pk",
        "delete",
        "one_to_one",
        "proxy_models",
        "update",
        "update_only_fields",
        "ordering"):

        mod = __import__(test_folder, globals(), locals(), fromlist=["tests", "models"])

        for f in ("tests", "models"):
            fi = getattr(mod, f)
            for k in dir(fi):
                if not k.startswith("__"):
                    attr = getattr(fi, k)
                    globals()[k] = attr

finally:
    sys.path = original_path

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
GetOrCreateThroughManyToMany.test_create_get_or_create = expectedFailure(GetOrCreateThroughManyToMany.test_create_get_or_create) #M2M
GetOrCreateThroughManyToMany.test_get_get_or_create = expectedFailure(GetOrCreateThroughManyToMany.test_get_get_or_create) #M2M
GetOrCreateThroughManyToMany.test_something = expectedFailure(GetOrCreateThroughManyToMany.test_something) #M2M

#This is a weird one. The Django test does this:
#         assert_filter_waiters(restaurant=self.p1.pk)
#         assert_filter_waiters(restaurant=self.r)
#         assert_filter_waiters(id__exact=self.p1.pk) # <<- WTF? Get the waiter by the place ID?
# This must only work in normal Django because the IDs are sequential, and it just so happens that this is the same ID as the place
# so I'm skipping it. TODO: Check and see if this exists in Django trunk and file a bug
OneToOneTests.test_foreign_key = expectedFailure(OneToOneTests.test_foreign_key)

OldFormForXTests.test_with_data = expectedFailure(OldFormForXTests.test_with_data) #Attempts a join
ProxyModelTests.test_proxy_bug = expectedFailure(ProxyModelTests.test_proxy_bug) #Attempts a join
