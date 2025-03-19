# InvitationCreateRequestDataAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**expires_at** | **datetime** | UTC. Default 7 days. If this attribute is provided, it must be at least 24 hours in the future. | [optional] 
**state** | **str** | * &#x60;pending&#x60; - Invitation is pending * &#x60;accepted&#x60; - Invitation was accepted by a user * &#x60;expired&#x60; - Invitation expired after the configured time * &#x60;revoked&#x60; - Invitation was revoked by a user | [optional] 
**token** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

