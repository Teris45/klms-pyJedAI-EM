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
	  <td><a href="./docs/block_building.md">block_building_object</a></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
  	  <td><code>block_cleaning</code></td>
	  <td>Block cleaning method and parameters used only for <code>BlockingBasedWorkflow</code> <br>More than one <code>block_cleaning</code> methods can be used 
	  <td><a href="#block-cleaning">block_cleaning_object</a> or <code>list</code> of <a href="block-cleaning">block_cleaning_object</a></td>
	  <td></td> 
  </tr>
  <tr>
    <td><code>comparison_cleaning</code></td>
	  <td>Comparison cleaning method and parameters used only for <code>BlockingBasedWorkflow</code> </td> 
	  <td><a href="#comparison-cleaning">comparison-cleaning-object</a></td>
	  <td></td> 
  </tr>
  <tr>
    <td><code>entity_matching</code></td>
	  <td>Entity Matching method and parameters used only for <code>BlockingBasedWorkflow</code> </td> 
	  <td><a href="#entity-matching">comparison-cleaning-object</a></td>
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



#### Block Cleaning
Attributes of key: `block_cleaning`

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Workflow</th>
    <th>Required</th>
  </tr>
  <tr>
	<td rowspan="1"><code>method</code></td>
  	<td><code>BlockFiltering</code><br><code>BlockPurging</code>		  		  
  	</td>
  	<td><code>string</code></td>
  	<td><code>BlockingBasedWorkflow</code></td>
	<td>&#10004;</td> 
  </tr>
</table>

Attributes of key: `params`

<table>
    <tr>
        <th>Attributes</th>
        <th>Name</th>
        <th>Value Type</th>
        <th>Default Value</th>
        <th>Method</th>
    </tr>
    <tr>
        <td rowspan="2"><code>params</code></td>
        <td><code>ratio</code></td>
        <td><code>float</code></td>
        <td>0.8</td>
        <td rowspan="1"><code>BlockFiltering</code></td>
    </tr>
    <tr>
        <td><code>smoothing_factor</code></td>
        <td><code>float</code></td>
        <td>1.025</td>
        <td rowspan="1"><code>BlockPurging</code></td>
    </tr>
</table>

#### Comparison Cleaning
Attributes of key: `comparison_cleaning`

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Workflow</th>
    <th>Required</th>
  </tr>
  <tr>
	<td rowspan="1"><code>method</code></td>
  	<td><code>WeightedEdgePruning</code>
<code>CardinalityEdgePruning</code>
<code>CardinalityNodePruning</code>
<code>ReciprocalCardinalityNodePruning</code>
<code>WeightedNodePruning</code>
<code>BLAST</code>
<code>ReciprocalWeightedNodePruning</code>
<code>ComparisonPropagation</code>		  		  
  	</td>
  	<td><code>string</code></td>
  	<td><code>BlockingBasedWorkflow</code></td>
	<td>&#10004;</td> 
  </tr>
</table>

Attributes of key: `params`

<table>
    <tr>
        <th>Attributes</th>
        <th>Name</th>
        <th>Value Type</th>
        <th>Default Value</th>
        <th>Method</th>
    </tr>
    <tr>
        <td rowspan="2"><code>params</code></td>
        <td><code>weighting_scheme</code></td>
        <td><code>CN-CBS</code><br><code>CBS</code><br><code>SN-CBS</code><br><code>CNC</code><br><code>SNC</code><br><code>SND</code><br><code>CND</code><br><code>CNJ</code><br><code>SNJ</code><br><code>COSINE</code><br><code>DICE</code><br><code>ECBS</code><br><code>JS</code><br><code>EJS</code><br><code>X2</code></td>
        <td><code>X2</code></td>
        <td rowspan="1"><code>WeightedEdgePruning</code><br><code>CardinalityEdgePruning</code><br><code>CardinalityNodePruning</code><br><code>ReciprocalCardinalityNodePruning</code><br><code>WeightedNodePruning</code><br><code>BLAST</code><br><code>ReciprocalWeightedNodePruning</code><br></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td rowspan="1"><code>ComparisonPropagation</code></td>
    </tr>
</table>


#### Entity Matching
Attributes of key: `entity_matching`

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Workflow</th>
    <th>Required</th>
  </tr>
  <tr>
	<td rowspan="1"><code>method</code></td>
  	<td><code>EntityMatching</code>  	</td>
  	<td><code>string</code></td>
  	<td><code>BlockingBasedWorkflow</code></td>
	<td>&#10004;</td> 
  </tr>
</table>

Attributes of key: `params`

<table>
    <tr>
        <th>Attributes</th>
        <th>Name</th>
        <th>Value Type</th>
        <th>Default Value</th>
        <th>Method</th>
    </tr>
    <tr>
        <td rowspan="7"><code>params</code></td>
        <td><code>metric</code></td>
        <td><code>edit_distance</code><br><code>cosine</code><br><code>jaro</code><br><code>jaccard</code><br><code>generalized_jaccard</code><br><code>dice</code><br><code>TF-IDF</code><br><code>Frequency</code><br><code>PL2</code><br><code>BM25F</code><br><code>overlap_coefficient</code><br><code>sqeuclidean</code></td>
        <td>dice</td>
        <td rowspan="7"><code>EntityMatching</code></td>
    </tr>
    <tr>
        <td><code>tokenizer</code></td>
        <td><code>char_tokenizer</code><br><code>word_tokenizer</code><br><code>white_space_tokenizer</code><br><code>qgrams</code><br><code>standard</code><br><code>standard_multiset</code><br><code>qgrams_multiset</code></td>
        <td>white_space_tokenizer</td>
    </tr>
    <tr>
        <td><code>vectorizer</code></td>
        <td><code>tfidf</code><br><code>tf</code><br><code>boolean</code></td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>qgram</code></td>
        <td><code>int</code></td>
        <td>1</td>
    </tr>
    <tr>
        <td><code>similarity_threshold</code></td>
        <td><code>float</code></td>
        <td>0.0</td>
    </tr>
    <tr>
        <td><code>tokenizer_return_unique_values</code></td>
        <td><code>bool</code></td>
        <td>False</td>
    </tr>
    <tr>
        <td><code>attributes</code></td>
        <td><code>any</code></td>
        <td>None</td>
    </tr>
</table>

#### Clustering


