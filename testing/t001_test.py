import pytest
import time


@pytest.fixture(scope="module")
def module_fixture():
    print('\n:: module_fixture')
    return 5




class TestClass_TestStuff:
    @pytest.fixture(scope="class")
    def class_fixture(self):
        print('\n::: class_fixture')
        return 6

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
        '-s',
    ])
