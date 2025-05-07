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
	  <td><a href="block-building">block_building_object</a></td>
	  <td>&#10004;</td> 
  </tr>
  <tr>
  	  <td><code>block_cleaning</code></td>
	  <td>Block cleaning method and parameters used only for <code>BlockingBasedWorkflow</code> <br>More than one <code>block_cleaning</code> methods can be used 
	  <td><a href="block-cleaning">block_cleaning_object</a> or <code>list</code> of <a href="block-cleaning">block_cleaning_object</a></td>
	  <td></td> 
  </tr>
  <tr>
    <td><code>comparison_cleaning</code></td>
	  <td>Comparison cleaning method and parameters used only for <code>BlockingBasedWorkflow</code> </td> 
	  <td><a href="comparison-cleaning">comparison-cleaning-object</a></td>
	  <td></td> 
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


#### Block Building
Attributes of key: `block_building`

<table>
  <tr>
    <th>Attributes</th>
    <th>Info</th>
    <th>Value Type</th>
    <th>Workflow</th>
    <th>Required</th>
  </tr>
  <tr>
	<td rowspan="2"><code>method</code></td>
  	<td><code>StandardBlocking</code>
		<code>QGramsBlocking</code>		  
		<code>SuffixArraysBlocking</code>
		<code>ExtendedSuffixArraysBlocking</code>
		<code>ExtendedQGramsBlocking</code>		  
  	</td>
  	<td><code>string</code></td>
  	<td><code>BlockingBasedWorkflow</code></td>
	<td>&#10004;</td> 
  </tr>
  <tr>
  	<td><code>EmbeddingsNNBlockBuilding</code>
  	</td>
  	<td><code>string</code></td>
  	<td><code>EmbeddingsNNWorkflow</code></td>
	<td>&#10004;</td> 
  </tr>
<tr>
 <td><code>attributes_1</code><br><code>attributes_2</code></td>
<td>Attributes to be used for block building</td>
<td><code>list</code></td>
<td><code>BlockingBasedWorkflow</code><code>EmbeddingsNNWorkflow</code></td>
	<td></td> 
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
        <td rowspan="21"><code>params</code></td>
        <td></td>
        <td></td>
        <td></td>
        <td><code>StandardBlocking</code></td>
    </tr>
   <tr>
        <td><code>qgrams</code></td>
        <td><code>int</code></td>
        <td>6</td>
        <td rowspan="1"><code>QGramsBlocking</code></td>
    </tr>
    <tr>
        <td><code>suffix_length</code></td>
        <td><code>int</code></td>
        <td>6</td>
        <td rowspan="2"><code>SuffixArraysBlocking</code></td>
    </tr>
    <tr>
        <td><code>max_block_size</code></td>
        <td><code>int</code></td>
        <td>53</td>
    </tr>
    <tr>
        <td><code>suffix_length</code></td>
        <td><code>int</code></td>
        <td>6</td>
        <td rowspan="2"><code>ExtendedSuffixArraysBlocking</code></td>
    </tr>
    <tr>
        <td><code>max_block_size</code></td>
        <td><code>int</code></td>
        <td>39</td>
    </tr>
    <tr>
        <td><code>qgrams</code></td>
        <td><code>int</code></td>
        <td>6</td>
        <td rowspan="2"><code>ExtendedQGramsBlocking</code></td>
    </tr>
    <tr>
        <td><code>threshold</code></td>
        <td><code>float</code></td>
        <td>0.95</td>
    </tr>
     <tr>
        <td><code>vectorizer</code></td>
        <td><code>['word2vec', 'fasttext', 'doc2vec', 'glove', 'bert', 'distilbert', 'roberta', 'xlnet', 'albert', 'smpnet', 'st5', 'sent_glove', 'sdistilroberta', 'sminilm']</code></td>
        <td><code>smpnet</code></td>
        <td rowspan="9"><code>EmbeddingsNNBlockBuilding</code></td>
    </tr>
    <tr>
        <td><code>vector_size</code></td>
        <td><code>int</code></td>
        <td>300</td>
    </tr>
    <tr>
        <td><code>num_of_clusters</code></td>
        <td><code>int</code></td>
        <td>5</td>
    </tr>
    <tr>
        <td><code>top_k</code></td>
        <td><code>int</code></td>
        <td>30</td>
    </tr>
    <tr>
        <td><code>max_word_embeddings_size</code></td>
        <td><code>int</code></td>
        <td>256</td>
    </tr>
    <tr>
        <td><code>attributes_1</code></td>
        <td><code>list</code></td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>attributes_2</code></td>
        <td><code>list</code></td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>similarity_distance</code></td>
        <td><code>['cosine', 'cosine_without_normalization', 'euclidean']</code></td>
        <td><code>cosine</code></td>
    </tr>
    <tr>
        <td><code>input_cleaned_blocks</code></td>
        <td><code>list</code></td>
        <td>None</td>
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


