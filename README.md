# README PyJedAI - Entity Matching

The following README will guide you through the whole process of Entity Matching using pyJedAI.

## Input
**For all key attributes in JSON, exactly one file path must be provided.**

| Attributes | Info | Value Type | Required  
| :--- | :--- | :--- | :---
`dataset_1` | `.csv` format | List | - [X]    
* `dataset_2`: `.csv` format &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; type: list &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Optional**  
> :bulb: **Tip:** If `dataset_2` is provided, matches will only be of type (e₁, e₂), where e₁ is an entity in `dataset_1` and e₂ is an entity in `dataset_2`.
* `ground_truth`: `.csv` format containing ids of matching entities &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; type: list &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Optional**  
> :bulb: **Tip:** If `ground_truth` is provided, metrics will be returned
```
{
	"inputs" :
		"dataset_1": [
            		"d5e730ba-c1d5-4ec1-ae95-88a637204c19"
        	],
        	"dataset_2": [
            		"cb37e262-a606-4d82-9712-b80e8f4d723d"
        	],
        	"ground_truth":[
            		"db006da0-16ed-4ef5-bf1e-d142488d533e"
        	]
}
```
## Parameters
* `dataset_1`: 
	*  `separator` : character separating values in each row &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Required**
	*  `id_column_name` : column containing id of dataset &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Required**
	*  `dataset_name` : name of dataset &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **optional**
   	*  `attributes` : certain attributes to be used for matching &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **optional**
Three different workflows can be executed from pyJedAI.



#### BlockingBased-Workflow
* `workflow`: `"BlockingBasedWorkflow"`

