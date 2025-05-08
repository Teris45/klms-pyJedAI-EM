## Comparison Cleaning
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
