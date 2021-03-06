import unittest
from pprint import pprint

from config.dev_config import DEV_CONFIG
from data_load import update_data, load_players, check_market
from layout_ga import do_ga
from pixstar import Ship, ship_layout
from ps_client import PixelStarshipsApi
# from scheduled import check_market
from run import push_context


class TestPixStar(unittest.TestCase):

    TEST_USER_ID = 2444412  # Sokitume
    UM_USER_ID = 2212422  # Upper Management

    def test_device_key_gen(self):
        device_key = '32598c26ec94'
        checksum = 'a7666d700ff92a35459daa6227eb28e0'

        print(PixelStarshipsApi().create_device_key())

    def test_checksum(self):
        s = '32598c26ec94'
        checksum = 'a7666d700ff92a35459daa6227eb28e0'
        print(s, checksum, PixelStarshipsApi().md5_checksum(s))

    def test_generate_device(self):
        print(PixelStarshipsApi().generate_device())

    def test_random_layout(self):
        ship = Ship(ship_layout)
        print()
        ship.print()
        ship.place_random_rooms((3, 2))
        ship.print()
        assert True

    def test_ga_layout(self):
        do_ga()
        assert True

    def test_get_pss_access_token(self):
        psa = PixelStarshipsApi()
        print(psa.token)
        assert True

    def test_get_ship_data(self):
        psa = PixelStarshipsApi()
        id = psa.get_user_id('jy3p')
        data = psa.inspect_ship(id)
        pprint(data)
        assert True

    def test_ship_data(self):
        psa = PixelStarshipsApi()
        # ship, user, chars, rooms = psa.summarize_ship(self.TEST_USER_ID)
        ship, user, chars, rooms, items = Ship('adam').summarize()
        if ship:
            print(ship)
            # print(user)
            # print(len(chars), chars)
            # print(len(rooms), rooms)
            # print(len(items), items)
        assert True

    def test_new_token(self):
        # Force a new token
        DEV_CONFIG['DEV_MODE'] = True
        psa = PixelStarshipsApi()
        print(psa.token)
        psa.get_new_token()
        print(psa.token)
        assert True

    def test_ship_map(self):
        psa = PixelStarshipsApi()
        print(psa.ship_map)
        assert True

    def test_room_map(self):
        psa = PixelStarshipsApi()
        print(psa.room_map)
        assert True

    def test_sprite_style(self):
        psa = PixelStarshipsApi()
        print(psa.sprite_data(655))
        assert True

    def test_char_map(self):
        psa = PixelStarshipsApi()
        print(psa.char_map)
        assert True

    def test_upgrade_map(self):
        psa = PixelStarshipsApi()
        print(psa.upgrade_map)
        assert True

    def test_market_data(self):
        psa = PixelStarshipsApi()
        data = psa.get_market_data()
        print(data)
        assert True

    def test_check_market(self):
        from data_load import check_market
        check_market()
        assert True

    def test_test_prices(self):
        push_context()
        psa = PixelStarshipsApi()
        data = psa._load_prices()
        print(data)
        assert True

    def test_load_room_map(self):
        push_context()
        psa = PixelStarshipsApi()
        psa._load_room_map()
        assert True

    def test_get_user_id(self):
        push_context()
        psa = PixelStarshipsApi()
        id = psa.get_user_id('jy3p')
        print(id)
        assert True

    def test_item_prices(self):
        push_context()
        psa = PixelStarshipsApi()
        r = psa.get_item_prices(103)
        print(r)
        assert True

    def test_add_records(self):
        push_context()
        psa = PixelStarshipsApi()
        psa.update_item_data()
        assert True

    def test_read_records(self):
        push_context()
        psa = PixelStarshipsApi()
        psa._load_item_map()
        assert True

    def test_setting_service(self):
        psa = PixelStarshipsApi()
        print(psa.get_settings())

    def test_update_data(self):
        update_data()

    def test_change_data(self):
        push_context()
        psa = PixelStarshipsApi()
        for r in psa.change_data:
            print(r)

    def test_get_verification_data(self):
        push_context()
        psa = PixelStarshipsApi()
        r = psa.get_verification_data('Sokitume')
        print(r)

    def test_load_players(self):
        load_players()
        return True

    def test_check_market(self):
        check_market()
        return True

    def test_harness(self):
        from api_helpers import player_data
        push_context()
        r = player_data()
        print(r[-1])
        return True
