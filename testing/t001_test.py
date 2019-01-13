import pytest
import time


@pytest.fixture(scope="module")
def results():
    print('\n:: results')
    return 5




class TestClass_TestStuff:
    @pytest.fixture(scope="class")
    def runonce(self):
        print('\n::: runonce')
        return 6

    def test_cls_01(self, runonce):
        assert runonce == 6

    def test_cls_02(self, runonce):
        assert runonce == 6

    def test_cls_03(self, runonce):
        assert runonce == 6

    def test_cls_04(self, runonce):
        assert runonce == 6






def test_things_01(results):
    assert results == 5

def test_things_02(results):
    assert results == 5

def test_things_03(results):
    assert results == 5

def test_things_04(results):
    assert results == 5

def test_things_05(results):
    assert results == 5





if __name__ == '__main__':
    pytest.main([
        __file__,
        # '-s',
    ])
