import re
import unittest
from mock import patch
import download_espa_order as deo

class TestDownloadEspaOrder(unittest.TestCase):

    def test_get_version(self):
        ver = deo.get_version()
        self.assertTrue(re.match("[0-9]{1}.[0-9]{1,2}.[0-9]{1,2}", ver))
        
class TestHTTPSHandler(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_auth(self):
        pass
    
    def test_get(self):
        pass

    def test_download_bytes(self):
        pass

    def test_download(self):
        pass


class TestRequestsHandler(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_auth(self):
        pass

    def test_get(self):
        pass

    def test_download(self):
        pass


class TestApi(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_api_request(self):
        pass

    def test_get_completed_scenes(self):
        pass

    def test_retrieve_all_orders(self):
        pass


class TestScene(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_checksum(self):
        pass

    
class TestLocalStorage(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_directory_path(self):
        pass

    def test_scene_path(self):
        pass

    def test_is_stored(self):
        pass

    def test_store(self):
        pass


 
