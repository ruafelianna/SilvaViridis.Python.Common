from enum import Enum
from pydantic import validate_call

from .HttpStatusGroup import HttpStatusGroup

class HttpStatus(Enum):
    Continue = 100
    SwitchingProtocols = 101
    Processing = 102
    EarlyHints = 103
    OK = 200
    Created = 201
    Accepted = 202
    NonAuthoritativeInformation = 203
    NoContent = 204
    ResetContent = 205
    PartialContent = 206
    MultiStatus = 207
    AlreadyReported = 208
    IMUsed = 226
    MultipleChoices = 300
    MovedPermanently = 301
    Found = 302
    SeeOther = 303
    NotModified = 304
    UseProxy = 305
    Reserved306 = 306
    TemporaryRedirect = 307
    PermanentRedirect = 308
    BadRequest = 400
    Unauthorized = 401
    PaymentRequired = 402
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    NotAcceptable = 406
    ProxyAuthenticationRequired = 407
    RequestTimeout = 408
    Conflict = 409
    Gone = 410
    LengthRequired = 411
    PreconditionFailed = 412
    PayloadTooLarge = 413
    URITooLong = 414
    UnsupportedMediaType = 415
    RangeNotSatisfiable = 416
    ExpectationFailed = 417
    IMATeapot = 418
    MisdirectedRequest = 421
    UnprocessableContent = 422
    Locked = 423
    FailedDependency  = 424
    TooEarly = 425
    UpgradeRequired = 426
    PreconditionRequired = 428
    TooManyRequests = 429
    RequestHeaderFieldsTooLarge = 431
    UnavailableForLegalReasons = 451
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HTTPVersionNotSupported = 505
    VariantAlsoNegotiates = 506
    InsufficientStorage = 507
    LoopDetected = 508
    NotExtended = 510
    NetworkAuthenticationRequired = 511

    @validate_call
    def get_group(
        self,
    ) -> HttpStatusGroup:
        return HttpStatusGroup(self.value // 100)

    @validate_call
    def is_information(
        self,
    ) -> bool:
        return self.get_group() == HttpStatusGroup.information

    @validate_call
    def is_success(
        self,
    ) -> bool:
        return self.get_group() == HttpStatusGroup.success

    @validate_call
    def is_redirect(
        self,
    ) -> bool:
        return self.get_group() == HttpStatusGroup.redirect

    @validate_call
    def is_client_error(
        self,
    ) -> bool:
        return self.get_group() == HttpStatusGroup.client_error

    @validate_call
    def is_server_error(
        self,
    ) -> bool:
        return self.get_group() == HttpStatusGroup.server_error
