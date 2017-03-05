import productname as pn
import pytest



def test_VariantName_instantiates():
    varname = pn.VariantName()
    assert isinstance(varname, pn.VariantName)


def test_VariantName_has_name_attribute():
    varname = pn.VariantName()
    assert hasattr(varname, 'name')

@pytest.mark.parametrize('name', ('a', 'aaa', 'aaaaaaaaaa', 1, 2))
def test_VariantName_can_init_w_name(name):
    varname = pn.VariantName(name=name)
    assert varname.name == name

@pytest.mark.parametrize('region', ('ger', 'fna'))
def test_VariantName_can_init_w_name(region):
    varname = pn.VariantName()
    varname.region = region
    assert varname.region == region

@pytest.mark.parametrize('year', (2000, 2005, 2020))
def test_year_proper_values(year):
    varname = pn.VariantName()
    varname.year = year
    assert varname.year == year

@pytest.mark.parametrize('year', (1, 1999, 2021, 2354))
def test_year_proper_values(year):
    varname = pn.VariantName()

    with pytest.raises(ValueError):
        varname.year = year



if __name__ == '__main__':
    pytest.main()