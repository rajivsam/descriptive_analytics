# 📊 Descriptive Analytics Recipes

Welcome to the **Descriptive Analytics Recipes** repository!  
---
This repository is dedicated to providing practical recipes and examples for performing descriptive analytics on operational datasets. It aims to help users understand their data better, identify patterns, and prepare for further analysis or modeling. Most of the recipes are designed to be accessible to both business managers and data scientists, ensuring that everyone can benefit from the insights derived from operational data. Most businesses do not have data on the scale of large enterprises. They do have operational data that can be analyzed, the results of which can be applied to improve business efficiency and decision-making. This repository provides a systematic approach to analyzing such data, focusing on profiling metrics before monitoring them, addressing the curse of dimensionality, and summarizing datasets for better human interpretation.


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

The basic idea of descriptive analytics is to provide a comprehensive understanding of operational data. A typical workflow includes:

1. Defining the business problem and the associated operational data.
2. Defining the period and metrics to be analyzed.
3. Transforming the raw data from step one to match step two.
4. Working with your data science team to develop a set of descriptive models that give you an understanding of the business problem instance represented by the data.
5. Interpreting the results of the descriptive models to gain insights into the business problem.
6. Developing a set of monitoring metrics to track the business problem over time. The monitoring metrics should be based on the descriptive models developed in step four and should be designed to provide early warning signals of potential issues or opportunities.

Please see the olist case study for a detailed example of this workflow. The example illustrates how to apply descriptive analytics to a real-world dataset, focusing on profiling metrics before monitoring them, addressing the curse of dimensionality, and summarizing datasets for better human interpretation. The examples directory also contains other case studies that follow a similar approach, providing a systematic way to analyze operational data.
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
