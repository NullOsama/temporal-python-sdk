# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: temporal/api/errordetails/v1/message.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class NotFoundFailure(betterproto.Message):
    current_cluster: str = betterproto.string_field(1)
    active_cluster: str = betterproto.string_field(2)


@dataclass
class WorkflowExecutionAlreadyStartedFailure(betterproto.Message):
    start_request_id: str = betterproto.string_field(1)
    run_id: str = betterproto.string_field(2)


@dataclass
class NamespaceNotActiveFailure(betterproto.Message):
    namespace: str = betterproto.string_field(1)
    current_cluster: str = betterproto.string_field(2)
    active_cluster: str = betterproto.string_field(3)


@dataclass
class ClientVersionNotSupportedFailure(betterproto.Message):
    client_version: str = betterproto.string_field(1)
    client_impl: str = betterproto.string_field(2)
    supported_versions: str = betterproto.string_field(3)


@dataclass
class FeatureVersionNotSupportedFailure(betterproto.Message):
    feature: str = betterproto.string_field(1)
    feature_version: str = betterproto.string_field(2)
    supported_versions: str = betterproto.string_field(3)


@dataclass
class NamespaceAlreadyExistsFailure(betterproto.Message):
    pass


@dataclass
class CancellationAlreadyRequestedFailure(betterproto.Message):
    pass


@dataclass
class QueryFailedFailure(betterproto.Message):
    pass
