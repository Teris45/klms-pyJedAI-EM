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
	  <td><a href="#Dataset">dataset_object</a></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
	  <td><code>dataset_2</code></td>
	  <td>Provide info for dataset to be processed correctly</td>
	  <td><a href="#Dataset">dataset_object</a></td>
	  <td></td> 
  </tr>
  <tr>
	  <td><code>ground_truth</code></td>
	  <td>Provide info for dataset to be processed correctly</td>
	  <td><a href="#Ground Truth">ground_truth_object</a></td>
	  <td></td> 
  </tr>
  <tr>
  	  <td><code>workflow</code></td>
	  <td><code>BlockingBasedWorkflow</code> \ <code>EmbeddingsNNWorkFlow</code> \ <code>JoinWorkflow</code></td>
	  <td><a href="#Workflow">workflow_object</a></td>
	  <td>&#10004;</td> 
  </tr>
</table>

#### Dataset
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


Three different workflows can be executed from pyJedAI.



#### BlockingBased-Workflow
* `workflow`: `"BlockingBasedWorkflow"`

