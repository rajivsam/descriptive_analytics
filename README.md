# 📊 Descriptive Analytics Recipes

Welcome to the **Descriptive Analytics Recipes** repository!  
---
This repository contains recipes illustrating the use of descriptive statistical methods and machine learning methods to describe facets of your dataset that are relevant to main machine learning task. For example, if your data contains multiple populations, a descriptive task will capture this information. This informs how you want to build machine learning models for this data. In other words, if there is structure in the data that is relevant to your principal machine learning tasks, you need a process component to capture and profile this. This is what descriptive analytics aims to do.xs

## 🗂️ Table of Contents

- [📊 Descriptive Analytics Recipes](#-descriptive-analytics-recipes)
  - [Welcome to the **Descriptive Analytics Recipes** repository!](#welcome-to-the-descriptive-analytics-recipes-repository)
  - [🗂️ Table of Contents](#️-table-of-contents)
  - [🔍 Overview](#-overview)
  - [📁 Directory Structure](#-directory-structure)
  - [⚙️ Getting Started](#️-getting-started)
  - [📚 Recipes \& Examples](#-recipes--examples)
  - [📝 Contributing](#-contributing)
  - [📄 License](#-license)

---

## 🔍 Overview


This repository contains recipes to describe datasets with the following elements:
1. The raw data is operational and has a timestamp capturing the interaction activity of interest. Examples could be transactional data, data from your health/fitness application, your blood glucose monitor.
2. Your use case needs to analyze specific metrics across a time period. This time period is present in the raw dataset.
3. You apply an aggregation and or a pivoting operation to compute the metric of interest for the time period
4. You analyze the cleaned and prepared data for the time period using descriptive analytics techniques.
5. An example is provided using ecommerce data. 

Real-world datasets, such as the Olist e-commerce dataset, are used to demonstrate each step. The basic assumptions made about the data are as follows:

1. The key assumption behind this repository is that the data you are working with is operational and has a timestamp capturing the interaction activity of interest. This means that the data is not static but rather dynamic, reflecting real-time interactions or transactions.

2. Business managers and a data scientist are working together to analyze specific metrics across a time period. The team knows what metrics are relevant to track and monitor.
3. Profiling a metric is a precursor to monitoring it. This means that before you can effectively monitor a metric, you need to understand its behavior and characteristics over time.
4. Business managers and data scientists often need to analyze several metrics across a time period. The curse of dimensionality is a common challenge in this context. Luckily, the machine learning and optimization community has developed techniques to address this issue.
5. Humans have cognitive limitations when it comes to analyzing large datasets. Therefore, the repository focuses on techniques that help summarize and visualize data effectively, making it easier for humans to interpret and understand.
6. Many small and medium-sized businesses do not have data on the scale of large enterprises. However, they have operational data that can be used to derive insights and make informed decisions. You don't need to use the tools and techniques designed for large-scale data to analyze operational data of small and medium-sized businesses. Hopefuly, this repository will convince you of this. Mapping your operational data to the techniques and tools used in this repository still takes skill and expertise, but it is a more accessible starting point for many businesses.

## 📁 Directory Structure

```
descriptive_analytics/
├── data/               # Sample datasets
├── notebooks/          # Jupyter notebooks with recipes & walkthroughs
├── examples/           # examples illustrating descriptive analytics
├── images/             # Visualizations & diagrams
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Getting Started

1. **Clone the repository:**
     ```bash
     git clone https://github.com/yourusername/descriptive_analytics.git
     cd descriptive_analytics
     ```

2. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

3. **Explore the conceptual documents and examples:**
   - Read the concept discussions in the `concept_discussion/` directory.
   - Pick a case study from the `examples/` directory to follow the implementation sketch.

---

## 📚 Recipes & Examples
The recipes and examples are created to emphasize a systematic approach to preparing and analyzing operational data. The concepts folder contains the relevant notes that are referenced in the case study discussions.

---

## 📝 Contributing

Contributions are welcome!  
Feel free to open issues, submit pull requests, or suggest new recipes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Made with ❤️ for the data community.
