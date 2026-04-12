![Header Image](https://github.com/rajivsam/descriptive_analytics/blob/main/images/desc_analytics_infographic.png)
# 📊 Descriptive Analytics Recipes

Welcome to the **Descriptive Analytics Recipes** repository!  
---
## What is Descriptive Analytics?
Descriptive analytics summarizes historical business data to answer the question: “What happened?” It uses aggregates, visualizations, segmentation and explanatory models to reveal patterns in past behavior — for example, customer purchase paths in an e‑commerce store or repayment patterns in a loan portfolio.

Why it matters
- Provides the foundation for predictive and prescriptive analytics by turning raw history into structured insights.
- Informs model design and feature engineering (explanatory models often feed predictive models).
- Reduces risk by highlighting past failures and opportunities before they are repeated.

Approaches and focus
- Determine the type of analysis your use case needs, is it cross-sectional, longitudinal or panel? The analysis approach and methods follow from which of these types of dataset your use case fits. For longitudinal analysis,see [tseda](https://github.com/rajivsam/tseda) — a package designed specifically for this use case. It provides tools for exploring and summarizing patterns in a single time series variable. For an overview of the package and what it offers, see the [tseda announcement blog post](https://rajivsam.github.io/r2ds-blog/posts/tseda%20announcement/). Examples and full details are available in the [tseda GitHub repository](https://github.com/rajivsam/tseda).

- Graph-based analysis can be a very powerful tool for descriptive analytics. Traditional machine learning approaches work can be sufficient for _Independent Identically Distributed_ data, when this is not a reasonable assumption, you need analysis methods that account for the dependencies in the data. Graph based analysis do this naturally. A lot of enterprise data reside in relational databases. A common first bottleneck in using graphs for descriptive analytics is related to getting the data from native relational format to a graph analysis model. For this reason, there is a complete section of this repository dedicated to transforming relational data to graphs. Please see [this video](https://www.youtube.com/watch?v=d997pgkwtGY&list=PL-lbroKJyNLDJ44l60GvHgcYtFh0pNFek&index=4&t=215s) for a summary of this process.


For an overview video, please see [this video](https://www.youtube.com/watch?v=MwXKC_oloH8). For some samples, please see [this playlist](https://www.youtube.com/playlist?list=PL-lbroKJyNLDJ44l60GvHgcYtFh0pNFek) 

## What kind of use cases does this repository cover?
This repository covers operational or analytical datasets that are relational. In particular, _Large Language Models_ are not part of any solution here. Solutions developed here utilize machine learning methods that have served the _knowledge discovery in databases_ for a long time. The following are common use cases for descriptive analytics:
1. Traffic and Engagement Analysis: Analyzing website traffic data to understand user behavior, popular pages, and engagement metrics.
2. Sales and Revenue Analysis: Summarizing sales data to identify top-selling products, seasonal trends, and revenue patterns.
3. Customer Segmentation: Grouping customers based on purchasing behavior, demographics, or engagement levels.
4. Financial Reporting: Creating summaries of financial data, such as profit and loss statements, balance
5. Inventory Management: Analyzing inventory levels, turnover rates, and stock movement patterns.
6. Social Media Analytics: Summarizing social media interactions, follower growth, and content performance

Explanatory models are commonly used for:
1. Customer Churn Analysis: Identifying factors that contribute to customer attrition.
2. Fraud Detection: Analyzing transaction patterns to identify unusual behavior indicative of fraud.
3. Incident Analysis: Understanding the root causes of operational incidents or failures.
4. Product Performance Analysis: Evaluating product features and their impact on sales or user satisfaction.
5. Marketing Campaign Analysis: Assessing the effectiveness of marketing campaigns and identifying key drivers of success.
6. User Behavior Analysis: Understanding how users interact with a product or service to improve user experience
7. Risk Assessment: Evaluating factors that contribute to risk in various domains, such as credit risk or operational risk.



---
## 📝 Contributing

Contributions are welcome!  
Feel free to open issues, submit pull requests, or suggest new recipes. If you have questions, please open an issue or contact the repository maintainers.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ for the data community.
