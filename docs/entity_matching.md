## Entity Matching
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