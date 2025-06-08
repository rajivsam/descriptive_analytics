## Summary of the Approach to Revenue Analysis

The analysis of the Olist case study was conducted as follows:
1. Understand what drives revenue to the store:
   1. Customer affinity 
   2. Popularity of products.
   3. Geographic distribution of customers.
   4. Temporal Patterns


2. Since purchase of frequent inventory items is what drives revenue to the store, the following analysis is relevant
   1. How are weekly purchases of inventory item different from week to week
   2. How do we capture the similarity of purchase behavior
   3. Can we summarize the weekly purchases succintly?
   4. Can we segment the weekly purchase behavior into a small number of segments
   
3. Geography is a significant factor in revenue for Olist. Sau Paulo is the biggest market for Olist. Initially the analysis will be restricted to Sau Paulo, but the same analysis can be repeated for MG and RJ, which are the other major geographical markets for Olist. The following questions are relevant 
   1. Which cities in Sau Paulo have similar shopping behavior
   2. How would you summarize geographical patterns of this behavior

4. Pattern of analysis: Both the above analysis had the following recipe. We had a transaction dataset. We aggregated this data in the following ways:
   1. Temporally: We computed weekly sales of frequent inventory items
   2. Geographically/Spatially: We computed the sales of frequent inventory items in each of the cities in Sau Paulo.
Once the aggregation is done, we are in a position to compute a similarity graph between the rows of the dataset. We can then apply a threshold metric on similarity. Rows that have a similarity value above this threshold are deemed connected in the similarity graph. We can then connected components on the similarity graph to determine the sub-problems of the original problem. There is usually a property or signal on the sub-graph that we want to analyze. 

5. Instead of using a threshold, can we leverage ideas like sub-modularity or convexity, on the similarity graph to simplify our original graph into smaller graphs/components. This is an idea to investigate.


