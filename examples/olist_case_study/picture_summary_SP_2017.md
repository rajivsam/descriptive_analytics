
![Header](../../images/shopping_in_SP.jpg)
# The Olist Dataset: Picture Summary for the Sau Paulo Region (SP) in 2017
This page is an initial iteration demonstrating the utility of taking the time to develop a descriptive profile of your dataset prior to embarking on predictive tasks on the same dataset. This page uses a [dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) that has applications to both retail and supply chain. It has transaction data that covers multiple geographic regions and a two year period. A schema is provided. It has data quality issues, but with analysis it is possible to isolate a chunk of data that can yield insights into purchasing behavior. Most importantly, performing a descriptive analysis such as this, maps your problem into simpler canonical problems - problems that we know how to solve well. A starting point like this dataset is representative in many ways to real life modeling projects. We have some broad analysis goals and a data dump that is created from this. Refinining this to useful models and insights is the ultimate goal.

## To whom is the case study useful?
This case study is useful to:
1. Those who have a transaction dataset and want to understand how to analyze it.
2. Those who have other kinds of user-activity datasets and want to understand how to analyze them. For example, you have an user health metric (say continuous glucose monitoring) and you have a user activity dataset (say, user activity on a health app). You consolidate user, activity and metric based on the time at which a health metric was recorded. You can then analyze the user activity dataset to understand how it relates to the health metric. This is a common pattern in many domains.



### Why Sau Paulo (SP)?
![sales_by_state](../../images/pct_orders_by_state.png)
When we look at the distribution of Olist orders by state, we see that Sau Paulo (SP) accounts for a significant portion of the total orders. This makes it a key region for analysis. RJ and MG follow, but SP stands out with a substantial lead in the number of orders.

**code**:
[customer_product_segmentation.ipynb](../../notebooks/customer_product_segmentation.ipynb)

### Why 2017?
2017 is the year where we have the most complete data available. We have data for the later part of 2016 but it is missing 10 weeks of data. We have data that is continuous for 2018, but it is for part of the year only. Therefore, 2017 is the best choice for a complete analysis of customer behavior and sales trends.
![weekly revenue](../../images/weekly_rev_SP_2017.png)

**code**:
[temporal_seg_plots.ipynb](../../notebooks/temporal_seg_plots.ipynb)


### How similar were weekly orders from Olist in SP in 2017?
Cosine similarity is a metric used to quantify how similar two non-zero vectors are, based on the angle between them. In this context, each weekly order is represented as a vector, where each component corresponds to an inventory item and its value is the revenue generated from that item during the week. By calculating the cosine similarity between consecutive weekly order vectors, we can assess how similar the mix of purchased items is from week to week. High cosine similarity indicates that the same items contributed similarly to revenue across weeks, while lower values suggest more variation in purchasing patterns. The plot below shows the cosine similarity of consecutive weekly orders in SP for the year 2017. The x-axis represents the week number, and the y-axis shows the cosine similarity value. The cosine similarity values have been binned into quartiles and color coded to identify the periods of high and low similarity.

![weekly cosine similarity](../../images/cs_2017_SP_succ_weeks.png)

The cosine similarity of the succesive weekly orders in SP during 2017 was low in the first quarter. Most weeks had cosine similarity in the first quartile. It picks up in the second quarter and moves in cycles. A moving average plot best brings out the cycles.

![monthly moving average of cosine similarity between weekly orders](../../images/monthly_MA_CS.png)


**code**:
[cs_analysis_prod_purch_2017.ipynb](../../notebooks/cs_analysis_prod_purch_2017.ipynb)


### Why are we looking at weekly orders?
When we exmanined what drives revenue to the store, we found that frequent purchases of a small number of items contribute most to the revenue. 

![contribution of frequent purchases to revenue](../../images/contrib_freq_inventory_revenue.png)

**code**:
[customer_product_segmentation.ipynb](../../notebooks/customer_product_segmentation.ipynb)


### What is a frequently purchased item and what portion of the inventory is it?
A frequently purchased item is one that was purchased 10 or more times in the period for which we have data. This is a very low threshold, but as we can see, it is still a very small portion of the inventory. 

![percentage of inventory that is frequently purchased](../../images/pct_of_inventory_freq_items.png)

**code**:
[customer_product_segmentation.ipynb](../../notebooks/customer_product_segmentation.ipynb)

### Why are we not looking at frequent customers?
Because frequent customers, those who have made 5 or more purchases at the store contribute a very small portion of the revenue in contrast to frequently purchased items.
![contribution of frequent customers to revenue](../../images/contribution_freq_cust_revenue.png)

This does not mean that frequent customers are not important, just that since frequent items are a much larger portion of the revenue, we will focus on them for this analysis.

### Can you summarize the weekly orders in SP in 2017 into smaller segments?
Yes, clustering the cosine similarity graph of the weekly orders in SP gives us that.

![cosine similarity graph clustered](../../images/cs_2017_temporal_clusters_weekly_rev.png)


The weekly revenue for the clusters is shown in the violin plot below. 
![violin plot of weekly revenue for clusters](../../images/cs_violin_plot_2017.png)

**code**:
[cs_analysis_prod_purch_2017.ipynb](../../notebooks/cs_analysis_prod_purch_2017.ipynb)


### Ok, how about summarizing the frequent items ordered, there are nearly 3k inventory items that are ordered frequently. Can these be summarized?

We achieve this by applying Non-negative Matrix Factorization (NMF) to the weekly orders in SP. NMF is a dimensionality reduction technique that summarizes high-dimensional data into a smaller set of interpretable components. In this case, the weekly orders can be effectively represented by just two distinct components, each characterized by a unique set of inventory items. For a clear explanation of the separable NMF concept, see [this talk](https://www.youtube.com/watch?v=O8YDAMjIzYs&t=1443s); for a deeper dive, refer to [Ankur Moitra's talk](https://www.youtube.com/watch?v=kSfwY68gQ9I&t=1647s). In matrix factorization, these defining items are known as "anchor items." Remarkably, these two components capture 90% of the variance in weekly orders for SP. The first component contains 34 unique inventory items, while the second has 104. Item descriptions are in Portuguese. Below is a sample of items from each component. Note these are item descriptions/categories. Two different inventory items can have the same descriptions. A set difference is used to determine the items in each component that are not in the other component. Please refer to the implementation.


<img src="../../images/nmf_cs_comp1.png" width="425"/>  <img src="../../images/nmf_cs_comp2.png" width="425"/> 


Now each week can be succintly described by just two components (instead of nearly 3 K components). In fact, the NMF solution gives us clear clusters of purchasing tendencies. We have a large cluster, which corresponds to a long temporal period where there are purchases of inventory items belonging to both components. Two small cluster/temporal periods where we have purchases belonging to component 1 and a small cluster/temporal period where we have purchases belonging to component 2.

![Temporal Patterns in Purchases, 2017](../../images/temporal_patterns_purchases.png)


**code**
[sep_nmf_cs_temp_2017_purch_data.ipynb](../../notebooks/sep_nmf_cs_temp_2017_purch_data.ipynb)


### What is similar when you are looking at frequently purchased items using cosine similarity?
Well, this is an analysis choice. It is a choice using which you can pivot your analysis into different sub-problems. For example if you decide that items with lessn than 10 percent cosine similarity are not similar, then this threshold will connect items that are similar and disconnect items that are not similar. 

In the temporal segmentation of weekly inventory items, we connect two weeks if their cosine similarity is greater than 0.1. This threshold requires analysis and tuning. Alternatively, you can pick a set of nearest neighbors for each point in your dataset. So this will segment your similarity graph into connected components. The connected components will be the weeks that are similar to each other. An example of this is illustated in the geographical segmentation of the weekly inventory items. The idea can be extended to temporal view also. Each connected component will be a sub-problem that can be analyzed separately. You typically want to analyze some signal on the sub-graphs, such as the number of orders, the revenue, or the number of unique items ordered. 

**code**:
1. [knn_graph_prep.ipynb](../../notebooks/knn_graph_prep.ipynb)

2. [geo_cs_analysis_prod_purch_2017.ipynb](../../notebooks/geo_cs_analysis_prod_purch_2017.ipynb)

### How was the ordering behavior in SP across different cities in the year 2017?
Just a quick description of the way this segmentation was done. In contrast to aggregating the weekly orders, we are looking at the orders in each city in SP. On a side note, this aggregation of a raw transaction dataset with respect to a small number of attributes is a common pattern in data analysis. 

The similarity graph for weekly orders computes the similarity of ordering behavior across different weeks of the year 2017. In contrast, the similarity graph for cities computes the similarity of ordering behavior across different cities in SP. 

In addition, the thresholding idea discussed above is applied to the similarity graph for cities. The threshold is set to 0.4. We connect two cities in the similarity graph if their cosine similarity is greater than 0.4. The connected components of the graph are the cities that are similar to each other in terms of ordering behavior. _The non singleton connected components are also subsets of the dataset where the IID assumption is not reasonable . The singleton connected components can be analyzed and modeled in isolation from the other data points, i.e, the IID assumption is reasonable for these points. The singleton compnents are those points, weeks or cities, depending on what aggregation you are analyzing, that are not connected to any other point. Knowing what cannot be treated as IID and what can be is a very useful finding. You have partitioned the original dataset into a part where the IID assumption cannot be made and a part where it can be made._. Each connected component can be analyzed according to the problem you are investigating, for example it could be a signal of some kind on a graph, revenue for example. It could be a discrete property, is the city a high sales volume city? You may be interested in clustering within a connected component. [Ulkrike von Luxborg's tutorial on Spectral Clustering](https://people.csail.mit.edu/dsontag/courses/ml14/notes/Luxburg07_tutorial_spectral_clustering.pdf) is a very popular resource. It is also an excellent resource. As discussed in the tutorial, you can generate the similarity graph by picking a fixed number of neighbors for each node instead of applying a threshold. This is another variation of parametrizing the size of the similarity graph.

Using a threshold of 0.4 for connecting two nodes of the similarity graph of the cities in Sau Paulo, we have 56 connected components. The largest one has 26 edges. The number of subgraphs in the connected components and thier respective sizes are shown in the table below. There were a total 476 cities in SP in 2017 where Olist had business transactions of frequently purchased items. It looks like 15-20 cities are assoicated data errors. Of nearly 460 cities, about 170 cities are in connected components of size 2 or more. The remaining cities are singleton connected components, i.e., they are not connected to any other city in the similarity graph. These are may be treated as IID data points. For a moment, consider one of the duties of a geographic manager, to monitor the cities in his/her region. Further grouping of the cities in both the connected components and the IID components is needed. This can done with graph theoretic methods for the connected components and with conventional statistical methods for the IID components.
![Subgraph Summary, threshold=0.4](../../images/subgraph_summ_geo_sim_graph.png)

A subgraph of size 26 is shown below

![subgraph of size 26](../../images/size_26_sub_graph_SP_cities.png)

In the following cities, the purchase behavior may be treated as IID.
![IID purchase behavior in SP](../../images/purch_behavior_SP_IID.png)


In the following cities the purchase behavior is connected and should be treated as a graph.
![Connected purchase behavior in SP](../../images/purch_behavior_SP_connected.png)

Cities shown with same color belong to the same connected component. 


**code**:

1. [geo_cs_analysis_prod_purch_2017.ipynb](../../notebooks/geo_cs_analysis_prod_purch_2017.ipynb)
2. [geo_data_analysis_IID.ipynb](../../notebooks/geo_data_analysis_IID.ipynb)
3. [geo_datat_analysis_connected.ipynb](../../notebooks/geo_data_analysis_connected.ipynb)


**NOTE**: Visualization of the geographic segmentation is quite elaborate and will be posted as an addendum shortly. The above points should make it evident that there are clear geographic patterns. Graphs can be used to analyze the geographic segments that have similar purchases. Some canonical graph problems of interest are:
1. Identify the k-cliques within a graph. This is interesting because it identifies subgroups of similar taste/habbits.
2. Identify centrality measures in a graph. This is interesting to a manager responsible for a geographic region because it identifies the cities that he/she should be monitoring closely.


Conventional ML methods can be used to study the segments where the IID assumption is reasonable. 


### Are we done with analyzing the Olist dataset?
No, to get the full picture, you need to repeat the analysis for:
1. RJ
2. MG
3. A combined set of all other states, because after the top 3 states, the data is very thinly spread across the other states. It makes more sense to just bucket these together.

The analysis should be similar to what was done for SP. To get the full picture, we combine the results from these analyses. For student's who want to develop skills in data science, this should be a good exercise. There is an existing template, you just need to repeat the steps for the new geographic regions.


### Concluding thoughts

 We analyzed the revenue for 2017 based on a temporal aggregation and geographical aggregation. We used the Cosine similarity to identify similar purchasing behavior. This segmented the major market into two sub-problems. One problem can be analyzed with Graph methods, the other, the IID data, can be analyzed with conventional machine learning methods. A descriptive analysis task simplified our analysis for us. Hopefully, this convinces you that, performing a descriptive analytics task like the above on this dataset is useful because it gives you information about how your problem is structured.



