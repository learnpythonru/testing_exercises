import pytest

# ВОПРОС: то есть в этом тесте можно было обойтись совсем-совсем без фикстур?
# Они получились очень мелкими и многочисленными

@pytest.fixture()
def host_name_1():
    return "host_name_8"

@pytest.fixture()
def host_name_2():
    return "str"

@pytest.fixture()
def relative_url():
    return "relative_url"


@pytest.fixture()
def get_params_mappings_k_and_v():
    return  {'k': 'k_str', 'v': 'v_str'}

@pytest.fixture()
def querypart_k_and_v(get_params_mappings_k_and_v):
    return '?' + '&'.join([f'{k}={v}' for (k, v) in get_params_mappings_k_and_v.items()])

@pytest.fixture()
def url_k_and_v(host_name_2, relative_url, querypart_k_and_v):
    return f'{host_name_2}/{relative_url}{querypart_k_and_v}'

@pytest.fixture()
def get_params_mappings_k():
    return  {'k': 'k_str'}

@pytest.fixture()
def querypart_k(get_params_mappings_k):
    return '?' + '&'.join([f'{k}={v}' for (k, v) in get_params_mappings_k.items()])

@pytest.fixture()
def url_k(host_name_1, relative_url, querypart_k):
    return f'{host_name_1}/{relative_url}{querypart_k}'


@pytest.fixture()
def get_params_no_querypart():
    return  {}


@pytest.fixture()
def get_params_none():
    return  None


@pytest.fixture()
def get_params_attr_error():
    return [1,1]

@pytest.fixture()
def querypart_no_querypart(get_params_no_querypart):
    return ''

@pytest.fixture()
def url_no_querypart(host_name_1, relative_url, querypart_no_querypart):
    return f'{host_name_1}/{relative_url}{querypart_no_querypart}'

