DB_NAME = 'mock_resq.db'

CREATE_TABLE_QUERY = """
CREATE TABLE analytics (
    user TEXT,
    purchase_number INTEGER,
    total_sales REAL,
    currency TEXT,
    favorite_segment TEXT,
    M0_cohort TEXT,
    M1_retention INTEGER,
    lifespan_days INTEGER);
"""

INSERT_QUERY = """
INSERT INTO analytics (user, purchase_number, total_sales, currency, favorite_segment, M0_cohort, M1_retention, lifespan_days)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""

REMOVE_TABLE_QUERY = """
DROP TABLE IF EXISTS analytics;
"""

TRANSFORM_QUERY = """
SELECT ord.userId as user,
       COUNT(*) as purchase_number,
       SUM(ord.sales) as total_sales,
       ord.currency as currency,
       GROUP_CONCAT(p.defaultOfferType) as segments,
       STRFTIME('%Y-%m', MIN(ord.createdAt)) AS M0_cohort,
       CASE
           WHEN (JULIANDAY(MAX(ord.createdAt)) - JULIANDAY(MIN(ord.createdAt))) > 30 THEN 1
           ELSE 0
       END as M1_retention,
       ROUND(JULIANDAY(MAX(ord.createdAt)) - JULIANDAY(MIN(ord.createdAt)), 0) as lifespan_days
FROM orders ord
LEFT JOIN providers p ON ord.providerId = p.id
GROUP BY ord.userId, ord.currency;
"""
