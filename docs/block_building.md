## Block Building

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
