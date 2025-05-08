# README PyJedAI - Entity Matching

The following README will guide you through the whole process of Entity Matching using pyJedAI.

## Input
**For all key attributes in JSON, exactly one file path must be provided.**

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Required</th>
  </tr>
  <tr>
    <td><code>dataset_1</code></td>
    <td><code>.csv</code> format</td>
    <td><code>list</code></td>
    <td>&#10004;</td>
  </tr>
  <tr>
    <td><code>dataset_2</code></td>
    <td><code>.csv</code> format</td>
    <td><code>list</code></td>
    <td></td>
  </tr>
  <tr>
    <td><code>ground_truth</code></td>
    <td><code>.csv</code> format</td>
    <td><code>list</code></td>
    <td></td>
  </tr>
  <tr>
    <td><code>embeddings_dataset_1</code></td>
    <td>Used for loading embeddings in <code>EmbeddingsNNWorkflow</code><br><code>.npy</code> format</td>
    <td><code>list</code></td>
    <td></td>
  </tr>
  <tr>
    <td><code>embeddings_dataset_2</code></td>
    <td>Used for loading embeddings in <code>EmbeddingsNNWorkflow</code><br><code>.npy</code> format</td>
    <td><code>list</code></td>
    <td></td>
  </tr>
</table>

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
>  &#x1F4A1; **Tip:** If `dataset_2` is provided, matches will only be of type (e_1, e_2), where e_1 is an entity in `dataset_1` and e_2 is an entity in `dataset_2`.

>  &#x1F4A1; **Tip:** If `ground_truth` is provided, metrics will be returned
## Parameters
Concering input, additional info must be provided.

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Required</th>
  </tr>
  <tr>
	  <td><code>dataset_1</code></td>
	  <td>Provide info for dataset to be processed correctly</td>
	  <td><a href="#dataset">dataset_object</a></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
	  <td><code>dataset_2</code></td>
	  <td>Provide info for dataset to be processed correctly</td>
	  <td><a href="#dataset">dataset_object</a></td>
	  <td></td> 
  </tr>
  <tr>
	  <td><code>ground_truth</code></td>
	  <td>Provide info for dataset to be processed correctly</td>
	  <td><a href="#ground-truth">ground_truth_object</a></td>
	  <td></td> 
  </tr>
  <tr>
  	  <td><code>workflow</code></td>
	  <td>Select your preferred workflow:  
  		<code>BlockingBasedWorkflow</code>,  
  		<code>EmbeddingsNNWorkflow</code>, or  
  		<code>JoinWorkflow</code>  
	  <td><code>string</code></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
  	  <td><code>block_building</code></td>
	  <td>Block building method and parameters used only for <code>BlockingBasedWorkflow</code>, <code>EmbeddingsNNWorkflow</code> 
	  <td><a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/block_building.md">block_building_object</a></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
  	  <td><code>block_cleaning</code></td>
	  <td>Block cleaning method and parameters used only for <code>BlockingBasedWorkflow</code> <br>More than one <code>block_cleaning</code> methods can be used 
	  <td><a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/block_cleaning.md">block_cleaning_object</a> or <code>list</code> of <a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/block_cleaning.md">block_cleaning_object</a></td>
	  <td></td> 
  </tr>
  <tr>
    <td><code>comparison_cleaning</code></td>
	  <td>Comparison cleaning method and parameters used only for <code>BlockingBasedWorkflow</code> </td> 
	  <td><a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/comparison_cleaning.md">comparison-cleaning-object</a></td>
	  <td></td> 
  </tr>
  <tr>
    <td><code>entity_matching</code></td>
	  <td>Entity Matching method and parameters used only for <code>BlockingBasedWorkflow</code> </td> 
	  <td><a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/entity_matching.md">entity-matching-object</a></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
    <td><code>clustering</code></td>
	  <td>Clustering method and parameters used only for <code>BlockingBasedWorkflow</code>, <code>EmbeddingsNNWorkflow</code> or <code>JoinWorkflow</code> </td> 
	  <td><a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/clustering.md">clustering-object</a></td>
	  <td></td> 
  </tr>
  <tr>
    <td><code>join</code></td>
	  <td>Join method and parameters used only for <code>JoinWorkflow</code> </td> 
	  <td><a href="https://github.com/Teris45/pyjedai2klms/blob/main/docs/join.md">join-object</a></td>
	  <td>&#10004;</td> 
  </tr>
		
		
</table>

>  &#x1F4A1; **Tip:** `JoinWorkflow` does not contain `block_building` step.


#### Dataset
Attributes of keys: `dataset_1`, `dataset_2`
<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Required</th>
  </tr>
  <tr>
	  <td><code>separator</code></td>
	  <td>Character separating values in csv</td>
	  <td><code>char</code></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
	  <td><code>id_column_name</code></td>
	  <td>Name of Dataset's id column</td>
	  <td><code>string</code></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
	  <td><code>dataset_name</code></td>
	  <td>Name of Dataset</td>
	  <td><code>string</code></td>
	  <td></td> 
  </tr>
  <tr>
	  <td><code>attributes</code></td>
	  <td>Columns to be used for matching</td>
	  <td><code>list</code></td>
	  <td></td> 
  </tr>
</table>

#### Ground Truth
Attributes of key: `ground_truth`
<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Required</th>
  </tr>
  <tr>
	  <td><code>separator</code></td>
	  <td>Character separating values in csv</td>
	  <td><code>char</code></td>
	  <td>&#10004;</td> 
  </tr>
</table>

> Input Examples
>
```
"parameters" : {
        "dataset_1" : {
            "separator" : "|",
            "id_column_name" : "id",
            "dataset_name" : "abt"                    
        },
        "dataset_2" : {
            "separator" : "|", 
            "id_column_name" : "id",
            "dataset_name" : "buy"
        },
        "ground_truth" : {
            "separator" : "|"
        },                
        "workflow": "BlockingBasedWorkflow",
        "block_building": {
              "method": "StandardBlocking",
              "attributes_1" : ["name"],
              "attributes_2" : ["first_name"]
        },
        "block_cleaning" : [
            {
                "method" : "BlockFiltering", 
                "params" : { "ratio" : 0.7 }
            }
        ],
        "comparison_cleaning": {
            "method": "BLAST"
        },
        "entity_matching" : { 
            "method" : "EntityMatching",
            "params" : {
                "similarity_threshold" : 0.8
            }
        },
        "clustering" : {
            "method" : "UniqueMappingClustering",
            "params" : {
                "similarity_threshold" : 0.1
            }
        }
}

```
```
"parameters" : {           
        "workflow": "EmbeddingsNNWorkflow",
        "block_building": 
        {
            "method" : "EmbeddingsNNBlockBuilding",
            "params" : {
                "vectorizer" : "st5"
            }
        },
        "clustering": {
            "method" : "UniqueMappingClustering",
            "params" : {
                "similarity_threshold": 0.4
            }
        }
     ....     
    }    
```   
```
"parameters" : {           
        "workflow": "JoinWorkflow",
        "block_building": 
        {
            "method" : "TopKJoin",
            "params" : {
                "metrics" : "cosine",
                "tokenization": "qgrams",
                "reverse_order": "False"
            },
            "attributes_1": ["name"],
            "attributes_2" : ["name"]
        },
        "clustering": {
            "method" : "UniqueMappingClustering",
            "params" : {
                "similarity_threshold": 0.4
            }
        }
     ....     
    }    
```   


## Output
**For all key attributes in JSON, exactly one file path must be provided.**

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Required</th>
  </tr>
  <tr>
    <td><code>metrics</code></td>
    <td>Creates a file with F1, Recall, Precision metrics if ground truth exists<br><code>.csv</code> format</td>
    <td><code>path</code></td>
    <td></td>
  </tr>
  <tr>
    <td><code>pairs</code></td>
    <td>Creates a file with the ids of pairs<br><code>.csv</code> format</td>
    <td><code>path</code></td>
    <td></td>
  </tr>
  <tr>
    <td><code>entities</code></td>
    <td>Creates a file with all the matched entities<code>.csv</code> format</td>
    <td><code>list</code></td>
    <td></td>
  </tr>
</table>

```
{
  "outputs": {
        "metrics" : "s3://klms-bucket/pyjedai-output/metrics.csv",
        "pairs" : "s3://klms-bucket/pyjedai-output/pairs.csv",
        "entities" : "s3://klms-bucket/pyjedai-output/entities_df.csv"
  }
}

```
