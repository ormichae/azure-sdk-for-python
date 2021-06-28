# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MetricsOperations:
    """MetricsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~monitor_query_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def list(
        self,
        resource_uri: str,
        timespan: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        metricnames: Optional[str] = None,
        aggregation: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        filter: Optional[str] = None,
        result_type: Optional[Union[str, "_models.ResultType"]] = None,
        metricnamespace: Optional[str] = None,
        **kwargs
    ) -> "_models.Response":
        """**Lists the metric values for a resource**.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param timespan: The timespan of the query. It is a string with the following format
         'startDateTime_ISO/endDateTime_ISO'.
        :type timespan: str
        :param interval: The interval (i.e. timegrain) of the query.
        :type interval: ~datetime.timedelta
        :param metricnames: The names of the metrics (comma separated) to retrieve. Special case: If a
         metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be
         **'Metric%2Name1'**.
        :type metricnames: str
        :param aggregation: The list of aggregation types (comma separated) to retrieve.
        :type aggregation: str
        :param top: The maximum number of records to retrieve.
         Valid only if $filter is specified.
         Defaults to 10.
        :type top: int
        :param orderby: The aggregation to use for sorting results and the direction of the sort.
         Only one order can be specified.
         Examples: sum asc.
        :type orderby: str
        :param filter: The **$filter** is used to reduce the set of metric data returned. Example:
         Metric contains metadata A, B and C. - Return all time series of C where A = a1 and B = b1 or
         b2 **$filter=A eq 'a1' and B eq 'b1' or B eq 'b2' and C eq '*'** - Invalid variant: **$filter=A
         eq 'a1' and B eq 'b1' and C eq '*' or B = 'b2'** This is invalid because the logical or
         operator cannot separate two different metadata names. - Return all time series where A = a1, B
         = b1 and C = c1: **$filter=A eq 'a1' and B eq 'b1' and C eq 'c1'** - Return all time series
         where A = a1 **$filter=A eq 'a1' and B eq '\ *' and C eq '*\ '**. Special case: When dimension
         name or dimension value uses round brackets. Eg: When dimension name is **dim (test) 1**
         Instead of using $filter= "dim (test) 1 eq '\ *' " use **$filter= "dim %2528test%2529 1 eq '*\
         ' "\ ** When dimension name is **\ dim (test) 3\ ** and dimension value is **\ dim3 (test) val\
         ** Instead of using $filter= "dim (test) 3 eq 'dim3 (test) val' " use **\ $filter= "dim
         %2528test%2529 3 eq 'dim3 %2528test%2529 val' "**.
        :type filter: str
        :param result_type: Reduces the set of data collected. The syntax allowed depends on the
         operation. See the operation's description for details.
        :type result_type: str or ~monitor_query_client.models.ResultType
        :param metricnamespace: Metric namespace to query metric definitions for.
        :type metricnamespace: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Response, or the result of cls(response)
        :rtype: ~monitor_query_client.models.Response
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Response"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-01-01"
        accept = "application/json"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if timespan is not None:
            query_parameters['timespan'] = self._serialize.query("timespan", timespan, 'str')
        if interval is not None:
            query_parameters['interval'] = self._serialize.query("interval", interval, 'duration')
        if metricnames is not None:
            query_parameters['metricnames'] = self._serialize.query("metricnames", metricnames, 'str')
        if aggregation is not None:
            query_parameters['aggregation'] = self._serialize.query("aggregation", aggregation, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query("top", top, 'int')
        if orderby is not None:
            query_parameters['orderby'] = self._serialize.query("orderby", orderby, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if result_type is not None:
            query_parameters['resultType'] = self._serialize.query("result_type", result_type, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if metricnamespace is not None:
            query_parameters['metricnamespace'] = self._serialize.query("metricnamespace", metricnamespace, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseAutoGenerated, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Response', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/{resourceUri}/providers/Microsoft.Insights/metrics'}  # type: ignore
