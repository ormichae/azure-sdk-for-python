# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AzureReservationAPIOperationsMixin:

    async def get_catalog(
        self,
        subscription_id: str,
        reserved_resource_type: str,
        location: Optional[str] = None,
        **kwargs
    ) -> List["_models.Catalog"]:
        """Get the regions and skus that are available for RI purchase for the specified Azure subscription.

        Get the regions and skus that are available for RI purchase for the specified Azure
        subscription.

        :param subscription_id: Id of the subscription.
        :type subscription_id: str
        :param reserved_resource_type: The type of the resource for which the skus should be provided.
        :type reserved_resource_type: str
        :param location: Filters the skus based on the location specified in this parameter. This can
         be an azure region or global.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of Catalog, or the result of cls(response)
        :rtype: list[~azure.mgmt.reservations.models.Catalog]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.Catalog"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_catalog.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        query_parameters['reservedResourceType'] = self._serialize.query("reserved_resource_type", reserved_resource_type, 'str')
        if location is not None:
            query_parameters['location'] = self._serialize.query("location", location, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[Catalog]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_catalog.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/catalogs'}  # type: ignore

    async def get_applied_reservation_list(
        self,
        subscription_id: str,
        **kwargs
    ) -> "_models.AppliedReservations":
        """Get list of applicable ``Reservation``\ s.

        Get applicable ``Reservation``\ s that are applied to this subscription or a resource group
        under this subscription.

        :param subscription_id: Id of the subscription.
        :type subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppliedReservations, or the result of cls(response)
        :rtype: ~azure.mgmt.reservations.models.AppliedReservations
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AppliedReservations"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_applied_reservation_list.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AppliedReservations', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_applied_reservation_list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/appliedReservations'}  # type: ignore