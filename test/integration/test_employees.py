import logging

import pytest

logger = logging.getLogger(__name__)


def test_get(nc):
    data = nc.employees.get_all()
    logger.debug('data = %s', data)
    assert data, 'get all didnt work'

    internal_id = data[0]['internalId']
    data = nc.employees.get(internalId=internal_id)
    logger.debug('data = %s', data)
    assert data, f'No object with internalId {internal_id}'


def test_get_all_generator(nc):
    res1 = nc.employees.get_all()
    res2 = []
    for r in nc.employees.get_all_generator(page_size=200):
        res2.append(r)
    assert len(res1) == len(res2), 'changing page size is returning different results'


def test_post(nc):
    data = {}
    with pytest.raises(NotImplementedError) as ex:
        nc.employees.post(data)
