## Clustering
Attributes of key: `clustering`

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
  	<td>
        <code>ConnectedComponentsClustering</code><br><code>UniqueMappingClustering</code><br><code>ExactClustering</code><br><code>CenterClustering</code><br><code>BestMatchClustering</code><br><code>MergeCenterClustering</code><br><code>CorrelationClustering</code><br><code>CutClustering</code><br><code>MarkovClustering</code><br><code>KiralyMSMApproximateClustering</code><br><code>RicochetSRClustering</code><br><code>RowColumnClustering</code>
  	</td>
  	<td><code>string</code></td>
  	<td><code>BlockingBasedWorkflow</code> <code>EmbeddingsNNWorkflow</code> <code>JoinWorkflow</code> </td>
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
        <td rowspan="1"><code>params</code></td>
        <td><code>similarity_threshold</code></td>
        <td>[0.0 - 1.0]</td>
        <td></td>
        <td rowspan="1"><code>ConnectedComponentsClustering</code><br><code>UniqueMappingClustering</code><br><code>ExactClustering</code><br><code>CenterClustering</code><br><code>BestMatchClustering</code><br><code>MergeCenterClustering</code><br><code>CorrelationClustering</code><br><code>CutClustering</code><br><code>MarkovClustering</code><br><code>KiralyMSMApproximateClustering</code><br><code>RicochetSRClustering</code><br><code>RowColumnClustering</code></td>
    </tr>
</table>