## Block Cleaning
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
	<tr>
 <td><code>params</code></td>
<td>See below which parameters can be used for each method</td>
<td><code>list</code></td>
<td><code>BlockingBasedWorkflow</code></td>
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
