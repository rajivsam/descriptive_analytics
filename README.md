![Header Image](https://github.com/rajivsam/descriptive_analytics/blob/main/images/desc_analytics_infographic.png)

# 📊 Descriptive Analytics Recipes

Welcome to the **Descriptive Analytics Recipes** repository.

---

## What is Descriptive Analytics?

Descriptive analytics summarizes historical business data to answer the question, “What happened?” It uses aggregates, visualizations, segmentation, and explanatory models to reveal patterns in past behavior. Examples include customer purchase paths in an e-commerce store and repayment patterns in a loan portfolio.

### Why It Matters

- Provides the foundation for predictive and prescriptive analytics by turning raw history into structured insights.
- Informs model design and feature engineering (explanatory models often feed predictive models).
- Reduces risk by highlighting past failures and opportunities before they are repeated.

### Approaches and Focus

We can categorize analysis approaches based on how time relates to the units being analyzed:

- **Cross-sectional analysis:** Analyze multiple units (such as people or companies) at a single point in time. Think of this as a snapshot.
- **Longitudinal (time-series) analysis:** Analyze a single unit across multiple points in time to track how it changes.
- **Panel analysis:** Combine both by analyzing the same set of multiple units across multiple points in time.

This repository focuses on cross-sectional data analysis, with an emphasis on graph-based approaches. For longitudinal analysis, see [tseda](https://github.com/rajivsam/tseda), a package designed specifically for this use case. It provides tools for exploring and summarizing patterns in a single time-series variable. For an overview of the package and what it offers, see the [tseda announcement blog post](https://rajivsam.github.io/r2ds-blog/posts/tseda%20announcement/). Examples and full details are available in the [tseda GitHub repository](https://github.com/rajivsam/tseda).

Graph-based analysis can be a powerful tool for descriptive analytics. Traditional machine learning approaches may be sufficient for _independent and identically distributed_ (IID) data. When that assumption is not reasonable, you need analysis methods that account for dependencies in the data. Graph-based methods handle these dependencies naturally.

A large amount of enterprise data resides in relational databases. A common bottleneck when using graphs for descriptive analytics is transforming data from its native relational format into a graph analysis model. For this reason, this repository includes a full section dedicated to relational-to-graph transformation. See [this video](https://www.youtube.com/watch?v=d997pgkwtGY&list=PL-lbroKJyNLDJ44l60GvHgcYtFh0pNFek&index=4&t=215s) for a summary of the process.

For an overview, see [this video](https://www.youtube.com/watch?v=MwXKC_oloH8). For sample walkthroughs, see [this playlist](https://www.youtube.com/playlist?list=PL-lbroKJyNLDJ44l60GvHgcYtFh0pNFek).

---

## 📝 Contributing

Contributions are welcome.
Feel free to open issues, submit pull requests, or suggest new recipes. If you have questions, please open an issue or contact the repository maintainers.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ for the data community.
