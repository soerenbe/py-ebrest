from __future__ import annotations

from typing import TYPE_CHECKING

from easybill_rest.helper import Helper
from easybill_rest.resources.resource_abstract import ResourceAbstract

if TYPE_CHECKING:
    from easybill_rest import Client


class ResourceDiscountPositions(ResourceAbstract):
    _endpoint: str = "/discounts/position"
    _client: Client = None

    def __init__(self, client: Client) -> None:
        super().__init__()
        self._client = client

    def get_position_discounts(self, params: dict = None) -> dict:
        """get_position_discounts returns a dict with position discount objects"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(self._endpoint, params),
            self._client.get_basic_headers_for_json()
        )

    def get_position_discount(self, position_discount_id: str) -> dict:
        """get_position_discount returns the referenced (id) position discount"""

        return self._client.call(
            "GET",
            Helper.create_request_url_from_params(
                self._endpoint +
                "/" +
                position_discount_id),
            self._client.get_basic_headers_for_json())

    def create_position_discount(self, payload: dict) -> dict:
        """create_position_discount returns the position discount model as dict on success with the data from the passed payload"""

        return self._client.call(
            "POST",
            Helper.create_request_url_from_params(self._endpoint),
            self._client.get_basic_headers_for_json(),
            payload
        )

    def update_position_discount(
            self,
            position_discount_id: str,
            payload: dict) -> dict:
        """update_position_discount updates the reference (id) position discount with the given payload. Returns the updated position discount model"""

        return self._client.call(
            "PUT",
            Helper.create_request_url_from_params(
                self._endpoint +
                "/" +
                position_discount_id),
            self._client.get_basic_headers_for_json(),
            payload)

    def delete_position_discount(self, position_discount_id: str) -> None:
        """delete_position_discount returns None on success and raises an exception if the discount couldn't be deleted"""

        self._client.call(
            "DELETE",
            Helper.create_request_url_from_params(
                self._endpoint +
                "/" +
                position_discount_id),
            self._client.get_basic_headers())
