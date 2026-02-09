# Executive Summary (Assignment 8 — Bankruptcy EDA & Clustering)

## What problem did we solve?
We analyzed a U.S. bankruptcy dataset and asked a simple question: **can an unsupervised method (k-means clustering) separate firms that failed from firms that stayed alive** using only financial variables? The deliverable is a **clean, well-documented workflow** that can be re-run end‑to‑end in R.

## What data did we use?
The dataset contains company identifiers, a status label (**alive** or **failed**), a year field, and 18 numeric financial variables (`X1`–`X18`). Many firms appear across multiple years, so we also created a **company-level** table (one row per firm) by keeping the **most recent year** for each company.

## What did we do (in plain language)?
1. **Checked data types and structure** to ensure text fields were treated as categories and numeric fields were treated as numbers.
2. **Checked for missing values** and documented the result.
3. **Inspected outliers and unusual values** using boxplots and summaries.
4. **Engineered new information** from the raw columns (e.g., a log “size” proxy and a simple year‑over‑year change feature).
5. **Split the data into training and test sets** so evaluation is honest and does not leak information.
6. **Transformed and scaled** numeric variables so distance-based clustering is meaningful.
7. **Built a k-means model with k = 2 clusters** on the training set.
8. **Mapped clusters to the two outcomes** (alive/failed) using training data only, then scored the model on the test set.

## What did we find?
* **Clustering reveals structure** in the financial data, but bankruptcy prediction is challenging because:
  * failure is **rare** (class imbalance),
  * many financial variables are **skewed** with **extreme outliers**, and
  * healthy and failing firms often have **overlapping** financial profiles.

## What does it mean for decision-makers?
K-means clustering is best viewed as a **baseline** or an **exploratory tool**: it can highlight groups of firms with different financial patterns and help analysts spot unusual profiles, but it should **not** be the only method used for bankruptcy risk scoring. For stronger prediction, supervised methods (e.g., logistic regression, tree/boosting models) or more flexible clustering models (e.g., mixture models) are typically required.

## Recommended next steps
1. Compare against a supervised baseline (logistic regression or gradient boosting).
2. Explore clustering methods designed for skewed distributions and imbalance.
3. Add richer temporal features (multi‑year trends) and evaluate stability over time.
