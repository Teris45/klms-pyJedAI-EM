## Join
Attributes of key: `join`

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
  	<td><code>EJoin</code><br><code>TopKJoin</code></td>
  	<td><code>string</code></td>
  	<td><code>JoinWorkflow</code></td>
	<td>&#10004;</td> 
  </tr>
  <tr>
    <td><code>attributes_1</code><br><code>attributes_2</code></td>
    <td>Attributes to be used for block building</td>
    <td><code>list</code></td>
    <td><code>JoinWorkflow</code></td>
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
        <td rowspan="6"><code>params</code></td>
        <td><code>metric</code></td>
        <td><code>dice</code><br><code>cosine</code><br><code>jaccard</code></td>
        <td></td>
        <td rowspan="4"><code>TopKJoin</code><br><code>EJoin</code></td>
    </tr>
    <tr>
        <td><code>tokenization</code></td>
        <td><code>qgrams</code><br><code>standard</code><br><code>standard_multiset</code><br><code>qgrams_multiset</code></td>
        <td></td>
    </tr>
    <tr>
        <td><code>qgrams</code></td>
        <td><code>int</code></td>
        <td></td>
    </tr>
    <tr>
        <td><code>reverse_order</code></td>
        <td><code>bool</code></td>
        <td>False</td>
    </tr>
    <tr>
        <td><code>K</code></td>
        <td><code>int</code></td>
        <td></td>
        <td><code>TopKJoin</code></td>
    </tr>
    <tr>
        <td><code>similarity_threshold</code></td>
        <td><code>float</code></td>
        <td>0.82</td>
        <td><code>EJoin</code></td>
    </tr>
</table>