# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._container_registry_client import ContainerRegistryClient
from ._container_repository_client import ContainerRepositoryClient
from ._models import (
    DeleteRepositoryResult,
    ContentProperties,
    RegistryArtifactOrderBy,
    RegistryArtifactProperties,
    RepositoryProperties,
    TagOrderBy,
    ArtifactTagProperties,
)
from ._version import VERSION

__version__ = VERSION

__all__ = [
    "ContainerRegistryClient",
    "ContainerRepositoryClient",
    "DeleteRepositoryResult",
    "ContentProperties",
    "RegistryArtifactOrderBy",
    "RegistryArtifactProperties",
    "RepositoryProperties",
    "TagOrderBy",
    "ArtifactTagProperties",
]
