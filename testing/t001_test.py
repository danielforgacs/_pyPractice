import pytest
import time

WAIT_SECS = 2


@pytest.fixture(scope="module")
# @pytest.fixture()
def module_fixture():
    print('\n\n::: MODULE_FIXTURE')
    time.sleep(WAIT_SECS)
    print('::: MODULE_FIXTURE - DONE')
    return 5



@pytest.fixture(scope="class")
# @pytest.fixture()
def class_fixture():
    print('\n\n::: CLASS_FIXTURE')
    time.sleep(WAIT_SECS)
    print('::: CLASS_FIXTURE - DONE')
    return 6



class TestClass_TestStuff:
    def test_cls_01(self, class_fixture):
        assert class_fixture == 6

    def test_cls_02(self, class_fixture):
        assert class_fixture == 6

    def test_cls_03(self, class_fixture):
        assert class_fixture == 6

    def test_cls_04(self, class_fixture):
        assert class_fixture == 6




def test_things_01(module_fixture):
    assert module_fixture == 5

def test_things_02(module_fixture):
    assert module_fixture == 5

def test_things_03(module_fixture):
    assert module_fixture == 5

def test_things_04(module_fixture):
    assert module_fixture == 5

def test_things_05(module_fixture):
    assert module_fixture == 5





if __name__ == '__main__':
    pytest.main([
        __file__,
    ])
