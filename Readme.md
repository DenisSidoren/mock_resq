## ResQ Assignment

prepared by Denis Sidorenko, sidorenko.den95@gmail.com

## How to use the Repo

There are two ways to check on the provided solution:

1. Interactively go through the solution in the [Colab Notebook](https://colab.research.google.com/drive/1ZMeq13NYoRbxeUcEAbRc2ZUD2B3xpJ-_?usp=sharing)
2. Use the code from this repository on your local machine following the short instruction below:
   1. Clone the repo and add the `mock_resq.db` file in the root
   2. Launch `problem1.py` file to play a data pipeline and create the presentation table in the database. All SQL queries are stored in the `conf.py`
   3. Open `problem2.ipynb` and paly all the cells to get the info about newly created presentation table and some analytics on top of that.

## The Task

**The problem #1**

You have just landed your dream job at ResQ Club, but you need to work with an analyst with poor SQL skills. They’d like to make some queries about ResQ customers but they can only write select statements and don’t know how to join tables. Therefore they’re asking you to provide them the needed data in one presentation table.

The analyst wants to make at least the following queries:

* Query to find the top 10 partners by sales
* Query to identify the customers’ favourite partner segments (default offer types). Partners are the companies who sell surplus items on the marketplace.
* Query to find out what is the M1 retention for any given customer cohort. A cohort consists of customers who made their first order within the same month (M0). M1 retention is the share of customers who have made at least one purchase one month after their first purchase month.

**Deliverable #1:** a simple data pipeline where this kind of presentation table is being created to help the analyst. Note that it’s not necessary to answer these questions yourself, but feel free to do that, if you want to ease up the analyst’s life.

**Problem #2** The marketing team wants to know how much can they spend on acquiring new customers to the platform. Therefore, they need to know how valuable an average customer is to us during their whole expected lifetime on the platform. Use the newly created presentation table and perform data analysis about Customer Lifetime Value (CLV).

**Deliverable #2:** An analysis about the expected Customer Lifetime Value (CLV). The calculation should consider factors such as purchase frequency, average order value, and average customer lifespan (the time between customers' first and last purchase). Present your results in a Jupyter Notebook or similar format.

**Problem #3**

You will get the instructions in the technical interview. This task will be about modifying your previous solutions. It will be a simple and short pair-coding session to ensure that you understand your own code – don’t stress about it!

**Data**

* `resq_user`,  **`resq_order` and**  `resq_provider` tables (psst, the business teams call users customers and providers are partners)

**Other instructions**

Answer the questions using the above data, save your work in a public Github repository and share it with us within one week from receiving these instructions (different applicants might receive the instructions at different times).

This task should take you 2-4 hours, so don’t overthink it. We’ll be asking some questions about your solution in the next interview, so be prepared to explain your choices.
